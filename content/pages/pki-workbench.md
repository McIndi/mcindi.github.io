Title: PKI Workbench — Private Certificate Authority Management
Slug: pki-workbench
Template: product
Status: hidden
Summary: A Django-based certificate authority management tool for building and operating private PKI workflows. Root and intermediate CAs, end-entity issuance, certificate profiles, and a REST API — without the OpenSSL scripting.
save_as: software/pki-workbench/index.html
url: software/pki-workbench/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">GPLv3 &bull; Django &bull; Development Preview</div>
        <h1>PKI Workbench</h1>
        <p>A Django-based certificate authority management tool for building and operating private PKI workflows. Root and intermediate CAs, end-entity issuance, certificate profiles, and a REST API — without OpenSSL scripting or commercial CA overhead.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="https://github.com/McIndi/pki_workbench" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=PKI%20Workbench%20Inquiry">Talk to an Engineer</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <span class="stat-num">Root+</span>
          <span class="stat-label">Intermediate CA support</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">REST</span>
          <span class="stat-label">Full API + OpenAPI schema</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">Dev</span>
          <span class="stat-label">Currently in development preview</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="notice">
      <strong>Development Preview:</strong> PKI Workbench is actively developed and suitable for evaluation and internal prototyping. Production hardening — secret management, strict TLS config, production database, and security review — is required before production deployment.
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Platform Capabilities</h2>
      <p>A complete private CA workflow in a single Django application.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">CA Management</span>
        <h3>Root &amp; Intermediate CAs</h3>
        <p>Create root CAs with configurable key algorithm and certification depth. Issue intermediate CAs with depth validation enforced against root policy.</p>
      </article>
      <article class="card">
        <span class="badge">Issuance</span>
        <h3>End-Entity Certificate Issuance</h3>
        <p>Issue end-entity certificates with full control over key algorithm, key size, curve, SAN DNS entries, Key Usage, and Extended Key Usage.</p>
      </article>
      <article class="card">
        <span class="badge">Policy</span>
        <h3>Certificate Profiles</h3>
        <p>Define reusable issuance policies with key and extension defaults, optional subject constraints, and auto-fill on the issue form. Derive a profile directly from an existing certificate.</p>
      </article>
      <article class="card">
        <span class="badge">Artifacts</span>
        <h3>Certificate Artifact Downloads</h3>
        <p>Download public cert, cert chain, CSR, and cert/key bundle ZIP from a dedicated certificate detail page. Consistent filename conventions across all artifacts.</p>
      </article>
      <article class="card">
        <span class="badge">Integration</span>
        <h3>REST API &amp; OpenAPI Schema</h3>
        <p>Full REST API covering CAs, certificates, profiles, and workflows. OpenAPI schema at <code>/api/schema/</code> for integration with CI/CD pipelines and automation tooling.</p>
      </article>
      <article class="card">
        <span class="badge">Visibility</span>
        <h3>Dashboard &amp; Trust Chain View</h3>
        <p>Home dashboard with CA and certificate counts, certificates approaching expiration, and a recursive clickable CA hierarchy. Searchable CA and profile selectors throughout.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Who It&rsquo;s Built For</h2>
      <p>Teams that need a private CA but don&rsquo;t need the complexity of a commercial PKI platform.</p>
    </div>
    <div class="grid">
      <article class="card">
        <h3>Security &amp; Infrastructure Teams</h3>
        <p>Stand up a private CA for internal TLS, mutual authentication, and service-to-service trust — without maintaining a tangle of OpenSSL commands or purchasing a commercial CA platform.</p>
      </article>
      <article class="card">
        <h3>DevOps &amp; Platform Engineering</h3>
        <p>Integrate with CI/CD pipelines via the REST API to automate certificate issuance and renewal for containerized services, internal APIs, and test environments.</p>
      </article>
      <article class="card">
        <h3>Regulated Environments</h3>
        <p>Keep certificate issuance entirely on-premises with full audit trails. Control the key lifecycle without third-party CA involvement or cloud dependency.</p>
      </article>
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <div class="card">
      <h3>Available for Evaluation &amp; Early Adoption</h3>
      <p>PKI Workbench is GPLv3 open source and available now for evaluation. McIndi can assist with deployment planning, production hardening, and custom integrations as the project matures toward general availability.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://github.com/McIndi/pki_workbench" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=PKI%20Workbench%20Inquiry">Talk to an Engineer</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
