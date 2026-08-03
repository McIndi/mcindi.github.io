Title: Ansible Dev Sandbox - Enterprise-Grade Role Testing
Slug: ansible-dev-sandbox
Template: product
Status: hidden
Summary: A reproducible testing harness for Ansible role development that mirrors how enterprise environments actually behave: container-isolated, environment-variable configured, and CI-ready.
save_as: software/ansible-dev-sandbox/index.html
url: software/ansible-dev-sandbox/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">Ansible &bull; DevOps &bull; Enterprise CI/CD</div>
        <h1>Ansible Dev Sandbox</h1>
        <p>A reproducible testing harness for Ansible role development that mirrors how enterprise environments actually behave. Environment-variable configuration, Molecule test scenarios, and container-based execution without committing sensitive files.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="https://github.com/McIndi/ans_dev_sandbox_playbook" target="_blank" rel="noopener noreferrer">GitHub Repo</a>
          <a class="btn btn-ghost" href="https://github.com/McIndi/ans_dev_sandbox_playbook/wiki" target="_blank" rel="noopener noreferrer">Documentation</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <span class="stat-num">3</span>
          <span class="stat-label">Molecule test scenarios</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">0</span>
          <span class="stat-label">Committed ansible.cfg files</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">CI</span>
          <span class="stat-label">Pipeline ready</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Enterprise-Grade Role Testing</h2>
      <p>Test Ansible roles the way they&rsquo;ll actually run in production environments.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Security</span>
        <h3>No ansible.cfg Commits</h3>
        <p>All configuration is driven by environment variables written to a session-scoped <code>.env</code> file. Complies with enterprise security policies that prohibit committed <code>ansible.cfg</code> files.</p>
      </article>
      <article class="card">
        <span class="badge">Testing</span>
        <h3>Molecule Test Scenarios</h3>
        <p>Three included scenarios: default, localhost-only, and with-linting. Python unit tests for supporting tooling. Extend or use as-is.</p>
      </article>
      <article class="card">
        <span class="badge">Isolation</span>
        <h3>Container-Based Execution</h3>
        <p>Fedora-based container with ephemeral SSH keys generated per run. The sandbox manages container lifecycle automatically, with no manual container management.</p>
      </article>
      <article class="card">
        <span class="badge">Security</span>
        <h3>Vault Inspection</h3>
        <p>Includes <code>DECRYPT_VAULTED_ITEMS.py</code> for safely inspecting encrypted Ansible vault variables during development without exposing secrets to version control.</p>
      </article>
      <article class="card">
        <span class="badge">CI/CD</span>
        <h3>Pipeline Ready</h3>
        <p>One-command activation: <code>python sandbox.py activate &amp;&amp; python sandbox.py run</code>. Drop it into any CI pipeline with Python and a container runtime.</p>
      </article>
      <article class="card">
        <span class="badge">Flexibility</span>
        <h3>Podman or Docker</h3>
        <p>Supports both Podman and Docker. Works in enterprise environments where Docker may not be available or permitted.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>The Problem It Solves</h2>
      <p>Enterprise Ansible development has constraints that generic sandboxes don&rsquo;t handle.</p>
    </div>
    <div class="grid">
      <article class="card">
        <h3>The Config Problem</h3>
        <p>Most Ansible sandbox examples involve committing <code>ansible.cfg</code> to the repo. Enterprise security policies often prohibit this. The Dev Sandbox uses environment variables exclusively.</p>
      </article>
      <article class="card">
        <h3>The Reproducibility Problem</h3>
        <p>Roles that pass tests on one developer&rsquo;s machine fail in CI. Container-based execution with ephemeral keys ensures every run starts from a known-good state.</p>
      </article>
      <article class="card">
        <h3>The Testing Gap</h3>
        <p>Molecule is the right tool for role testing, but setup is complex. The Dev Sandbox provides three working scenarios out of the box, ready to extend or use as-is.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Works Well With</h2>
      <p>Testing the roles that deploy these? That&rsquo;s exactly what this harness is for.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Reference Arch &bull; Preview</span>
        <h3>Project Armory</h3>
        <p>Armory provisions its entire platform with Ansible and OpenTofu. Test those roles here first in a container-isolated, ephemeral-key, CI-ready workflow.</p>
        <a class="btn btn-ghost" href="/software/project-armory/">Learn More &rarr;</a>
      </article>
      <article class="card">
        <span class="badge">GPLv3 &bull; Open Source</span>
        <h3>MAST</h3>
        <p>MAST integrates natively with Ansible and CI/CD. This is the harness for testing the roles that drive it before they touch a real appliance estate.</p>
        <a class="btn btn-ghost" href="/software/mast/">Learn More &rarr;</a>
      </article>
      <article class="card">
        <span class="badge">Private Alpha &bull; Commercial</span>
        <h3>SIEMatic</h3>
        <p>Deploying SIEMatic with Ansible? Validate the roles here before they touch production agents and indexers.</p>
        <a class="btn btn-ghost" href="/software/siematic/">Learn More &rarr;</a>
      </article>
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <div class="card">
      <h3>Open Source. Production-Hardened.</h3>
      <p>The Ansible Dev Sandbox is freely available on GitHub. Need help integrating it into your enterprise CI/CD pipeline or extending it for custom requirements? McIndi can help.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://github.com/McIndi/ans_dev_sandbox_playbook" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Ansible%20Dev%20Sandbox%20Inquiry">Talk to an Engineer</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
