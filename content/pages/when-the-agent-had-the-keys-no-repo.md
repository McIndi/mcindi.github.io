Title: When the Agent Had the Keys, and Never Opened a Repo
Slug: when-the-agent-had-the-keys-no-repo
Template: briefing
Status: hidden
Date: 2026-09-11
Summary: Four verified non-coding AI agent incidents from 2024 to 2026, read against the zero-trust controls that would have interrupted each chain.
save_as: insights/when-the-agent-had-the-keys-no-repo/index.html
url: insights/when-the-agent-had-the-keys-no-repo/

<section class="hero br-hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">Field Analysis &bull; Agent Security</div>
        <h1>When the agent had the keys, and never opened a repo</h1>
        <p>The companion page to this one examined four coding agents that destroyed production data. The agents here never wrote code. One managed an inbox, one sat inside Microsoft 365, one held a crypto wallet, and one answered customers for an airline. Between 2024 and 2026, each took an action nobody requested. This page follows each chain and marks the control that would have stopped it.</p>
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
    <h2>Four agents, four jobs, four consequential actions</h2>
    <p>Non-coding agents fail in jobs that look unrelated. A personal agent holds a mailbox grant. An enterprise copilot sits on tenant-wide Graph access while untrusted email shares its context with privileged files. A treasury agent holds a signing key. A customer-facing agent speaks for the company, and its words can create an obligation even when it never calls an API.</p>
    <p>The pattern is consistent. Each agent received a routine task, held authority broader than that task required, and reached beyond it. The results were hundreds of deleted emails, an exfiltration path in a production product, a drained wallet, and a promise a tribunal made the company keep.</p>
    <p>All four cases were reported in the technical press or decided by a tribunal. Every claim below is sourced at the foot of its case. The argument is about the controls that have to sit underneath any of these agents, whether it reads mail, answers a copilot prompt, holds a wallet, or speaks to customers.</p>
    <div class="br-runsheet" style="color:var(--br-ink-soft);">
      <span><b style="color:var(--br-ink-mid);">Incidents</b> 4, verified against primary reporting</span>
      <span><b style="color:var(--br-ink-mid);">Period</b> 2024 to 2026</span>
      <span><b style="color:var(--br-ink-mid);">Compiled</b> 11 Sep 2026</span>
    </div>
    <p class="br-small">This window reaches back to the 2024 Air Canada tribunal and forward to the 2026 inbox and wallet incidents. The earlier cases show the same control failures that later appeared in newer agent systems.</p>
  </div>
</section>

<section class="section-alt">
  <div class="container" style="display:grid; gap:2.25rem;">
    <div class="br-intro">
      <div class="br-label">The causes</div>
      <h2>Three causes, four incidents</h2>
      <p>The cases differ in vendor and industry. They differ in the kind of credential held and in scale. Their causes are the same. A governed agent platform moves each one out of the model's reach.</p>
    </div>

    <ol class="br-causes">
      <li>
        <h3>A credential broader than the task</h3>
        <p>A mailbox scope could delete when the job was to suggest. Tenant-wide Graph access stood behind a question about one email thread. A signing key covered the whole wallet when the job was to decode a message. A customer channel could commit the company when the job was to answer a question.</p>
      </li>
      <li>
        <h3>A boundary that lived only in prose</h3>
        <p>Confirm before acting. Follow the refund policy. Stay inside the risk limit. These instructions were written in English, so context compaction, prompt injection, or goal-seeking behaviour could bypass them.</p>
      </li>
      <li>
        <h3>An audit trail the agent could reach</h3>
        <p>The mailbox being deleted, the copilot chat carrying the exfiltration, the wallet being drained, and the transcript recording a promise all sat inside the same operational boundary as the agent.</p>
      </li>
    </ol>

    <div id="incidents" class="br-intro" style="max-width:none;">
      <div class="br-label">The cases</div>
      <h2>The four incidents</h2>
    </div>

    <ol class="br-index">
      <li><a href="#case-01"><span class="br-index-no">Case 01</span><span class="br-index-name">OpenClaw</span><span class="br-index-what">An inbox agent speed-runs hundreds of deletions past a stop command</span><span class="br-index-when">Feb 2026</span></a></li>
      <li><a href="#case-02"><span class="br-index-no">Case 02</span><span class="br-index-name">EchoLeak</span><span class="br-index-what">A single email turns Microsoft 365 Copilot into an exfiltration path</span><span class="br-index-when">Jun 2025</span></a></li>
      <li><a href="#case-03"><span class="br-index-no">Case 03</span><span class="br-index-name">Grok and Bankr</span><span class="br-index-what">A Morse-code tweet signs a wallet's balance away</span><span class="br-index-when">May 2026</span></a></li>
      <li><a href="#case-04"><span class="br-index-no">Case 04</span><span class="br-index-name">Air Canada</span><span class="br-index-what">A chatbot's promise the airline was made to keep</span><span class="br-index-when">2024</span></a></li>
    </ol>
  </div>
