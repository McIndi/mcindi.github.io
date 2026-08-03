Title: LogSieve - In-Browser Log Exploration
Slug: logsieve
Template: product
Status: hidden
Summary: Analyze, filter, and explore log files entirely in the browser. Build extractors, filter from results, and investigate without moving data off-device. MIT licensed.
save_as: software/logsieve/index.html
url: software/logsieve/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">MIT &bull; Client-Side &bull; Offline</div>
        <h1>LogSieve</h1>
        <p>In-browser log exploration and filtering that runs entirely in the browser. Load your log files, build extractors, filter directly from the results view, and investigate without sending anything to a server.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="https://www.mcindi.com/logsieve" target="_blank" rel="noopener noreferrer">Open LogSieve</a>
          <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=LogSieve%20Support%20Inquiry">Request Support Quote</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <span class="stat-num">0</span>
          <span class="stat-label">Server requests at runtime</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">100%</span>
          <span class="stat-label">Client-side processing</span>
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
      <h2>Analyze Logs Without Moving Them</h2>
      <p>Designed for environments where shipping logs to an external service isn&rsquo;t an option.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Privacy</span>
        <h3>Nothing Leaves the Browser</h3>
        <p>Log data is loaded and processed entirely in memory. When you close the tab, nothing persists. No backend, no telemetry, no upload.</p>
      </article>
      <article class="card">
        <span class="badge">Offline</span>
        <h3>Air-Gap Ready</h3>
        <p>Download once and run with no internet connection. Works on isolated networks, secure facilities, and classified environments.</p>
      </article>
      <article class="card">
        <span class="badge">Analysis</span>
        <h3>Filter &amp; Search</h3>
        <p>Filter log lines by pattern, level, timestamp range, or custom criteria. Find the signal in large log files without writing grep scripts or round-tripping through a hosted search service.</p>
      </article>
      <article class="card">
        <span class="badge">Extraction</span>
        <h3>Build Reusable Extractors</h3>
        <p>Turn recurring parsing logic into reusable extractor definitions so structured fields can be surfaced quickly during incident work, even when the original logs were never normalized.</p>
      </article>
      <article class="card">
        <span class="badge">Investigation</span>
        <h3>Right-Click Filtering</h3>
        <p>Apply filters straight from the results grid with context-menu actions. When a field value matters, you can pivot on it immediately instead of retyping or rebuilding the filter by hand.</p>
      </article>
      <article class="card">
        <span class="badge">Feedback</span>
        <h3>Action Confirmation in Context</h3>
        <p>Toast notifications confirm filter and extractor actions as you work, which keeps fast-moving investigations understandable without cluttering the screen.</p>
      </article>
      <article class="card">
        <span class="badge">Portability</span>
        <h3>Single File Deployment</h3>
        <p>One HTML file. No installation, no dependencies, no build process. Carry it on a USB drive or share it as an email attachment.</p>
      </article>
      <article class="card">
        <span class="badge">Compliance</span>
        <h3>No Data Exfiltration Risk</h3>
        <p>Use LogSieve on sensitive log data without risk of exfiltration. Safe for PII, PHI, or confidential infrastructure data.</p>
      </article>
      <article class="card">
        <span class="badge">Open Source</span>
        <h3>MIT Licensed</h3>
        <p>Free to use, fork, and redistribute. Audit the source yourself to verify the zero-exfiltration guarantee.</p>
      </article>
      <article class="card">
        <span class="badge">Performance</span>
        <h3>Multi-MB Log Files</h3>
        <p>Optimized for large log files with efficient in-memory data structures, lazy processing, and background workers. Analyze without waiting for a SIEM query to return.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Where LogSieve Gets Used</h2>
    </div>
    <div class="grid">
      <article class="card">
        <h3>Incident Response</h3>
        <p>Pull logs off a compromised system, open LogSieve locally, build the extractor you need, and analyze without routing evidence through your corporate proxy or logging pipeline.</p>
      </article>
      <article class="card">
        <h3>Regulated Environments</h3>
        <p>Healthcare and financial services teams can analyze logs containing PHI or PII without moving data outside the approved security boundary.</p>
      </article>
      <article class="card">
        <h3>On-Call Debugging</h3>
        <p>Engineers troubleshooting production issues can load multi-MB log files directly in the browser, pivot with contextual filters, and keep moving without waiting for a SIEM query to return.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Works Well With</h2>
      <p>LogSieve is often the offline starting point. Here are good next steps when you need more.</p>
    </div>
    <div class="grid">
      <article class="card">
        <h3>Delve &amp; SIEMatic</h3>
        <p>Outgrew a single HTML file? When you need central indexing, scheduled alerting, and retention across many hosts, graduate to <a href="/software/delve/">Delve</a> or <a href="/software/siematic/">SIEMatic</a>.</p>
      </article>
      <article class="card">
        <span class="badge">MIT &bull; Browser-Native</span>
        <h3>WebUtils</h3>
        <p>It follows the same offline, single-file approach. See the rest of the toolkit including Kanban, Secret Share, Regex Workbench, and more, all zero-telemetry and local-first.</p>
        <a class="btn btn-ghost" href="/software/webutils/">Learn More &rarr;</a>
      </article>
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <div class="card">
      <h3>Free to Use. Commercially Supported.</h3>
      <p>LogSieve is MIT licensed: download, use, and share freely. Commercial support contracts available for organizations that need SLA-backed maintenance and feature roadmap input.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://www.mcindi.com/logsieve" target="_blank" rel="noopener noreferrer">Open LogSieve</a>
        <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=LogSieve%20Support%20Inquiry">Request Support Quote</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
