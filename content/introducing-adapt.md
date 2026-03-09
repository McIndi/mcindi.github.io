Title: Introducing Adapt: Your Folder Is Already a Server
Author: Cliff
Date: 2026-03-09 10:00
Category: Announcements
Tags: server, file sharing, authentication, permissions, Python, FastAPI
Summary: An introduction to Adapt, a lightweight server that turns a folder into a secure, queryable workspace for data, documents, and media.
Slug: introducing-adapt
Status: published

A lot of the work I do as a Software Engineer/architect/developer/wizzard-of-many-hats, produces artifacts (data exports, analysis results, documentation, recorded walkthroughs) that need to get in front of clients or teammates without ending up somewhere they shouldn't be. The usual options are clunky: shared drives with no access control, cloud storage services with complex permission models, or standing up dedicated infrastructure for what is essentially a file sharing problem.

I wanted something simpler. Something I could point at a directory, configure once, and hand a URL to the right people with confidence that the wrong people couldn't get in.

That's why I built Adapt.

---

## What It Does

Adapt is a lightweight server you point at a folder. It scans what's in that folder and automatically makes it available over HTTP with authentication, permissions, and an admin interface included out of the box.

What "available" looks like depends on the file:

**Spreadsheets and CSVs**: become queryable data tables with sortable, searchable HTML interfaces and full REST APIs. You can read, filter, and, if you choose, edit data right from the browser.

**Markdown and HTML documents**: get rendered and served as formatted pages, discoverable from a landing page that adapts to what each user is allowed to see.

**Audio and video files**: meeting recordings, training walkthroughs, Zoom exports become streamable from the same workspace. Link to them from any Markdown or HTML document, and they're one click away for anyone with access.

**Python files**: become live API endpoints. Drop a `.py` file with a FastAPI router into the folder and Adapt mounts it automatically. No restart required.

Everything lives under one auth layer. Users log in, see only what they're permitted to see, and every action is recorded in an audit log.

---

## The Problem It Solves

I work across multiple clients and contexts. Sharing work product with the right people, while keeping it away from the wrong ones, is a recurring operational problem that doesn't have a great lightweight answer.

SharePoint is overkill and requires an IT footprint. Google Drive works, but granular permissions at the file level get messy fast and I'm not always comfortable with where data ends up. Standing up a proper web application for every engagement isn't realistic.

Adapt fills that gap. It's designed for the kind of work that produces a folder of outputs (data, documents, recordings) and needs a controlled way to expose them to a specific audience. No cloud account required. No database to provision. Just a directory and a config file.

---

## Who Else Might Find It Useful

While I built this for my own use, I think there's a broader audience:

**Small technical teams** who have operational data in spreadsheets and want a shared, queryable interface without migrating to a database or a SaaS tool.

**Consultants and freelancers** who deliver data-heavy work and need a clean, professional way to give clients access to results without exposing everything.

**Anyone running internal training or onboarding** who wants to organize documents, recordings, and reference data in one place with proper access control.

---

## Where It Stands Today

Adapt is early. I've been using it internally and I'm releasing it now to get real feedback from people with different use cases than mine.

The core is solid:

- Session-based authentication with role and group permissions
- REST APIs and HTML UIs auto-generated from CSV, Excel, and Parquet files
- Markdown and HTML document serving
- Audio and video streaming
- Python handler plugins for custom endpoints
- An admin dashboard for managing users, groups, permissions, and API keys
- Full audit logging

Things that are on the roadmap but not there yet: full-text search across all content types, PostgreSQL support for larger deployments, and a richer plugin ecosystem.

---

## Early Access and Feedback

The project is open source and available on [GitHub](https://github.com/McIndi/adapt). I'm genuinely interested in hearing from people who try it: what works, what doesn't, what use cases I haven't thought of.

If you're building something similar, solving a similar problem a different way, or just have thoughts on the direction, I'd welcome the conversation. Drop a comment below or reach out directly.

More posts to follow: I'll get into the technical design, the plugin architecture, and some of the tradeoffs I made along the way.