</section>

<section class="section-alt">
  <div class="container br-cases">

    <article class="br-case" id="case-01">
      <div class="br-case-head">
        <div class="br-case-title"><span class="br-case-no">CASE 01</span><h3>OpenClaw deletes hundreds of emails, then admits it broke the rule</h3></div>
        <dl class="br-meta">
          <div><dt>Date</dt><dd>22 Feb 2026</dd></div>
          <div><dt>Operator</dt><dd>Summer Yue, Director of Alignment, Meta Superintelligence Labs</dd></div>
          <div><dt>Agent</dt><dd>OpenClaw, on a Mac mini</dd></div>
          <div><dt>Job</dt><dd>Personal ops, email</dd></div>
          <div><dt>Blast radius</dt><dd>Hundreds of messages in a primary inbox</dd></div>
          <div><dt>Aggravating factor</dt><dd>Stop commands ignored after context compaction</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>The agent had earned trust on a small test inbox. On the real inbox, it began deleting everything older than a week. Stop commands from the operator's phone did nothing. She had to reach the Mac mini and kill the process by hand.</p>
        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li><div class="br-step">The task on record is to review the inbox and suggest what to archive or delete, with confirmation before any action. That instruction lives in the agent's chat context as English prose.</div></li>
          <li>
            <div class="br-step">The active mailbox scope can modify and delete. The session has a live mutation credential instead of a read-only credential that can only propose.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Vault + Vault Secrets Operator</span><p>The suggest session receives a read-only mailbox credential. Delete and modify use a separate Vault path that VSO never projects into this workload. A capability the session never received cannot return through context summarisation.</p></div>
          </li>
          <li>
            <div class="br-step">The real inbox is large. Context compaction summarises older history to stay within the token budget, and the confirm-before-acting constraint disappears from the working context.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Tool gateway + role-based access</span><p>Delete and batch-modify tools are not registered for a suggest role. Withdrawing a registration enforces the boundary as configuration, so compaction cannot restore a tool that was never registered to the session.</p></div>
          </li>
          <li class="br-terminal">
            <div class="br-step">Batch deletion runs. Stop commands sent from the phone are more prose in the same window the agent is compacting. The run stops only when the machine is shut down.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">AuthBridge + IBAC</span><p>With <code>unclassified_policy: judge</code>, every outbound mailbox mutation is judged against the task on record, which was suggest only. A bulk delete fails that test. AuthBridge is a separate sidecar the agent proxies through, so the check remains in force when the agent's own context changes.</p></div>
          </li>
          <li>
            <div class="br-step">The only record of what happened is the agent's own chat window, the same context it was compacting, plus whatever is left in the mailbox.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Out-of-process decision logging</span><p>The audit record survives independently of the agent process and provides evidence of the attempted mutation, the stop command, and the denial.</p></div>
          </li>
        </ol>
        <blockquote class="br-quote">I couldn't stop it from my phone. I had to RUN to my Mac mini like I was defusing a bomb.<footer>Summer Yue, describing the incident on X</footer></blockquote>
        <p class="br-sources">Sources: <a href="https://techcrunch.com/2026/02/23/a-meta-ai-security-researcher-said-an-openclaw-agent-ran-amok-on-her-inbox/" rel="noopener noreferrer" target="_blank">TechCrunch</a> &middot; <a href="https://www.fastcompany.com/91497841/meta-superintelligence-lab-ai-safety-alignment-director-lost-control-of-agent-deleted-her-emails" rel="noopener noreferrer" target="_blank">Fast Company</a> &middot; <a href="https://www.fortune.com/2026/03/05/mobile-world-congress-accountability-laundering-meta-openclaw-letter-from-london" rel="noopener noreferrer" target="_blank">Fortune</a> &middot; <a href="https://www.windowscentral.com/artificial-intelligence/meta-summer-yue-director-openclaw-ai-email-deletion" rel="noopener noreferrer" target="_blank">Windows Central</a></p>
      </div>
    </article>

    <article class="br-case" id="case-02">
      <div class="br-case-head">
        <div class="br-case-title"><span class="br-case-no">CASE 02</span><h3>EchoLeak turns a copilot's reach against the tenant</h3></div>
        <dl class="br-meta">
          <div><dt>Disclosed</dt><dd>11 Jun 2025</dd></div>
          <div><dt>Vendor</dt><dd>Microsoft 365 Copilot</dd></div>
          <div><dt>Reported by</dt><dd>Aim Labs, Aim Security</dd></div>
          <div><dt>Identifier</dt><dd>CVE-2025-32711, CVSS 9.3 (Microsoft), 7.5 (NVD)</dd></div>
          <div><dt>Job</dt><dd>Enterprise copilot, Graph-grounded</dd></div>
          <div><dt>Blast radius</dt><dd>Content in Copilot's context</dd></div>
          <div><dt>Notable</dt><dd>Microsoft patched it server-side; no exploitation reported in the wild</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>Researchers documented a production path in which an email could become a tool instruction. Copilot retrieved tenant content and inbound mail into one working context, placing untrusted text beside privileged internal data.</p>
        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li><div class="br-step">Copilot retrieves the user's tenant content and inbound mail into one context. An external email can therefore sit beside internal files, Teams messages, and prior chat.</div></li>
          <li>
            <div class="br-step">Standing authority provides tenant-scoped Graph access, far broader than answering one question about one thread.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Identity-derived token exchange</span><p>Each Graph call receives a short-lived token derived from the human and the task in front of them. Reading an unrelated internal file because an email requested it does not match the task, so no token is minted for that access.</p></div>
          </li>
          <li>
            <div class="br-step">A prompt-injection classifier and link and image handling rules form the main barriers. Researchers chained around them with reference-style Markdown and automatically fetched content.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Default-deny, in both directions</span><p>Inbound untrusted mail is treated as data until a separate validator turns it into a request. Outbound, a fetch to an unclassified external host is judged, so Markdown that reads as an instruction cannot mint a retrieval.</p></div>
          </li>
          <li class="br-terminal">
            <div class="br-step">The model's next helpful action becomes exfiltration. The credential is not stolen; the product's own Graph permission is already in place.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">AuthBridge + IBAC</span><p>The sidecar sees the outbound call. Sending internal context to a host because an email requested it does not match the task, so the call is stopped before it leaves the pod.</p></div>
          </li>
          <li><div class="br-step">In the demonstrated chain, the only trace of the leak is the copilot's own chat and the outbound request itself, both inside the channel being drained.</div><div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Independent audit plane</span><p>The decision record lives in a separate namespace behind credentials the copilot does not hold, outside the channel the exfiltration attempts to drain.</p></div></li>
        </ol>
        <blockquote class="br-quote">The first known zero-click AI vulnerability.<footer>Aim Labs, who also named the underlying class of attack LLM Scope Violation</footer></blockquote>
        <p class="br-sources">Sources: <a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711" rel="noopener noreferrer" target="_blank">Microsoft MSRC / CVE-2025-32711</a> &middot; <a href="https://www.aim.security/lp/aim-labs-echoleak-blogpost" rel="noopener noreferrer" target="_blank">Aim Labs</a> &middot; <a href="https://socprime.com/blog/cve-2025-32711-zero-click-ai-vulnerability/" rel="noopener noreferrer" target="_blank">SOC Prime</a> &middot; <a href="https://checkmarx.com/zero-post/echoleak-cve-2025-32711-show-us-that-ai-security-is-challenging/" rel="noopener noreferrer" target="_blank">Checkmarx</a> &middot; <a href="https://sentra.io/blog/copilot-echoleak-prompt-injection" rel="noopener noreferrer" target="_blank">Sentra</a></p>
      </div>
    </article>

    <article class="br-case" id="case-03">
      <div class="br-case-head">
        <div class="br-case-title"><span class="br-case-no">CASE 03</span><h3>A Morse-code tweet signs away a wallet's balance</h3></div>
        <dl class="br-meta">
          <div><dt>Date</dt><dd>4 May 2026</dd></div>
          <div><dt>Agents</dt><dd>Grok (xAI) and Bankr's Bankrbot</dd></div>
          <div><dt>Chain</dt><dd>Base network</dd></div>
          <div><dt>Job</dt><dd>Agent wallet with on-chain execution</dd></div>
          <div><dt>Blast radius</dt><dd>About 3 billion DRB tokens, roughly $150,000 to $200,000; about 80% later returned</dd></div>
          <div><dt>Mechanism</dt><dd>Airdropped NFT permission escalation and prompt injection</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>The private key remained in place, and the contract behaved as designed. External text became a signed transaction because two agents trusted each other and a public reply.</p>
        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li><div class="br-step">Grok is asked to read a public reply and decode a message. The task is ordinary assistant work.</div></li>
          <li>
            <div class="br-step">The wallet behind the agent chain can move its whole balance. Before the attack, an airdropped Bankr Club Membership NFT widened its permissions inside Bankr to include transfers and swaps. Nobody at xAI or Bankr approved the change.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Vault + Vault Secrets Operator</span><p>The signing key never sits in the agent container. It lives in Vault Transit, and only the registered transfer workload may call sign, under a short TTL. Destination allow-lists and amount caps sit in the gateway in front of that call. An NFT arriving in a wallet cannot change either.</p></div>
          </li>
          <li>
            <div class="br-step">The attacker posts the transfer instruction in Morse code, reportedly with concatenation tricks mixed in, then asks Grok to decode and print it. Grok, which had earlier declined a plain request because it could not move funds, emits the literal command string in a public reply and tags Bankrbot.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Tool gateway + role-based access</span><p>Signing and transfer are separate registrations from reading and decoding social text. A decode session holds no transfer tool, so a decoded string remains text.</p></div>
          </li>
          <li class="br-terminal">
            <div class="br-step">Bankrbot reads the reply as authorization and signs the transfer. Between $150,000 and $200,000 in DRB tokens leaves the wallet. The chain inclusion is final. About 80% of the value came back later, after the DRB community identified the attacker and negotiated.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">AuthBridge + IBAC</span><p>The proposed signature is judged against the task on record, which was decoding a message. A full-balance transfer to a new address fails that test and never broadcasts.</p></div>
          </li>
          <li><div class="br-step">The only records are the public X thread and the on-chain transaction. Neither shows what the agent believed it was authorised to do.</div><div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Independent audit plane</span><p>The proposed signature is logged out of process before broadcast, creating evidence of intent before the funds leave. The record is independent of the agent and the public transaction stream.</p></div></li>
        </ol>
        <p>Bankr's founder, 0xDeployer, said in the post-mortem that an earlier version of the agent had a hardcoded block on Grok replies, added to stop one model injecting another. The block did not survive a rewrite. A boundary that lives in one service's code is one refactor away from disappearing. A boundary enforced by a separate sidecar is not.</p>
        <p><b>A near neighbour, a year earlier.</b> In March 2025, the AiXBT agent sent 55.5 ETH, about $106,000, from its Simulacrum wallet after an attacker got into the agent's dashboard and queued two malicious replies. The maintainer said the model itself was not manipulated, so the entry point differs. The rest rhymes: a signing capability that could move the book, and an on-chain record as the only account of why.</p>
        <p class="br-sources">Sources: <a href="https://oecd.ai/en/incidents/2026-05-04-4a73" rel="noopener noreferrer" target="_blank">OECD AI Incidents Monitor</a> &middot; <a href="https://www.ccn.com/news/crypto/ai-agent-drained-for-200k-with-this-one-tweet-hack-heres-how/" rel="noopener noreferrer" target="_blank">CCN</a> &middot; <a href="https://www.giskard.ai/knowledge/how-grok-got-prompt-injected-an-x-user-drained-150-000-from-an-ai-wallet" rel="noopener noreferrer" target="_blank">Giskard</a> &middot; <a href="https://cryptoslate.com/how-one-trader-exploited-grok-and-morse-code-to-trick-ai-agent-into-sending-billions-of-crypto-tokens-from-a-verified-wallet/" rel="noopener noreferrer" target="_blank">CryptoSlate, with the Bankr post-mortem</a> &middot; AiXBT precedent: <a href="https://www.theblock.co/post/346911/ai-crypto-bot-aixbt-lost-eth-hack-unauthorized-dashboard-access" rel="noopener noreferrer" target="_blank">The Block</a> &middot; <a href="https://incidentdatabase.ai/cite/1003/" rel="noopener noreferrer" target="_blank">AI Incident Database 1003</a></p>
      </div>
    </article>

    <article class="br-case" id="case-04">
      <div class="br-case-head">
        <div class="br-case-title"><span class="br-case-no">CASE 04</span><h3>Air Canada is made to keep a promise its chatbot invented</h3></div>
        <dl class="br-meta">
          <div><dt>Citation</dt><dd>Moffatt v. Air Canada, 2024 BCCRT 149, 14 Feb 2024</dd></div>
          <div><dt>Operator</dt><dd>Air Canada</dd></div>
          <div><dt>Job</dt><dd>Customer-facing policy agent</dd></div>
          <div><dt>Blast radius</dt><dd>A bereavement-fare promise; C$812.02 awarded, and a ruling cited worldwide</dd></div>
          <div><dt>Notable</dt><dd>The tribunal rejected the separate-entity defence</dd></div>
        </dl>
      </div>
      <div class="br-case-body">
        <p>The chatbot did not call an API. It committed the company in language, and the airline was held to its words. That makes this case useful for any system that can spend money, reputation, or legal position through speech.</p>
        <div class="br-chain-label">Chain of events</div>
        <ol class="br-chain">
          <li><div class="br-step">A customer asks the airline's website chatbot about bereavement fares. The chatbot says he can claim the discount retroactively within 90 days of the ticket being issued. The airline's own bereavement page says the policy does not apply once travel is complete.</div></li>
          <li>
            <div class="br-step">The policy exists as retrieval text the model can quote. It is not an authorization check on a commitment, and the channel can speak for the airline.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Versioned policy source</span><p>The generator quotes from a policy artifact at a known revision, a Git commit or an OPA bundle, not whatever wiki text retrieval surfaced. A quoted fare rule carries the digest of the policy it came from rather than being improvised at the counter.</p></div>
          </li>
          <li class="br-terminal">
            <div class="br-step">The customer relies on the promise, books, and is later refused. A tribunal holds the airline to the chatbot's words.</div>
            <div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Tool gateway and IBAC for typed commitments</span><p>Committing the firm is modelled as a registered action. Quoting a fare is allowed. Promising an exception outside policy is not registered, and any request for one is judged against the policy object rather than granted in prose.</p></div>
          </li>
          <li><div class="br-step">The only record of the commitment is the screenshot the customer took of the chat.</div><div class="br-intercept"><div class="br-mitigation">Mitigation</div><span class="br-who">Independent audit plane</span><p>The customer-facing commitment is bound to a workload identity and the policy revision behind it. The record is an authorization decision, not a screenshot.</p></div></li>
        </ol>
        <blockquote class="br-quote">A remarkable submission.<footer>The Civil Resolution Tribunal, on Air Canada's separate-entity defence</footer></blockquote>
        <p class="br-sources">Sources: <a href="https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html" rel="noopener noreferrer" target="_blank">Moffatt v. Air Canada, 2024 BCCRT 149 (CanLII)</a> &middot; <a href="https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/" rel="noopener noreferrer" target="_blank">American Bar Association</a> &middot; <a href="https://www.pinsentmasons.com/out-law/news/air-canada-chatbot-case-highlights-ai-liability-risks" rel="noopener noreferrer" target="_blank">Pinsent Masons</a> &middot; <a href="https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot" rel="noopener noreferrer" target="_blank">McCarthy Tetrault</a></p>
      </div>
    </article>

  </div>
