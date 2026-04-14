# App Dev Dashboard

Central hub for the app development vault.

## Pipeline
- [[_App Ideas MOC|App Ideas]] — brainstorming space
- [[_Projects MOC|Projects]] — ideas promoted to active work
- [[_App Platform MOC|App Platform]] — marketing, newsletter, website, business dev
- [[_Research MOC|Research]] — cross-cutting tech/market/competitor research

## Idea Pipeline (Dataview)

```dataview
TABLE status, area, updated
FROM "App Ideas"
WHERE status
SORT updated DESC
```

## Active Projects (Dataview)

```dataview
LIST
FROM "Projects"
WHERE file.name = "Brief" OR file.name = this.file.name
```
