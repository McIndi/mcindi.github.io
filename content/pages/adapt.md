Title: Adapt - Turn a Folder Into a Secure API Server
Slug: adapt
Template: product
Status: hidden
Summary: A FastAPI server that turns files in a directory into APIs, searchable resources, UIs, and streaming endpoints. Authentication, RBAC, full-text search, and an admin interface built in. Point it at a folder and go.
save_as: software/adapt/index.html
url: software/adapt/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">MIT &bull; Python &bull; FastAPI</div>
        <h1>Adapt</h1>
        <p>A FastAPI server that turns files in a directory into APIs, searchable resources, UIs, and streaming endpoints. Point it at a folder and datasets become CRUD APIs, documents become browsable pages, media files become streaming players, and the whole tree becomes discoverable through permission-aware search and automation-friendly resource exposure.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="https://github.com/McIndi/adapt" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Adapt%20Support%20Inquiry">Request Support Quote</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <span class="stat-num">5</span>
          <span class="stat-label">File types auto-served</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">RBAC</span>
          <span class="stat-label">Auth &amp; permissions built in</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">MIT</span>
          <span class="stat-label">Open source license</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Your Folder Is Already a Server</h2>
      <p>Adapt auto-discovers resources and mounts routes. Drop files in, get APIs, search, and UIs out.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Data</span>
        <h3>Dataset CRUD APIs</h3>
        <p>CSV, XLSX, and Parquet files become full CRUD endpoints with schema exposure, caching, atomic writes, and sortable tables. DataTables UI is included at no extra configuration.</p>
      </article>
      <article class="card">
        <span class="badge">Documents</span>
        <h3>Document Browser</h3>
        <p>Markdown and HTML files are rendered and served as formatted pages. Adapt generates a landing page that adapts to what each user is permitted to see and makes large document trees easier to navigate as content grows.</p>
      </article>
      <article class="card">
        <span class="badge">Media</span>
        <h3>Streaming Media</h3>
        <p>Video and audio files become streaming endpoints with built-in player and gallery UIs. Meeting recordings, training walkthroughs, and Zoom exports are one link away.</p>
      </article>
      <article class="card">
        <span class="badge">Discovery</span>
        <h3>Permission-Aware Search</h3>
        <p>Index datasets, documents, and other mounted resources for full-text search while still respecting the same permissions used everywhere else. Users find what they are allowed to see without exposing what they are not.</p>
      </article>
      <article class="card">
        <span class="badge">Integration</span>
        <h3>MCP Resource Exposure</h3>
        <p>Expose the same folder through an MCP interface for AI agents and automation tooling. Resource ordering and discovery controls make large collections easier to consume programmatically.</p>
      </article>
      <article class="card">
        <span class="badge">Extensibility</span>
        <h3>Custom Python Routers</h3>
        <p>Drop a <code>.py</code> file with a FastAPI router into the folder and Adapt mounts it automatically. Live API endpoints without a restart.</p>
      </article>
      <article class="card">
        <span class="badge">Security</span>
        <h3>Auth &amp; RBAC Built In</h3>
        <p>Session cookies, API keys, PBKDF2 password hashing, CSRF protection, CSP, HSTS, and RBAC with users, groups, and permissions are all included and enforced by default.</p>
      </article>
      <article class="card">
        <span class="badge">Operations</span>
        <h3>Admin UI &amp; Audit Logs</h3>
        <p>A full admin interface for managing users, groups, permissions, API keys, cache, and locks. Smarter lock handling and security-relevant audit logs help shared environments stay predictable under load.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Built for Internal Data Sharing</h2>
      <p>Adapt covers the use cases that are too simple for a full application but too sensitive for an S3 bucket.</p>
    </div>
    <div class="grid">
      <article class="card">
        <h3>Client Deliverable Portals</h3>
        <p>Share data exports, analysis results, and recorded walkthroughs with clients. Control exactly who can see what without building a custom portal or using a cloud storage service.</p>
      </article>
      <article class="card">
        <h3>Internal Data APIs</h3>
        <p>Turn operational data files into queryable REST APIs for downstream tooling and dashboards. No database schema migrations, no web framework boilerplate.</p>
      </article>
      <article class="card">
        <h3>Secure Document Distribution</h3>
        <p>Publish runbooks, documentation, and reference material to a team with per-user access control. Documents stay in a folder you already manage.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Get Started in Three Commands</h2>
    </div>
    <div class="card" style="max-width:640px;">
      <pre style="margin:0;background:#0f172a;color:#e2e8f0;padding:1.25rem;border-radius:12px;overflow-x:auto;font-size:.9rem;"><code>pip install adapt-server
adapt addsuperuser --username admin /path/to/docroot
adapt serve /path/to/docroot</code></pre>
    </div>
    <p style="margin-top:1rem;color:var(--muted);">Then visit <code>http://localhost:8000/admin/</code> to configure users, groups, and permissions.</p>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Works Well With</h2>
      <p>Adapt covers the folder-to-API layer. These tools cover what surrounds it.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">GPLv3 &bull; Dev Preview</span>
        <h3>PKI Workbench</h3>
        <p>Bring your own CA. Adapt enforces TLS and RBAC out of the box. Issue its server certificate from PKI Workbench to keep the whole trust chain under your control.</p>
        <a class="btn btn-ghost" href="/software/pki-workbench/">Learn More &rarr;</a>
      </article>
      <article class="card">
        <span class="badge">Reference Arch &bull; Preview</span>
        <h3>Project Armory</h3>
        <p>Both speak MCP. Adapt exposes a folder&rsquo;s resources over MCP for agent tooling; Project Armory is a reference architecture for running agents like that under enterprise identity, secrets, and audit controls.</p>
        <a class="btn btn-ghost" href="/software/project-armory/">Learn More &rarr;</a>
      </article>
      <article class="card">
        <span class="badge">Ansible &bull; DevOps</span>
        <h3>Ansible Dev Sandbox</h3>
        <p>Deploying Adapt with Ansible? Test the roles that provision it in a container-isolated, CI-ready harness before they touch a real environment.</p>
        <a class="btn btn-ghost" href="/software/ansible-dev-sandbox/">Learn More &rarr;</a>
      </article>
    </div>
  </div>
</section>

<section id="contact" style="margin-top:0;">
  <div class="container">
    <div class="card">
      <h3>Free to Use. Commercially Supported.</h3>
      <p>Adapt is MIT licensed. McIndi offers commercial support contracts for organizations that need SLA-backed maintenance, security review assistance, and custom plugin development.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://github.com/McIndi/adapt" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Adapt%20Support%20Inquiry">Request Support Quote</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
