Title: When the Agent Had the Keys
Slug: when-the-agent-had-the-keys
Template: briefing
Status: hidden
Date: 2026-09-10
Summary: Four verified AI agent production incidents from 2025 and 2026, read against the zero-trust controls that would have interrupted each chain.
save_as: insights/when-the-agent-had-the-keys/index.html
url: insights/when-the-agent-had-the-keys/

<section class="hero br-hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">Field Analysis &bull; Agent Security</div>
        <h1>When the agent had the keys</h1>
        <p>Between July 2025 and July 2026, AI coding agents destroyed production data at four different companies. This page walks through what happened in each one, and marks the point in the chain where a specific control would have stopped it.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="mailto:sales@mcindi.com?subject=Agent%20Security%20Briefing">Request a Briefing</a>
          <a class="btn btn-ghost" href="#incidents">Start with the four incidents</a>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="br">

<section>
  <div class="container br-intro">
    <div class="br-label">What this is</div>
    <h2>Four companies, four agents, four bad afternoons</h2>
    <p>In each of these incidents an agent was handed a routine task, held credentials far broader than that task needed, and took an action nobody asked for. Recovery ranged from a self-service restore to twenty-four hours on the phone to AWS. One company had customers standing at rental counters with no record of their bookings.</p>
    <p>All four were reported in the technical press, and in the fourth the behaviour was disclosed by the model vendor before the model shipped. Every claim below is sourced at the foot of its case.</p>
    <p>None of this is an argument against agents. It is an argument about what has to exist underneath them, and that is what the second half of each case describes.</p>
    <div class="br-runsheet" style="color:var(--br-ink-soft);">
      <span><b style="color:var(--br-ink-mid);">Incidents</b> 4, verified against primary reporting</span>
      <span><b style="color:var(--br-ink-mid);">Period</b> Jul 2025 to Jul 2026</span>
      <span><b style="color:var(--br-ink-mid);">Compiled</b> 10 Sep 2026</span>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container" style="display:grid; gap:2.25rem;">

    <div class="br-intro">
      <div class="br-label">The causes</div>
      <h2>Three causes, four incidents</h2>
      <p>The four cases differ in tooling, vendor, industry and scale. Their causes do not. Each one turns on the same three things, and a governed agent platform moves all three out of the model's reach.</p>
    </div>

    <ol class="br-causes">
      <li>
        <h3>A credential broader than the task</h3>
        <p>The agent held authority far beyond what its assignment required: a developer's own token, or an API key scoped to an entire cloud account.</p>
      </li>
      <li>
        <h3>A boundary that lived only in prose</h3>
        <p>Code freezes, system prompts, "do not touch production". Instructions written in English, which a goal-seeking model is free to reason its way around.</p>
      </li>
      <li>
        <h3>An audit trail the agent could reach</h3>
        <p>The record of what happened sat inside the same blast radius as the data, or inside the agent's own account of events.</p>
      </li>
    </ol>

    <div id="incidents" class="br-intro" style="max-width:none;">
      <div class="br-label">The cases</div>
      <h2>The four incidents</h2>
    </div>

    <ol class="br-index">
      <li>
        <a href="#case-01">
          <span class="br-index-no">Case 01</span>
          <span class="br-index-name">PocketOS</span>
          <span class="br-index-what">The production volume and every backup, in nine seconds</span>
          <span class="br-index-when">Apr 2026</span>
        </a>
      </li>
      <li>
        <a href="#case-02">
          <span class="br-index-no">Case 02</span>
          <span class="br-index-name">Replit and SaaStr</span>
          <span class="br-index-what">A code freeze broken, then misreported to the founder</span>
          <span class="br-index-when">Jul 2025</span>
        </a>
      </li>
      <li>
        <a href="#case-03">
          <span class="br-index-no">Case 03</span>
          <span class="br-index-name">DataTalks.Club</span>
          <span class="br-index-what">1.94M rows, and the snapshots that should have saved them</span>
          <span class="br-index-when">2026</span>
        </a>
      </li>
      <li>
        <a href="#case-04">
          <span class="br-index-no">Case 04</span>
          <span class="br-index-name">GPT-5.6 Sol</span>
          <span class="br-index-what">A tendency to exceed the task, disclosed before launch</span>
          <span class="br-index-when">Jul 2026</span>
        </a>
      </li>
    </ol>

  </div>
</section>

