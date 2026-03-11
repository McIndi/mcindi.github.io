Title: Protecting Your Local-First Data: Backup Warnings and Per-App Controls in WebUtils
Author: Cliff
Date: 2026-03-11 10:00
Category: Programming
Tags: JavaScript, Web-Development, LocalStorage, IndexedDB, Browser, Vanilla-JS, Data-Management, Backup
Summary: A walkthrough of the data safety improvements shipped in WebUtils: a backup warning banner, per-app export and delete controls, mandatory backup offers on deletion, and snapshot validation.
Slug: common-sense-data-controls
Status: published

One of the quiet risks of browser-based, local-first tools is that your data lives entirely in your hands, which is great for privacy but means there's no server quietly making backups. I learned this the hard way when I accidentally deleted all my data on purpose. So I spent some time hardening the data management story in WebUtils.

Here's what changed and why.

---

## The Problem

WebUtils stores everything in `localStorage` or `IndexedDB`. There's no cloud sync, no undo history, no recovery path. The index page already had a bulk export/import system, but it had four gaps:

- Nothing reminded you to actually use it
- You couldn't act on a single app without touching all of them
- Destructive actions gave you no chance to grab a backup first
- You had no way to know if a snapshot file was valid before importing it

---

## Backup Warning Banner

The first change is a simple amber banner that appears at the top of the page if you have saved data but haven't exported a snapshot in the last 24 hours.

```javascript
const checkBackupWarning = async () => {
  let hasData = false;
  for (const app of APP_REGISTRY) {
    const value = await readAppData(app);
    if (value !== null) { hasData = true; break; }
  }
  if (!hasData) return;

  const lastExport = localStorage.getItem("webutils.lastExport.v1");
  if (!lastExport) {
    showWarning("You have saved data with no backup on record.");
    return;
  }
  const hoursSince = (Date.now() - new Date(lastExport).getTime()) / 3_600_000;
  if (hoursSince >= 24) {
    showWarning(`Last backup was ${Math.floor(hoursSince)} hours ago.`);
  }
};
```

Every export, bulk or per-app, stamps `webutils.lastExport.v1` with the current timestamp, resets the clock, and dismisses the banner.

---

## Per-App Export, Import, and Delete

The bulk controls are still there, but each app row in the Utilities list now has its own Export, Import, and Delete buttons. This matters when you want to, say, restore your Notes without touching your Kanban board.

Per-app import reuses the same validation and restore logic as the bulk path, but first checks that the snapshot actually contains data for the target app:

```javascript
if (!snapshot.apps[app.id]) {
  setStatus(`This snapshot does not contain data for ${app.label}.`);
  return;
}
```

Export and Delete buttons are disabled when there's nothing stored, so the UI always reflects reality.

---

## Mandatory Backup Offer on Delete

Deleting data, whether a single app or everything at once, is the one action that can't be undone. So rather than just asking "are you sure?", both the per-app Delete and the global "Clear all data" button now split into two steps.

First, they offer a backup download:

```javascript
const wantsBackup = await requestConfirmation({
  title: `Back up ${app.label} first?`,
  message: `Deleted data cannot be recovered. Download a backup snapshot now,
            or cancel to skip and proceed to deletion.`,
  confirmText: "Download backup",
});

if (wantsBackup) {
  await exportAppData(app);
}
```

Then, regardless of whether they took the backup, a second confirmation asks them to explicitly confirm the deletion. For "Clear all data", the backup step exports a full snapshot covering every app before the second prompt fires.

The concerns are separated, so each question is easy to answer on its own. Someone who hasn't thought about backups in a while gets a nudge exactly when it matters, tied directly to what they're about to do.

---

## Snapshot Validation

Before this change, importing a corrupted or wrong-format file would either silently do nothing or throw a generic error. Now there's a dedicated `validateSnapshot()` function that checks structure before anything is written:

```javascript
const validateSnapshot = (snapshot) => {
  const issues = [];
  if (typeof snapshot.version !== "number") {
    issues.push("Missing or invalid 'version' field.");
  }
  if (!snapshot.createdAt || isNaN(Date.parse(snapshot.createdAt))) {
    issues.push("Missing or invalid 'createdAt' timestamp.");
  }
  for (const [appId, entry] of Object.entries(snapshot.apps || {})) {
    if (!knownIds.has(appId))
      issues.push(`Unrecognized app ID: "${appId}".`);
    if (!["localStorage", "indexedDB"].includes(entry.storage))
      issues.push(`App "${appId}": invalid storage type.`);
    if (entry.value == null)
      issues.push(`App "${appId}": missing value.`);
  }
  return { valid: issues.length === 0, issues };
};
```

A Validate file button in the Restore section lets you inspect any snapshot before committing to an import. Valid files get a green confirmation with the version, app count, and creation date. Invalid files get a red list of every specific problem found. All import paths, bulk and per-app, run this validation and bail with a clear message if anything looks wrong.

---

## Schema Standardization

While in the area, I bumped the snapshot format to version 3. The changes are minor but make snapshots more self-describing:

```json
{
  "version": 3,
  "generator": "webutils",
  "createdAt": "2026-03-11T14:22:00.000Z",
  "apps": {
    "kanban": {
      "appId": "kanban",
      "storage": "localStorage",
      "key": "webutils.kanban.v2",
      "value": "..."
    }
  }
}
```

The `generator` field identifies the source, and each app entry now carries its own `appId` so it makes sense on its own. Version 2 snapshots import fine without any changes.

---

## The Takeaway

None of this is glamorous. It's the kind of defensive plumbing that only matters the one time you really need it. But for a local-first tool where you're the only backup, that one time is the whole game.
