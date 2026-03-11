Title: Adapt Security Hardening: What We Shipped and Why
Author: Cliff
Date: 2026-03-10 10:00
Category: Announcements
Tags: server, file sharing, authentication, permissions, Python, FastAPI, security, CSRF, CSP, HSTS
Summary: A focused security hardening pass for Adapt, a lightweight server that turns a folder into a secure, queryable workspace for data, documents, and media.
Slug: adapt-security-hardening
Status: published

This release is a focused security hardening pass. No new features, no API surface changes, just a set of defenses that Adapt should have had from the start, now fully in place. Here's a walkthrough of what changed and the reasoning behind each decision.

---

## CSRF Protection, End to End

The biggest addition is full Cross-Site Request Forgery (CSRF) protection using the double-submit cookie pattern.

### How it works

On every request, Adapt now generates a random CSRF token and sets it as a non-HttpOnly cookie (`adapt_csrf`). Any unsafe HTTP method (POST, PATCH, PUT, DELETE) that is authenticated via a session cookie must also supply that same token in the `X-CSRF-Token` request header (or a `csrf_token` form field for standard HTML form submissions).

The validation logic lives in a new `adapt/security.py` module:

```python
async def validate_csrf(request: Request) -> JSONResponse | None:
    if not requires_csrf_validation(request):
        return None

    expected = request.cookies.get(CSRF_COOKIE_NAME)
    provided = request.headers.get(CSRF_HEADER_NAME)
    # ... form field fallback omitted for brevity

    if not secrets.compare_digest(str(provided), str(expected)):
        return JSONResponse(status_code=403, content={"detail": "Invalid CSRF token"})

    return None
```

`secrets.compare_digest` ensures constant-time comparison, which prevents timing side-channels.

### Who is exempt

API-key-only clients — scripts, automation, anything that authenticates purely via `X-API-Key` with no session cookie — are exempt from CSRF checks by design. CSRF attacks rely on a browser silently sending credentials (session cookies) cross-origin. An API key passed in a header cannot be sent that way.

The edge case worth calling out: if a request carries **both** a session cookie and an API key header, CSRF still applies. The presence of the session cookie is what triggers the requirement, not which auth method "wins."

```python
def requires_csrf_validation(request: Request) -> bool:
    if request.method.upper() in SAFE_METHODS:
        return False
    has_session_cookie = bool(request.cookies.get(SESSION_COOKIE_NAME))
    has_api_key_header = bool(request.headers.get(API_KEY_HEADER))
    if has_api_key_header and not has_session_cookie:
        return False
    return has_session_cookie
```

### Frontend integration

Every template and JS module that makes mutating fetch calls now passes the token. A helper function is defined once per page context:

```javascript
function csrfHeaders(headers = {}) {
    const token = window.getAdaptCsrfToken ? window.getAdaptCsrfToken() : '';
    if (!token) return headers;
    return { ...headers, 'X-CSRF-Token': token };
}
```

The admin UI, DataTables UI, and profile page all use this. For custom companion templates (user-supplied `.adapt/*.index.html` files), the dataset plugin now automatically injects the CSRF fetch-patching script at render time — so custom UIs get CSRF support without any changes required.

---

## Response Security Headers

All responses now carry a standard set of hardening headers, applied in the security middleware:

| Header | Value |
|---|---|
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `DENY` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` |
| `Content-Security-Policy` | see below |
| `Strict-Transport-Security` | set only when TLS is enabled |

The CSP allows scripts from `self` and the CDN origins Adapt uses (Bootstrap, jQuery, DataTables). HSTS is conditional — you don't want to set it on a plain HTTP deployment, because it will cause browsers to refuse future HTTP connections to the same host.

---

## Host Header Protection

Adapt now installs FastAPI's `TrustedHostMiddleware` when a specific bind host is configured:

```python
allowed_hosts = build_allowed_hosts(config.host)
if allowed_hosts != ["*"]:
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)
```

When the host is `0.0.0.0` or `::` (i.e., "bind to everything"), all hosts are permitted — consistent with the expectation that you've placed a reverse proxy in front. When a specific host is set, only that host plus `localhost` and `127.0.0.1` are accepted. This blocks Host header injection attacks that can poison redirects, cache entries, and password-reset links.

---

## Open Redirect Hardening

Previously, login redirects were built by concatenating the `next` query parameter directly:

```python
# Before
return RedirectResponse(url=f"/auth/login?next={request.url}", status_code=302)
```

This is an open redirect. An attacker who tricks a user into visiting `/auth/login?next=https://evil.example` gets a redirect to their phishing site after login.