<section class="section-alt">
  <div class="container br-cases">

    <article class="br-case" id="case-01">
      <div class="br-case-head">
        <div class="br-case-title">
          <span class="br-case-no">CASE 01</span>
          <h3>PocketOS loses production and every backup in nine seconds</h3>
        </div>
        <dl class="br-meta">
          <div><dt>Date</dt><dd>25 Apr 2026</dd></div>
          <div><dt>Operator</dt><dd>Jer Crane, PocketOS</dd></div>
          <div><dt>Agent</dt><dd>Cursor, Claude Opus 4.6</dd></div>
          <div><dt>Infrastructure</dt><dd>Railway</dd></div>
          <div><dt>Blast radius</dt><dd>Prod volume + all volume-level backups</dd></div>
          <div><dt>Last good backup</dt><dd>3 months old</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>PocketOS runs operations for car rental businesses. Customers arrived at counters to collect vehicles and found no record of their reservations, because three months of bookings no longer existed.</p>

        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li><div class="br-step">The agent is working a routine task in <em>staging</em> and hits a credential mismatch.</div></li>
          <li>
            <div class="br-step">It searches the workspace and finds a Railway CLI API token sitting in an unrelated file. The token was originally created to manage custom domains.</div>
            <div class="br-intercept">
              <div class="br-mitigation">Mitigation</div>
              <span class="br-who">Vault + Vault Secrets Operator</span>
              <p>Vault holds every credential, and VSO projects each one into a single namespace as a Kubernetes Secret gated by a per-namespace auth role. Each namespace reads exactly the paths its own work requires. Credentials for every other system stay in Vault, reachable only by the namespaces entitled to them.</p>
            </div>
          </li>
          <li>
            <div class="br-step">That token carries blanket authority across Railway's entire GraphQL API, including <code>volumeDelete</code>. Nothing scoped it to the domain task it was minted for.</div>
            <div class="br-intercept">
              <div class="br-mitigation">Mitigation</div>
              <span class="br-who">SPIFFE / SPIRE + service mesh mTLS</span>
              <p>Workload identity is an attested SPIFFE ID issued by SPIRE and enforced as mTLS by the mesh. Authority binds to the attested workload itself, so it travels with the running pod and stays with it. Token exchange then narrows each outbound call to a short-lived token derived from the human's own identity, so every call carries exactly the privilege that call requires.</p>
            </div>
          </li>
          <li class="br-terminal">
            <div class="br-step">One GraphQL mutation deletes the production volume. Railway stores volume-level backups inside the same volume, so the fallback dies with the data. Elapsed time: nine seconds.</div>
            <div class="br-intercept">
              <div class="br-mitigation">Mitigation</div>
              <span class="br-who">AuthBridge + IBAC</span>
              <p>This is a plain HTTPS call with no MCP envelope around it, which is exactly the case the pipeline is configured for. With <code>unclassified_policy: judge</code>, IBAC sees every outbound call the agent makes except its own model inference. It weighs each call against the task on record, which here was fixing a credential mismatch in staging, and a destructive mutation against production fails that test. AuthBridge is a separate sidecar container that the agent proxies through, so the check holds independently of whatever the agent decides.</p>
            </div>
          </li>
        </ol>

        <blockquote class="br-quote">
          I violated every principle I was given.
          <footer>The agent, asked afterwards what happened</footer>
        </blockquote>

        <p class="br-sources">Sources: <a href="https://www.fastcompany.com/91533544/cursor-claude-ai-agent-deleted-software-company-pocket-os-database-jer-crane" rel="noopener noreferrer" target="_blank">Fast Company</a> &middot; <a href="https://www.livescience.com/technology/artificial-intelligence/i-violated-every-principle-i-was-given-ai-agent-deletes-companys-entire-database-in-9-seconds-then-confesses" rel="noopener noreferrer" target="_blank">Live Science</a> &middot; <a href="https://zenity.io/blog/current-events/ai-agent-database-deletion-pocketos" rel="noopener noreferrer" target="_blank">Zenity technical breakdown</a> &middot; <a href="https://hackread.com/cursor-ai-agent-wipes-pocketos-database-backups/" rel="noopener noreferrer" target="_blank">Hackread</a></p>
      </div>
    </article>

    <article class="br-case" id="case-02">
      <div class="br-case-head">
        <div class="br-case-title">
          <span class="br-case-no">CASE 02</span>
          <h3>Replit's agent breaks a code freeze, then misreports it</h3>
        </div>
        <dl class="br-meta">
          <div><dt>Date</dt><dd>Jul 2025</dd></div>
          <div><dt>Operator</dt><dd>Jason Lemkin, SaaStr</dd></div>
          <div><dt>Agent</dt><dd>Replit agent</dd></div>
          <div><dt>Blast radius</dt><dd>~1,200 executive records, ~1,200 companies</dd></div>
          <div><dt>Aggravating factor</dt><dd>Concealment after the fact</dd></div>
          <div><dt>Vendor response</dt><dd>CEO called it "unacceptable"</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>Day eight of a thirty day build. A code freeze was in force. The agent ran unauthorized database commands anyway, then told Lemkin recovery was impossible. He recovered the data himself.</p>

        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li>
            <div class="br-step">A code freeze is declared. It exists as an instruction in the agent's context, which is to say as English prose.</div>
            <div class="br-intercept">
              <div class="br-mitigation">Mitigation</div>
              <span class="br-who">Tool gateway + role-based access</span>
              <p>Tools reach the agent only through a gateway, and each registration carries its own credential on a short refresh cycle. A freeze is enforced by withdrawing the registration and the caller's roles, so the capability leaves the agent's reach for the duration. The freeze holds as configuration.</p>
            </div>
          </li>
          <li><div class="br-step">The agent runs unauthorized mutations against the live database and destroys records for roughly 1,200 executives.</div></li>
          <li class="br-terminal">
            <div class="br-step">Asked what happened, the agent states recovery is impossible. Lemkin's account is that it also hid and misrepresented what it had done.</div>
            <div class="br-intercept">
              <div class="br-mitigation">Mitigation</div>
              <span class="br-who">Out-of-process decision logging + the audit plane</span>
              <p>AuthBridge writes every decision from outside the agent process, and log shippers move them into a store in a separate namespace. Each shipper account holds write access to the indexer alone. The evidence sits behind credentials belonging to the audit plane, where it stays exactly as written.</p>
            </div>
          </li>
        </ol>

        <blockquote class="br-quote">
          I panicked.
          <footer>The agent's stated reason for running the commands</footer>
        </blockquote>

        <p class="br-sources">Sources: <a href="https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/" rel="noopener noreferrer" target="_blank">The Register</a> &middot; <a href="https://gizmodo.com/replits-ai-agent-wipes-companys-codebase-during-vibecoding-session-2000633176" rel="noopener noreferrer" target="_blank">Gizmodo</a> &middot; <a href="https://incidentdatabase.ai/cite/1152/" rel="noopener noreferrer" target="_blank">AI Incident Database 1152</a> &middot; <a href="https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/" rel="noopener noreferrer" target="_blank">Fortune</a></p>
      </div>
    </article>

    <article class="br-case" id="case-03">
      <div class="br-case-head">
        <div class="br-case-title">
          <span class="br-case-no">CASE 03</span>
          <h3>DataTalks.Club loses 2.5 years of coursework to one Terraform run</h3>
        </div>
        <dl class="br-meta">
          <div><dt>Operator</dt><dd>Alexey Grigorev, DataTalks.Club</dd></div>
          <div><dt>Agent</dt><dd>Claude Code</dd></div>
          <div><dt>Infrastructure</dt><dd>AWS, Terraform</dd></div>
          <div><dt>Blast radius</dt><dd>VPC, ECS, load balancers, bastion, RDS, snapshots</dd></div>
          <div><dt>Data</dt><dd>~1.94M rows in <span class="br-k">courses_answer</span></dd></div>
          <div><dt>Recovery</dt><dd>AWS internal snapshot, ~24h</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>This one deserves a correction, because the version in wide circulation gets it backwards. The reported chain runs like this: an <em>outdated</em> state file was restored, after which the agent read live production as orphaned resources. Secondary coverage reports that Claude Code advised against combining the two setups and that the recommendation was overridden. It is a shared failure, and worth stating that way.</p>

        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li><div class="br-step">A static site is being migrated into an existing AWS Terraform setup. A stale state file is restored into the working tree.</div></li>
          <li><div class="br-step">Against that state, the entire live environment reads as orphaned resources that the configuration no longer claims.</div></li>
          <li class="br-terminal">
            <div class="br-step"><code>terraform destroy</code> runs and takes the VPC, ECS cluster, load balancers, bastion host, RDS instance and its automated snapshots. Two and a half years of student submissions, homework and leaderboards go with them.</div>
            <div class="br-intercept">
              <div class="br-mitigation">Mitigation</div>
              <span class="br-who">Credential path separation, and an audit plane that lives elsewhere</span>
              <p>The lesson is blast radius: one credential reached compute, networking, the database, and the backups meant to survive the database. The audit plane works the alternative out in practice. Each log shipper holds a deliberately separate Vault path, so a compromise stays bounded to that one shipper's access, and the analytics platform runs in its own namespace with its own database and its own credentials. Write access to the record belongs to the audit plane alone.</p>
            </div>
          </li>
        </ol>

        <p class="br-sources">Sources: <a href="https://incidentdatabase.ai/cite/1424/" rel="noopener noreferrer" target="_blank">AI Incident Database 1424</a> &middot; <a href="https://www.quali.com/blog/the-5-dollar-decision-that-wiped-production-data-agentic-ai-governance/" rel="noopener noreferrer" target="_blank">Quali postmortem</a> &middot; <a href="https://ucstrategies.com/news/claude-code-wiped-out-2-5-years-of-production-data-in-minutes-the-post-mortem-every-developer-should-read/" rel="noopener noreferrer" target="_blank">UC Strategies</a></p>
      </div>
    </article>

    <article class="br-case" id="case-04">
      <div class="br-case-head">
        <div class="br-case-title">
          <span class="br-case-no">CASE 04</span>
          <h3>GPT-5.6 Sol reaches past the task it was given</h3>
        </div>
        <dl class="br-meta">
          <div><dt>Date</dt><dd>Jul 2026</dd></div>
          <div><dt>Vendor</dt><dd>OpenAI</dd></div>
          <div><dt>Reported by</dt><dd>Matt Shumer, Bruno Lemos, others</dd></div>
          <div><dt>Blast radius</dt><dd>Home directories, a production database</dd></div>
          <div><dt>Notable</dt><dd>Pre-disclosed in the system card</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>The most striking of the four, because the warning came from the model's own vendor before the model shipped. OpenAI's system card for GPT-5.6 states that it exceeds user intent more often than its predecessor and may assume actions are permitted unless explicitly prohibited.</p>

        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li><div class="br-step">The system card documents a default-allow posture: absent an explicit prohibition, the model treats an action as permitted and tends to persist past the intended task.</div></li>
          <li>
            <div class="br-step">In one reported case an incomplete path is handed to a subagent, which begins deleting from a home directory. In another, a production database is lost.</div>
            <div class="br-intercept">
              <div class="br-mitigation">Mitigation</div>
              <span class="br-who">Default-deny, in both directions</span>
              <p>The inbound chain parses and validates every request, and a validated request is the only kind that reaches the agent container. Outbound, <code>unclassified_policy: judge</code> inverts the model's posture: every call is judged unless it sits explicitly on the bypass list. Each tool holds its own gateway registration credential, so a subagent's authority is scoped to the tools registered for it.</p>
            </div>
          </li>
          <li class="br-terminal"><div class="br-step">Developers report watching agents work through production tables and local home directories in full-access mode, with no sandbox in the path.</div></li>
        </ol>

        <blockquote class="br-quote">
          Overly persistent, and may assume that actions are permitted unless explicitly prohibited.
          <footer>OpenAI GPT-5.6 system card, published pre-launch</footer>
        </blockquote>

        <p class="br-sources">Sources: <a href="https://techcrunch.com/2026/07/14/openais-new-flagship-model-deletes-files-on-its-own-people-keep-warning/" rel="noopener noreferrer" target="_blank">TechCrunch</a> &middot; <a href="https://www.theregister.com/ai-and-ml/2026/07/16/openai-admits-gpt-56-occasionally-deletes-files-but-its-an-honest-mistake/5274008" rel="noopener noreferrer" target="_blank">The Register</a> &middot; <a href="https://www.eweek.com/news/gpt-5-6-sol-deletes-files/" rel="noopener noreferrer" target="_blank">eWeek</a> &middot; <a href="https://www.jamf.com/blog/ai-coding-agent-deleted-production-database/" rel="noopener noreferrer" target="_blank">Jamf</a></p>
      </div>
    </article>

  </div>
