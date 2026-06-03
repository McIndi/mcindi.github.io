Title: Project Armory — Secure AI Agent Platform for Regulated Enterprises
Slug: project-armory
Template: product
Status: hidden
Summary: An open reference architecture for deploying AI agents inside regulated enterprises. An auditable Kubernetes platform with Keycloak OIDC, OpenBao secrets and PKI, TLS everywhere, and the BeeAI agent runtime — provisioned end to end with Ansible and OpenTofu.
save_as: software/project-armory/index.html
url: software/project-armory/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">Reference Architecture &bull; Kubernetes &bull; Preview</div>
        <h1>Project Armory</h1>
        <p>An open reference architecture for running AI agents inside regulated enterprises. A complete, auditable Kubernetes platform — Keycloak OIDC across the stack, OpenBao for secrets and PKI, TLS-everywhere ingress, and the BeeAI agent runtime — provisioned end to end with Ansible and OpenTofu.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="https://github.com/McIndi/project-armory" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Project%20Armory%20Inquiry">Talk to an Engineer</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <span class="stat-num">OIDC</span>
          <span class="stat-label">Identity across the stack</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">IaC</span>
          <span class="stat-label">Ansible + OpenTofu provisioning</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">Preview</span>
          <span class="stat-label">Reference architecture, evolving</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="notice">
      <strong>Reference Architecture:</strong> Project Armory is a working blueprint for secure agent deployment, intended for evaluation and as a foundation to adapt to your environment. Production hardening — secret backends, network policy, and security review against your own controls — is expected before production use.
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Security-First by Construction</h2>
      <p>Every layer is wired for identity, encryption, and auditability — not bolted on after the fact.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Identity</span>
        <h3>Keycloak OIDC Everywhere</h3>
        <p>A single identity provider wired through the whole stack, including k3s API authentication. Users and services authenticate against Keycloak, with OIDC-driven access to the Kubernetes API and the Headlamp dashboard.</p>
      </article>
      <article class="card">
        <span class="badge">Secrets &amp; PKI</span>
        <h3>OpenBao Secret Management</h3>
        <p>OpenBao manages secrets and PKI, integrated with the Vault Secrets Operator and cert-manager. Credentials are generated and rotated automatically — including hands-off realm admin password cycling.</p>
      </article>
      <article class="card">
        <span class="badge">Encryption</span>
        <h3>TLS-Everywhere Ingress</h3>
        <p>RBAC and TLS-everywhere ingress configuration by default. cert-manager and nginx-ingress issue and terminate certificates so traffic is encrypted end to end across the platform.</p>
      </article>
      <article class="card">
        <span class="badge">Agent Runtime</span>
        <h3>BeeAI Agent Stack</h3>
        <p>Agents run on the BeeAI Agent Stack, a Linux Foundation project, deployed onto the secured k3s platform — giving AI workloads a runtime that inherits the platform's identity and secret controls.</p>
      </article>
      <article class="card">
        <span class="badge">Infrastructure as Code</span>
        <h3>Ansible + OpenTofu</h3>
        <p>End-to-end provisioning via Ansible playbooks and OpenTofu. Granular task execution through Ansible tags, with multi-component readiness validation run after deployment.</p>
      </article>
      <article class="card">
        <span class="badge">Evaluation</span>
        <h3>Vagrant Local Deploy</h3>
        <p>Stand up the full platform inside a Vagrant VM for local evaluation. Retrieve credentials directly from OpenBao and inspect synced Kubernetes secrets without touching production infrastructure.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Who It&rsquo;s Built For</h2>
      <p>Organizations that want to adopt AI agents without giving up the controls their environment demands.</p>
    </div>
    <div class="grid">
      <article class="card">
        <h3>Regulated AI Adopters</h3>
        <p>Healthcare, financial services, and high-security teams that need agentic AI to run under the same identity, secret, and audit controls as the rest of their estate — not as an exception to them.</p>
      </article>
      <article class="card">
        <h3>Security &amp; Platform Teams</h3>
        <p>Engineers who want a vetted, auditable starting point for a Kubernetes AI platform — OIDC, PKI, and TLS already integrated — instead of assembling and securing the pieces from scratch.</p>
      </article>
      <article class="card">
        <h3>Air-Gap &amp; Data-Sovereign Environments</h3>
        <p>Deployments that must stay on-premises and self-hosted. Identity, secrets, certificates, and agent runtime all run inside infrastructure you control, with no external dependency.</p>
      </article>
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <div class="card">
      <h3>Open Architecture. Hands-On Support.</h3>
      <p>Project Armory is open source and available now for evaluation. McIndi can help you adapt the architecture to your environment, integrate it with existing identity and secret backends, and harden it for production.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://github.com/McIndi/project-armory" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Project%20Armory%20Inquiry">Talk to an Engineer</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
