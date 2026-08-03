Title: Trailhead - Codebase Indexing & Semantic Search
Slug: trailhead
Template: product
Status: hidden
Summary: A CLI and HTTP API that parses a codebase into a queryable property graph in SQLite, with tree-sitter parsing across 14 languages, vector embeddings, and a browser UI for semantic code search. MIT licensed.
save_as: software/trailhead/index.html
url: software/trailhead/

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="eyebrow">MIT &bull; Python &bull; CLI + HTTP API</div>
        <h1>Trailhead</h1>
        <p>Trailhead parses a source tree into a property graph of modules, classes, functions, and their relationships, then stores it in a single SQLite file. Add vector embeddings for semantic search over your own codebase through a CLI, a warm-model HTTP API, and a browser UI that all run locally.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="https://github.com/McIndi/trailhead" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Trailhead%20Inquiry">Talk to an Engineer</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <span class="stat-num">14</span>
          <span class="stat-label">Languages via tree-sitter</span>
        </div>
        <div class="stat-box">
          <span class="stat-num">SQLite</span>
          <span class="stat-label">Single-file graph &amp; vectors</span>
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
      <h2>A Queryable Graph of Your Own Code</h2>
      <p>Index once, then query it from the CLI, the HTTP API, or a browser UI. Your code stays on your machine.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">Indexing</span>
        <h3>Property Graph in SQLite</h3>
        <p>Parses source files into vertices and edges for modules, classes, functions, and relationships, then persists them to a single SQLite database. Smart sync runs a full build first, then incremental updates.</p>
      </article>
      <article class="card">
        <span class="badge">Language Support</span>
        <h3>Polyglot via Tree-sitter</h3>
        <p>Python works out of the box. JavaScript, TypeScript, Rust, Go, Java, C#, C, C++, Ruby, PHP, Bash, HTML, and Ansible-shaped YAML are available as optional extras. Install only the languages you need.</p>
      </article>
      <article class="card">
        <span class="badge">Search</span>
        <h3>Semantic Similarity Search</h3>
        <p>Generate embeddings with sentence-transformers and query them for semantic similarity, not just exact text match. Falls back to SQLite BLOB storage when the vector extension isn't available on a given platform.</p>
      </article>
      <article class="card">
        <span class="badge">Live Updates</span>
        <h3>Background Reindexing</h3>
        <p>The server watches the source tree and reindexes changed files incrementally while keeping the embedding model warm in memory, so there is no need to rerun the indexer by hand.</p>
      </article>
      <article class="card">
        <span class="badge">Interface</span>
        <h3>Browser UI &amp; CLI</h3>
        <p>A single <code>th</code> command handles indexing, serving, and querying. The same server exposes an interactive browser UI at <code>localhost:8000</code> for visualizing and querying the graph directly.</p>
      </article>
      <article class="card">
        <span class="badge">Integration</span>
        <h3>HTTP API &amp; OpenAPI Schema</h3>
        <p>Full REST API for embeddings, SQL queries, semantic search, and graph traversal, documented at <code>/openapi.json</code> and <code>/docs</code>. Built for scripting and for feeding an LLM prompt context.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Who It&rsquo;s Built For</h2>
      <p>Anyone who needs a codebase's structure and meaning queryable, without shipping the code anywhere.</p>
    </div>
    <div class="grid">
      <article class="card">
        <h3>AI &amp; LLM Tooling Builders</h3>
        <p>Give an agent or a RAG pipeline structured, queryable context about a codebase instead of dumping raw files into a prompt window.</p>
      </article>
      <article class="card">
        <h3>Platform &amp; Developer Tooling Teams</h3>
        <p>Explore an unfamiliar or legacy codebase's structure, including module boundaries, call relationships, and cross-file references, without reading it file by file.</p>
      </article>
      <article class="card">
        <h3>Regulated &amp; Air-Gapped Environments</h3>
        <p>Everything runs locally against a SQLite file. No code, embeddings, or queries leave the machine running Trailhead.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Get Started</h2>
    </div>
    <div class="card" style="max-width:640px;">
      <pre style="margin:0;background:#0f172a;color:#e2e8f0;padding:1.25rem;border-radius:12px;overflow-x:auto;font-size:.9rem;"><code>pip install trailhead
th index .
th serve .</code></pre>
    </div>
    <p style="margin-top:1rem;color:var(--muted);">Then visit <code>http://localhost:8000</code> for the browser UI, or query straight from the CLI with <code>th query similar "..."</code>.</p>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Works Well With</h2>
      <p>Dev-tooling neighbors from the same shop.</p>
    </div>
    <div class="grid">
      <article class="card">
        <span class="badge">MIT &bull; Browser-Native</span>
        <h3>WebUtils</h3>
        <p>Repo2Prompt packages a codebase for LLM prompt contexts entirely in the browser. Trailhead is the deeper local option, with a persistent queryable graph and semantic search over the same code.</p>
        <a class="btn btn-ghost" href="/software/webutils/">Learn More &rarr;</a>
      </article>
      <article class="card">
        <span class="badge">MIT &bull; Python &bull; FastAPI</span>
        <h3>Adapt</h3>
        <p>Point Adapt at a folder for auth-gated APIs and MCP resource exposure. Point Trailhead at the same folder for semantic code search and a queryable property graph.</p>
        <a class="btn btn-ghost" href="/software/adapt/">Learn More &rarr;</a>
      </article>
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <div class="card">
      <h3>Free to Use. Commercially Supported.</h3>
      <p>Trailhead is MIT licensed. McIndi offers commercial support contracts for organizations that need SLA-backed maintenance, custom language support, and integration work.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://github.com/McIndi/trailhead" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        <a class="btn btn-ghost" href="mailto:sales@mcindi.com?subject=Trailhead%20Inquiry">Talk to an Engineer</a>
        <a class="btn btn-ghost" href="/#software">&larr; All Software</a>
      </div>
    </div>
  </div>
</section>