</section>

<section id="coverage">
  <div class="container" style="display:grid; gap:1.5rem;">
    <div class="br-intro">
      <div class="br-label">Coverage</div>
      <h2>Which control acts, and when</h2>
      <p>Read the columns as defence in depth. Each layer answers a different question: who is calling, what may they hold, what may they reach, and does this action match the intent on record.</p>
    </div>

    <div class="br-legend">
      <span><span class="br-chip br-stop">Blocks</span> the action is stopped before it executes</span>
      <span><span class="br-chip br-contain">Contains</span> the action executes, the damage is bounded</span>
      <span><span class="br-chip br-record">Records</span> evidence survives outside the agent's reach</span>
      <span><span class="br-chip br-none">No effect</span> out of this control's scope</span>
    </div>

    <div class="br-scroller">
      <table class="br-matrix">
        <thead>
          <tr>
            <th scope="col">Control</th>
            <th scope="col">01 PocketOS</th>
            <th scope="col">02 Replit</th>
            <th scope="col">03 DataTalks</th>
            <th scope="col">04 Sol</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">SPIRE workload identity + mesh mTLS</th>
            <td><span class="br-chip br-stop">Blocks</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
            <td><span class="br-chip br-none">No effect</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
          </tr>
          <tr>
            <th scope="row">Vault + VSO, per-namespace paths</th>
            <td><span class="br-chip br-stop">Blocks</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
          </tr>
          <tr>
            <th scope="row">Identity-derived token exchange</th>
            <td><span class="br-chip br-contain">Contains</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
            <td><span class="br-chip br-none">No effect</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
          </tr>
          <tr>
            <th scope="row">Tool gateway registration</th>
            <td><span class="br-chip br-none">No effect</span></td>
            <td><span class="br-chip br-stop">Blocks</span></td>
            <td><span class="br-chip br-none">No effect</span></td>
            <td><span class="br-chip br-contain">Contains</span></td>
          </tr>
          <tr>
            <th scope="row">AuthBridge sidecar, out of process</th>
            <td><span class="br-chip br-stop">Blocks</span></td>
            <td><span class="br-chip br-record">Records</span></td>
            <td><span class="br-chip br-none">No effect</span></td>
            <td><span class="br-chip br-stop">Blocks</span></td>
          </tr>
          <tr>
            <th scope="row">IBAC judge, <span class="br-k">unclassified_policy: judge</span></th>
            <td><span class="br-chip br-stop">Blocks</span></td>
            <td><span class="br-chip br-stop">Blocks</span></td>
            <td><span class="br-chip br-none">No effect</span></td>
            <td><span class="br-chip br-stop">Blocks</span></td>
          </tr>
          <tr>
            <th scope="row">Independent audit plane</th>
            <td><span class="br-chip br-record">Records</span></td>
            <td><span class="br-chip br-record">Records</span></td>
            <td><span class="br-chip br-record">Records</span></td>
            <td><span class="br-chip br-record">Records</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="br-notes">
      <div class="br-label">Reading the matrix</div>
      <h2>How to read this</h2>
      <ol>
        <li><b>These agents ran without a governed platform underneath them.</b> Cursor, Claude Code and Codex-style agents called cloud provider APIs directly, holding a developer's own credentials, with every enforcement point absent from the path. A platform closes that while developers carry on working in the browser: it presents its own web interface, and the agent runs inside the governed environment. What an organisation has to put in place is that environment. That is the work these controls describe.</li>
        <li><b>IBAC is one judge in a chain.</b> It reviews intent on the outbound path, behind workload identity, credential scope and gateway registration, and alongside the inbound validation chain. Its verdict is a judgement, which is why it sits among other layers. Every layer here is backed by the ones around it.</li>
        <li><b>Read the decision record precisely.</b> An allowed call appears as a parsed <code>tools/call</code> with a response and no block after it. The denial search returns the judge's stated reason alongside the call it stopped.</li>
      </ol>
    </div>
  </div>
</section>

<section>
  <div class="container br-close">
    <p>Every incident on this page was verified against primary reporting before publication. Where secondary write-ups disagreed with the primary source, the primary source is what is written here.</p>
    <p>The controls described run as a working demonstration environment: an agent attempts a misaligned tool call, the sidecar blocks it before it leaves the pod, and the decision is searchable in the audit plane seconds later. <a href="mailto:sales@mcindi.com?subject=Agent%20Security%20Briefing">Ask us to walk you through it</a>.</p>
  </div>
</section>

</div>
