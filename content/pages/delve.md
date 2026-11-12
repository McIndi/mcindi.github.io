Title: Delve - Open-Source Data Workbench
Slug: delve
Template: product
Status: hidden
Summary: Open-source data workbench. A pipeline search pulls data from HTTP APIs, SQL databases and files, reshapes it, and sends the results out by email or on a schedule.
save_as: software/delve/index.html
url: software/delve/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">AGPL-3.0 &bull; Django &bull; PostgreSQL</div>
        <h1>Delve</h1>
        <p>An open-source data workbench for ops teams, ad-hoc analysis and lightweight ETL. A pipeline search pulls data from HTTP APIs, SQL databases and files, reshapes it, and sends the results out. Dashboards and alerts sit on the same searches, without a heavy analytics stack.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="mailto:sales@mcindi.com?subject=Delve%20Support%20Inquiry">Request Support Quote</a>
          <a class="btn btn-ghost" href="https://github.com/McIndi/delve" target="_blank" rel="noopener noreferrer">GitHub</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <span class="stat-num">33</span>
          <span class="stat-label">Search commands</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">Air-gap</span>
          <span class="stat-label">Ready to deploy</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">AGPL</span>
          <span class="stat-label">Open source</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>What Delve Does</h2>
      <p>Pull data from anywhere, reshape it, and push the results out, all from one pipeline search.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Pull</span>
        <h3>HTTP, SQL and Files</h3>
        <p><code>request</code> calls HTTP APIs, <code>run_query</code> runs SQL against your databases, and <code>read_file</code> reads files. You can also tail log files and receive syslog events into a searchable index.</p>
      </article>
      <article class="card">
        <span class="badge">Reshape</span>
        <h3>Pipeline Search Syntax</h3>
        <p>Filter, transform and aggregate with 33 search commands, including <code>eval</code>, <code>rex</code>, <code>chart</code> and <code>transpose</code>. Search-time and index-time field extraction included.</p>
      </article>
      <article class="card">
        <span class="badge">Visualization</span>
        <h3>Interactive Dashboards</h3>
        <p>Build operational dashboards from your data. Track metrics, visualize trends, and share views with your team.</p>
      </article>
      <article class="card">
        <span class="badge">Push</span>
        <h3>Alerts and Email</h3>
        <p>Define alert conditions on your data pipelines, and use <code>send_email</code> to mail the results of scheduled searches.</p>
      </article>
      <article class="card">
        <span class="badge">Deployment</span>
        <h3>Docker &amp; Air-Gap Ready</h3>
        <p>Docker Compose for standard deployments. Automated packaging via <code>bootstrap.py</code> for air-gapped or fully offline environments.</p>
      </article>
      <article class="card">
        <span class="badge">Extensibility</span>
        <h3>Custom Applications</h3>
        <p>Extend Delve with custom application modules. Build specialized workflows on top of the ingestion and search infrastructure.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>What Teams Use It For</h2>
      <p>Delve is for ops teams and analysts who want answers from their data without the overhead of an enterprise analytics platform.</p>
    </div>
    <div class="grid">
      <article class="card">
        <h3>Operational Monitoring</h3>
        <p>Ingest logs and metrics from your infrastructure. Build dashboards that tell you what&rsquo;s happening right now without shipping data to a cloud service.</p>
      </article>
      <article class="card">
        <h3>Lightweight ETL</h3>
        <p>Pull data from an API or a database, reshape it with a pipeline search, and send the results on by email or on a schedule.</p>
      </article>
      <article class="card">
        <h3>Data Validation</h3>
        <p>Ingest API responses or exported data for validation and troubleshooting. Spot anomalies and inconsistencies before they cause production issues.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Works Well With</h2>
      <p>Delve stays lightweight on purpose. These tools fill the gaps around it.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Public Alpha &bull; Source Available</span>
        <h3>SIEMatic</h3>
        <p>Delve or SIEMatic? Use Delve to work with any data: call APIs, query databases, read files, reshape the results and send them on. Use SIEMatic for security audit and detection: agents that ship Kubernetes and Keycloak events, findings with severity and MITRE ATT&amp;CK mapping, and retention policies. SIEMatic is source-available under the Business Source License, with commercial licensing and support.</p>
        <a class="btn btn-ghost" href="/software/siematic/">Learn More &rarr;</a>
      </article>
      <article class="card">
        <span class="badge">GPLv3 &bull; Open Source</span>
        <h3>MAST</h3>
        <p>Delve already ingests DataPower and API gateway security events. MAST is the estate manager producing them, including backups, config promotion, and governance at scale.</p>
        <a class="btn btn-ghost" href="/software/mast/">Learn More &rarr;</a>
      </article>
      <article class="card">
        <span class="badge">MIT &bull; Client-Side</span>
        <h3>LogSieve</h3>
        <p>Need an offline, single-host look at the same kind of log data? LogSieve does ad-hoc triage entirely in the browser, no server required.</p>
        <a class="btn btn-ghost" href="/software/logsieve/">Learn More &rarr;</a>
      </article>
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <div class="card">
      <h3>Get Started with Delve</h3>
      <p>Delve is AGPL-3.0 open source. McIndi offers commercial support for organizations that need production SLAs, custom integrations, and hands-on onboarding.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="mailto:sales@mcindi.com?subject=Delve%20Support%20Inquiry">Request a Support Quote</a>
        <a class="btn btn-ghost" href="https://github.com/McIndi/delve" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
