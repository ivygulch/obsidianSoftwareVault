# Ideal State Method

Writing-first app development, after Daniel Miessler's "Writing Is Closer to Thought Than Code" (2026). One living document per project, the Ideal State Artifact (ISA), holds the intent; code is an implementation of it; criteria with evals are both the build target and the test harness.

## Pages
- [[Craft/Ideal State Method/Method|Method]] — the method as practiced in this vault: artifacts, the two loops, the eval ladder mapped to the iOS stack, the skills, the rules
- [[Craft/Ideal State Method/Adoption Plan|Adoption Plan]] — phased plan to bring the method into the active projects, with done-criteria and kill criteria
- [[Craft/Ideal State Method/Article Notes|Article Notes]] — source notes on the Miessler article, Pocock's counterpoint, and the grilling skill

## Vault pieces
- Template: [[Templates/Ideal State Artifact|Ideal State Artifact]] → `Projects/<Project>/Ideal State.md`
- Template: [[Templates/Eval Run|Eval Run]] → `Projects/<Project>/Evals/<date> Eval Run.md`
- Skills: `/isa-discuss`, `/isa-criteria`, `/isa-check` (in `.claude/skills/`)

## ISAs in the vault (Dataview)

```dataview
TABLE status, criteria_done, criteria_open, updated
FROM "Projects"
WHERE type = "isa"
SORT updated DESC
```
