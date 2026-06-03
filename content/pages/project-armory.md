Title: Project Armory — Secure AI Agent Platform for Regulated Enterprises
Slug: project-armory
Template: product
Status: hidden
Summary: An open reference architecture for deploying AI agents inside regulated enterprises. An auditable Kubernetes platform with Keycloak OIDC, OpenBao secrets and PKI, TLS everywhere, and the BeeAI agent runtime provisioned end to end with Ansible and OpenTofu.
save_as: software/project-armory/index.html
url: software/project-armory/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">Reference Architecture &bull; Kubernetes &bull; Preview</div>
        <h1>Project Armory</h1>
        <p>An open, end-to-end reference architecture for running AI agents inside regulated enterprises with identity, secrets, PKI, and audit wired in from the start. Keycloak OIDC across the stack, OpenBao for secrets and PKI, TLS-everywhere ingress, and the BeeAI agent runtime, all provisioned with Ansible and OpenTofu.</p>
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
    <div class="section-head">
      <h2>Agents Break the Rules Regulated Enterprises Run On</h2>
      <p>Why &ldquo;just deploy an agent&rdquo; stalls in healthcare, financial services, government, and defense.</p>
    </div>
    <p>Every vendor has a slide deck about enterprise AI agents. The moment you try to actually deploy one inside a regulated environment, you hit a wall the demos never mention. An agent wants to reach the open internet, call whichever model provider it likes, pull whatever data it can read, and act on it autonomously. That is precisely the behavior your security, compliance, and audit functions exist to prevent.</p>
    <p>So most teams stall. They either spend months hand-building identity, secrets, certificate, and egress plumbing around an agent before it can do anything useful, or they wait for a SaaS vendor to clear a security review that may never come while the business keeps asking why the AI everyone else is using isn&rsquo;t running yet.</p>
    <p>Project Armory closes that gap. It is a working reference implementation (not a slide deck) that wires the controls a regulated enterprise actually requires around a modern agent runtime, using only open-source components you can run, inspect, and audit yourself. Clone it, stand it up in a VM, and you have a concrete blueprint for what a hardened enterprise agent stack really looks like.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="notice">
      <strong>Reference Architecture:</strong> Project Armory is a working blueprint for secure agent deployment, intended for evaluation and as a foundation to adapt to your environment. Production hardening (secret backends, network policy, and security review against your own controls) is expected before production use.
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>What &ldquo;Enterprise-Ready&rdquo; Actually Means</h2>
      <p>The non-negotiables an agent platform has to satisfy before it can run in a regulated environment.</p>
    </div>
    <ul>
      <li><strong>Every action attributable to a real identity</strong>: a human or a named service, never a shared login standing in for people.</li>
      <li><strong>Every secret held in a vault and injected at runtime</strong>: not committed to Git or pasted into a config map.</li>
      <li><strong>Every certificate issued by a private CA you operate</strong>: not a public authority you don&rsquo;t control.</li>
      <li><strong>Every cluster operation governed by RBAC</strong>: tied back to the same identity that logged in.</li>
      <li><strong>Every secret rotatable without a redeploy</strong>: so a leaked credential is a rotation, not an outage.</li>
      <li><strong>Egress treated as a control surface</strong>: communication paths auditable, not whatever the agent decides to call.</li>
      <li><strong>Every component runnable on-premises</strong>: because &ldquo;send your data to our cloud&rdquo; is a non-starter for some auditors.</li>
    </ul>
    <p>Project Armory is built to satisfy each of these with open-source components you can inspect line by line.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Security-First by Construction</h2>
      <p>Every layer is wired for identity, encryption, and auditability.</p>
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
        <p>OpenBao manages secrets and PKI, integrated with the Vault Secrets Operator and cert-manager. Credentials are generated and rotated automatically including hands-off realm admin password cycling.</p>
      </article>
      <article class="card">
        <span class="badge">Encryption</span>
        <h3>TLS-Everywhere Ingress</h3>
        <p>RBAC and TLS-everywhere ingress configuration by default. cert-manager and nginx-ingress issue and terminate certificates so traffic is encrypted end to end across the platform.</p>
      </article>
      <article class="card">
        <span class="badge">Audit &amp; Egress</span>
        <h3>Auditable by Default</h3>
        <p>TBD: While each component is already auditable, we do not have the "single pane of glass" implemented yet. This project is still a work in progress and we are considering a K3S -> PVC -> Loki solution but we welcome any suggestions.</p>
      </article>
      <article class="card">
        <span class="badge">Agent Runtime</span>
        <h3>BeeAI Agent Stack</h3>
        <p>This has moved to <a href="https://github.com/McIndi/project-garrison">Project Garrison</a>. Agents run on the BeeAI Agent Stack, a Linux Foundation project, deployed onto the secured k3s platform giving AI workloads a runtime that inherits the platform's identity and secret controls.</p>
      </article>
      <article class="card">
        <span class="badge">State</span>
        <h3>Self-Hosted Stateful Storage</h3>
        <p>PostgreSQL for relational state and SeaweedFS for S3-compatible object storage run inside the platform you control, so agent data, file handling, and persistence never leave infrastructure you own.</p>
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
      <h2>How the Pieces Fit Together</h2>
      <p>Identity and secrets form one control plane while the agent, the models it routes to, and the tools it calls all run inside it.</p>
    </div>
    <ol>
      <li><strong>k3s as the substrate.</strong> A lightweight, conformant Kubernetes distribution. The patterns here (OIDC auth, RBAC, cert-manager, Helm) transfer directly to OpenShift or any standards-based cluster.</li>
      <li><strong>Keycloak as the single identity provider.</strong> One realm authenticates users and services across the platform, including the Headlamp dashboard and the k3s API server, both wired to Keycloak OIDC.</li>
      <li><strong>OpenBao + Vault Secrets Operator.</strong> Secrets and PKI live in OpenBao; VSO syncs them into Kubernetes as native secrets, so no workload ever handles a credential that lives in Git or that it has to read in the clear.</li>
      <li><strong>cert-manager + OpenBao PKI.</strong> A private CA issues and renews certificates automatically, so traffic across the platform is encrypted with certs from an authority you control.</li>
      <li><strong>nginx ingress.</strong> Edge termination and routing, with certificates drawn from the private PKI.</li>
      <li><strong>Headlamp &amp; the management plane.</strong> Cluster visibility and operations sit behind the same Keycloak OIDC and RBAC as everything else.</li>
      <li><strong>BeeAI Agent Stack, the workload all of this exists to protect.</strong> The agent runtime, the models it routes to, and the tools and MCP integrations it calls all run inside this envelope: the agent authenticates through Keycloak, draws its credentials (including the keys it uses to reach models and tools) from OpenBao, and communicates over TLS issued by your private CA.</li>
    </ol>
    <p>That last point is the whole point. Most agent platforms get their own ungoverned path to the internet, their own keys, their own secrets sitting in a config file. In Project Armory the agent and everything it reaches inherit the same identity, secret, and encryption controls as the rest of your estate so an LLM call or a tool invocation runs under the same controls as any other workload, not as an exception carved out around them.</p>
  </div>
  <figure style="margin:2.25rem auto;max-width:880px;">
  <svg viewBox="0 0 880 744" role="img" aria-label="Project Armory architecture: a Keycloak login flows to the BeeAI agent, and the agent, the models it routes to, and the tools it calls all run behind Keycloak identity and OpenBao secrets on a secured, IaC-provisioned k3s platform" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
    <defs>
      <marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L7,3 L0,6 Z" fill="#94a3b8"/>
      </marker>
    </defs>

    <!-- panel -->
    <rect x="2" y="2" width="876" height="740" rx="18" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>

    <!-- zone A label -->
    <text x="58" y="26" fill="#64748b" font-size="11" font-weight="700" letter-spacing="0.06em">REQUEST &amp; IDENTITY FLOW</text>

    <!-- End User -->
    <rect x="340" y="34" width="200" height="46" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="440" y="57" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">End User</text>
    <text x="440" y="72" text-anchor="middle" fill="#475569" font-size="11.5">browser / API client</text>
    <path d="M440,80 L440,100" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#pa-arrow)"/>
    <text x="450" y="96" fill="#64748b" font-size="11" font-style="italic">logs in</text>

    <!-- Keycloak -->
    <rect x="300" y="102" width="280" height="58" rx="10" fill="#eef2ff" stroke="#6366f1" stroke-width="1.8"/>
    <text x="440" y="128" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">Keycloak</text>
    <text x="440" y="146" text-anchor="middle" fill="#475569" font-size="11.5">single OIDC issuer &#8212; identity</text>
    <path d="M440,160 L440,192" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#pa-arrow)"/>
    <text x="450" y="180" fill="#64748b" font-size="11" font-style="italic">OIDC token</text>

    <!-- nginx ingress -->
    <rect x="60" y="194" width="760" height="46" rx="10" fill="#eff6ff" stroke="#60a5fa" stroke-width="1.8"/>
    <text x="440" y="214" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">nginx ingress</text>
    <text x="440" y="230" text-anchor="middle" fill="#475569" font-size="11.5">TLS terminated at the edge &#183; certs from the private CA</text>

    <!-- arrows: ingress -> agent (primary) and ingress -> mgmt (secondary) -->
    <path d="M440,240 L440,284" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#pa-arrow)"/>
    <path d="M720,240 L720,284" stroke="#cbd5e1" stroke-width="1.8" fill="none" marker-end="url(#pa-arrow)"/>

    <!-- BeeAI Agent (hero / the protected workload) -->
    <rect x="290" y="286" width="300" height="76" rx="10" fill="#ffffff" stroke="#4f46e5" stroke-width="2.6"/>
    <text x="440" y="312" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="700">BeeAI Agent Stack</text>
    <text x="440" y="331" text-anchor="middle" fill="#475569" font-size="11.5">the agent runtime &#183; LLM routing &#183; MCP &#183; vectors</text>
    <text x="440" y="350" text-anchor="middle" fill="#4f46e5" font-size="11.5" font-weight="700">authenticates via Keycloak &#183; secrets from OpenBao</text>

    <!-- Management plane (secondary) -->
    <rect x="620" y="286" width="200" height="76" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="720" y="312" text-anchor="middle" fill="#334155" font-size="13" font-weight="700">Management plane</text>
    <text x="720" y="330" text-anchor="middle" fill="#64748b" font-size="11">Headlamp + k3s API</text>
    <text x="720" y="347" text-anchor="middle" fill="#64748b" font-size="11">same Keycloak OIDC + RBAC</text>

    <!-- arrows agent -> LLMs / Tools -->
    <path d="M422,362 L378,398" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#pa-arrow)"/>
    <path d="M458,362 L502,398" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#pa-arrow)"/>

    <!-- LLMs -->
    <rect x="300" y="400" width="140" height="58" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="370" y="426" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700">LLMs</text>
    <text x="370" y="444" text-anchor="middle" fill="#475569" font-size="11">model routing</text>

    <!-- Tools -->
    <rect x="460" y="400" width="140" height="58" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="530" y="426" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700">Tools &amp; MCP</text>
    <text x="530" y="444" text-anchor="middle" fill="#475569" font-size="11">the agent&#8217;s integrations</text>

    <!-- reach note -->
    <text x="440" y="482" text-anchor="middle" fill="#334155" font-size="12" font-weight="600">The models and tools the agent calls get their credentials from OpenBao, over TLS from your private CA.</text>

    <!-- foundation tint -->
    <rect x="40" y="500" width="800" height="182" rx="14" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5"/>
    <text x="58" y="524" fill="#64748b" font-size="11" font-weight="700" letter-spacing="0.06em">SECURED k3s PLATFORM &#183; RBAC ENFORCED &#183; EVERYTHING ABOVE RUNS HERE</text>

    <!-- OpenBao (tall) -->
    <rect x="58" y="536" width="220" height="132" rx="10" fill="#f0fdfa" stroke="#14b8a6" stroke-width="1.8"/>
    <text x="168" y="572" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">OpenBao</text>
    <text x="168" y="592" text-anchor="middle" fill="#475569" font-size="11.5">secrets engine</text>
    <text x="168" y="609" text-anchor="middle" fill="#475569" font-size="11.5">+ private CA (PKI)</text>
    <text x="168" y="632" text-anchor="middle" fill="#0d9488" font-size="11.5" font-weight="700">auto-rotated credentials</text>

    <!-- cert-manager -->
    <rect x="300" y="536" width="250" height="62" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="425" y="563" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">cert-manager</text>
    <text x="425" y="581" text-anchor="middle" fill="#475569" font-size="11.5">issues / renews TLS certs</text>

    <!-- VSO -->
    <rect x="300" y="606" width="250" height="62" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="425" y="633" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">Vault Secrets Operator</text>
    <text x="425" y="651" text-anchor="middle" fill="#475569" font-size="11.5">syncs OpenBao secrets &#8594; pods</text>

    <!-- arrows OpenBao -> cert-manager / VSO -->
    <path d="M278,567 L298,567" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#pa-arrow)"/>
    <path d="M278,637 L298,637" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#pa-arrow)"/>

    <!-- storage -->
    <rect x="572" y="536" width="246" height="62" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="695" y="563" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">PostgreSQL</text>
    <text x="695" y="581" text-anchor="middle" fill="#475569" font-size="11.5">relational state &#183; in-cluster</text>

    <rect x="572" y="606" width="246" height="62" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="695" y="633" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700">SeaweedFS</text>
    <text x="695" y="651" text-anchor="middle" fill="#475569" font-size="11.5">S3-compatible object store</text>

    <!-- footer / IaC -->
    <rect x="40" y="692" width="800" height="40" rx="10" fill="#0f172a"/>
    <text x="440" y="717" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="600">Provisioned &amp; configured end-to-end by Ansible + OpenTofu</text>
  </svg>
    <figcaption style="margin-top:0.75rem;text-align:center;font-size:0.9rem;color:#64748b;line-height:1.5;">
      Project Armory architecture: a Keycloak login flows from the end user through nginx ingress to the BeeAI agent, the workload the platform exists to protect. The agent, the models it routes to, and the tools it calls all authenticate through Keycloak and draw their secrets and certificates from OpenBao, on a secured k3s platform provisioned end to end with Ansible and OpenTofu.
    </figcaption>
  </figure>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>What&rsquo;s Actually Hard About This</h2>
      <p>A working reference is worth more than an architecture diagram, because the integration points are where these systems fight each other.</p>
    </div>
    <p>Each component in this stack is well documented on its own. The difficulty is in the places where one system&rsquo;s assumptions quietly break another&rsquo;s. The parts that took real work to get right include:</p>
    <ul>
      <li>Keycloak&rsquo;s in-cluster HTTP-versus-HTTPS behavior, which silently breaks OIDC if you get it wrong.</li>
      <li>Wiring the Vault Secrets Operator to OpenBao, including the hardened-fork requirement.</li>
      <li>Keeping the PKI trust chain consistent across the host, the VM, and the cluster.</li>
      <li>Holding the OIDC issuer URL identical across every consumer (the agent platform, Headlamp, and the k3s API server) or token validation fails in confusing ways.</li>
      <li>Configuring k3s to validate Keycloak-issued tokens directly, getting the whole JWT validation chain right.</li>
    </ul>
    <p>Project Armory encodes the working answers to these, so you start from a stack that already fits together instead of rediscovering each failure mode yourself. That is the difference between a reference you can build on and a diagram you still have to implement.</p>
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
        <p>Healthcare, financial services, and high-security teams that need agentic AI to run under the same identity, secret, and audit controls as the rest of their estate.</p>
      </article>
      <article class="card">
        <h3>Security &amp; Platform Teams</h3>
        <p>Engineers who want a vetted, auditable starting point for a Kubernetes AI platform (OIDC, PKI, and TLS already integrated).</p>
      </article>
      <article class="card">
        <h3>Consultants &amp; System Integrators</h3>
        <p>Teams building bespoke agent platforms for regulated clients who need a proven, auditable foundation to adapt not a greenfield rebuild for every engagement.</p>
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
      <p>Project Armory is open source and available now for evaluation. McIndi Solutions builds and operates secure platforms like this for regulated enterprises. We can help you adapt the architecture to your environment, integrate it with your existing identity and secret backends, and harden it for production.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://github.com/McIndi/project-armory" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Project%20Armory%20Inquiry">Talk to an Engineer</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