The fix is a new `adapt/security_urls.py` module with explicit validation:

```python
def is_safe_next_path(value: str | None) -> bool:
    if not value:
        return False
    candidate = unquote(value).strip()
    if candidate.startswith("//"):
        return False
    parsed = urlsplit(candidate)
    if parsed.scheme or parsed.netloc:
        return False
    return candidate.startswith("/")
```

Note that the URL is decoded before validation — `https%3A//evil.example` would bypass a check that only looks at the raw string. All redirect construction throughout the codebase now goes through `login_redirect_url()`, which calls this validator and falls back to `/` for anything that doesn't pass.

The client-side login form applies matching validation in JavaScript before following the redirect, providing a second layer of defense.

---

## Sensitive Data Removed from API Responses

The admin user endpoints (`GET /admin/users`, `POST /admin/users`, `GET /admin/groups/{id}`) were previously returning the raw `User` SQLModel, which includes `password_hash`. That field was being serialized into API responses.

Two new response models fix this:

- `UserPublic` — used for user list and create responses
- `GroupReadSafe` — used for group detail responses, with users represented via a nested `GroupUserRead` model

```python
@router.get("/users", response_model=List[UserPublic])
def list_users(...):
    ...
    return [
        UserPublic(
            id=u.id,
            username=u.username,
            is_active=u.is_active,
            is_superuser=u.is_superuser,
            created_at=u.created_at,
        )
        for u in result
    ]
```

The tests now explicitly assert the absence of the field:

```python
assert "password_hash" not in users[0]
```

---

## TLS Flag Validation

A small but useful guard was added to the `serve` command: passing only `--tls-cert` without `--tls-key` (or vice versa) now raises an error immediately rather than silently starting an HTTP server.

```python
if (tls_cert and not tls_key) or (tls_key and not tls_cert):
    raise ValueError("Both --tls-cert and --tls-key must be provided together")
```

---

## Test Infrastructure

The test suite required updates to function in a CSRF-enforced environment. Rather than adding token headers to every individual test, `conftest.py` now patches `TestClient.request` with an `autouse` fixture that automatically attaches the CSRF token for unsafe methods when a valid cookie is present:

```python
@pytest.fixture(autouse=True)
def auto_csrf_for_testclient(monkeypatch):
    original_request = TestClient.request

    def patched_request(self, method, url, *args, **kwargs):
        method_name = str(method).upper()
        headers = kwargs.get("headers") or {}
        if method_name in {"POST", "PUT", "PATCH", "DELETE"}:
            token = self.cookies.get("adapt_csrf")
            has_csrf_header = any(k.lower() == "x-csrf-token" for k in headers.keys())
            if token and not has_csrf_header:
                headers = {**headers, "X-CSRF-Token": token}
                kwargs["headers"] = headers
        return original_request(self, method, url, *args, **kwargs)

    monkeypatch.setattr(TestClient, "request", patched_request)
```

New dedicated CSRF tests cover the failure cases: missing cookie, invalid token, and the mixed-auth scenario.

---

## Documentation

The manual was substantially trimmed. Sections that described behavior not yet implemented — multi-server scaling, GraphQL, WebSocket support, GDPR compliance workflows, detailed incident response procedures — have been removed or replaced with accurate descriptions of what the code actually does.

The README was similarly simplified: a concise feature list and quick-start commands rather than an exhaustive marketing document.

This matters for users and contributors. Aspirational documentation that diverges from the implementation is misleading and erodes trust. The manual now reflects what you get when you install Adapt today.

---

## Deployment Notes

A few practical reminders that come out of this work:

- **Use TLS in any non-local environment.** Several of the protections added here (HSTS, secure cookies) are only effective over HTTPS. `--tls-cert` and `--tls-key` must be provided together.
- **API-key clients don't need to change anything.** If you're accessing Adapt programmatically via `X-API-Key`, CSRF enforcement doesn't apply to you.
- **Browser clients get CSRF automatically.** The cookie is set on first visit; the admin UI, DataTables, and profile pages all include the header on mutations. Custom companion templates get fetch-patching injected automatically.

---

That covers everything in this changeset. Questions and feedback welcome in the usual places.