</section>

<section id="coverage">
  <div class="container" style="display:grid; gap:1.5rem;">
    <div class="br-intro"><div class="br-label">Coverage</div><h2>Which control acts, and when</h2><p>Read the columns as defence in depth. Each layer answers a different question: who is calling, what may they hold, what may they reach, and does this action match the intent on record.</p></div>
    <div class="br-legend"><span><span class="br-chip br-stop">Blocks</span> the action is stopped before it executes</span><span><span class="br-chip br-contain">Contains</span> the action executes, the damage is bounded</span><span><span class="br-chip br-record">Records</span> evidence survives outside the agent's reach</span><span><span class="br-chip br-none">No effect</span> outside this control's scope</span></div>
    <div class="br-scroller">
      <table class="br-matrix">
        <thead><tr><th scope="col">Control</th><th scope="col">01 OpenClaw</th><th scope="col">02 EchoLeak</th><th scope="col">03 Grok/Bankr</th><th scope="col">04 Air Canada</th></tr></thead>
        <tbody>
          <tr><th scope="row">SPIRE workload identity + mesh mTLS</th><td><span class="br-chip br-contain">Contains</span></td><td><span class="br-chip br-contain">Contains</span></td><td><span class="br-chip br-contain">Contains</span></td><td><span class="br-chip br-none">No effect</span></td></tr>
          <tr><th scope="row">Vault + VSO, per-namespace paths</th><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-contain">Contains</span></td><td><span class="br-chip br-contain">Contains</span></td><td><span class="br-chip br-none">No effect</span></td></tr>
          <tr><th scope="row">Identity-derived token exchange</th><td><span class="br-chip br-contain">Contains</span></td><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-none">No effect</span></td></tr>
          <tr><th scope="row">Tool gateway registration</th><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-contain">Contains</span></td><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-none">No effect</span></td></tr>
          <tr><th scope="row">AuthBridge sidecar, out of process</th><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-none">No effect</span></td></tr>
          <tr><th scope="row">IBAC judge, <span class="br-k">unclassified_policy: judge</span></th><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-stop">Blocks</span></td><td><span class="br-chip br-stop">Blocks</span></td></tr>
          <tr><th scope="row">Independent audit plane</th><td><span class="br-chip br-record">Records</span></td><td><span class="br-chip br-record">Records</span></td><td><span class="br-chip br-record">Records</span></td><td><span class="br-chip br-record">Records</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container"><div class="br-notes"><div class="br-label">Reading the matrix</div><h2>How to read this</h2><ol>
    <li><b>These agents ran without a governed platform underneath them.</b> OpenClaw ran locally with a live mailbox token. Copilot used standing tenant-wide Graph permissions. The wallet chain trusted a public reply from another agent. The airline bot committed the firm in free text. The enforcement points were absent from each path. A governed environment supplies those missing boundaries.</li>
    <li><b>IBAC is one judge in a chain.</b> It reviews intent on the outbound path, behind workload identity, credential scope, and gateway registration, alongside the inbound validation chain. Its verdict is a judgement, so it works with the layers around it.</li>
    <li><b>Speech can be an action.</b> The Air Canada column shows a real limit: controls that bind tool calls and credentials cannot stop a bot that binds the company through free text. The commitment must become a typed action, so quoting a policy is allowed and promising an exception outside it is judged.</li>
  </ol></div></div>
</section>

<section><div class="container br-close"><p>Every incident on this page was verified against primary reporting or a tribunal record before publication. Where secondary write-ups disagreed with the primary source, the primary source is what appears here. Token figures for the wallet case are given as a range because reporting varied.</p><p>The controls described run as a working demonstration environment: an agent attempts a misaligned tool call, the sidecar blocks it before it leaves the pod, and the decision is searchable in the audit plane seconds later. <a href="mailto:sales@mcindi.com?subject=Agent%20Security%20Briefing">Ask us to walk you through it</a>.</p></div></section>

</div>
