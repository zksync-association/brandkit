# Execution Prompt — Update the ZK Nation brand voice & language guidelines

> Structured per Anthropic's *Prompting Claude Fable 5* guide
> (platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5).
> Drop this into a fresh Fable 5 session (effort: `high`) with the repo checked out.

---

## Why this is being asked (intent)

I maintain the **ZKsync Association / ZK Nation brand kit** — a Claude Code skill plus a public
site that lets any agent or contributor apply the brand to docs, decks, sites, and components.
The single source of truth for how the brand *sounds* is `skill/references/voice-tone-vocabulary.md`.

That file was written mainly from the website and the ZK Credo. Since then we've published two
authoritative, long-form artifacts that exercise registers the current guide barely covers:
the **ZKsync Association Operational Report 2024–2025** (a board letter, a year-in-review, and a
legal disclaimer, all in one document) and the fuller **docs.zknation.io** corpus. People writing
reports, governance posts, and legal copy have no exemplar to anchor on. With that in mind:

## Task

Update the voice & language guidance in `skill/references/voice-tone-vocabulary.md` so it reflects
**both** sources, and add a reference block of **verbatim** brand copy that writers can pattern-match
against. The deliverable is the edited reference file (and its synced site mirror), not a summary.

## Sources of truth (read these; quote only what you can point to)

1. **The Operational Report** — `/ZKsync_Association_Operational_Report_2024-2025 (3).pdf` (repo root).
   Read all 27 pages. Note the distinct registers: the Board letter (resolute, institutional),
   the Year-in-Review (factual past-tense reporting, incidents stated plainly), the Legal
   Disclaimer (sober, hedged), and the "Onward" close (invitational).
2. **The docs** — `/_docs_repo/` (a local mirror of docs.zknation.io). Anchor especially on
   `zk-nation/mission-zk-credo.md`, `zk-nation/zksync-governance-system-north-star.md`, and
   `zk-nation-community/zk-nation-code-of-conduct.md`.
3. **The current guide** — `skill/references/voice-tone-vocabulary.md` (the file you're editing).
4. **`CLAUDE.md`** — the verified brand facts and the edit/sync workflow. Do not contradict it.

## What to change

- **Tone table:** add the registers the report surfaces — an *Operational / report* row and a
  *Legal / disclaimer* row — each with a real register example pulled verbatim from the report.
- **Voice principles:** keep the existing five; where the report or docs give a sharper verbatim
  illustration of one, swap it in. Don't invent new principles unless a source genuinely demands it.
- **Vocabulary:** add the governance and token-mechanics terms the report introduces (Capped Minter,
  Minter Mod, mint-on-demand, Token Program / TPP, ZIP, GAP, Token Assembly, Guardians, Security
  Council, Emergency Upgrade Board, ZKsync Gateway, ZKsync Atlas, ZKGPS), spelled and cased exactly
  as the report uses them. Extend the glossary to match.
- **Canonical phrases:** add the report's reusable lines (e.g. the Board letter's close and the
  report's sign-off), kept verbatim.
- **Reference exemplars (new section):** a block of verbatim passages from the report and docs,
  each tagged with its register and source, so writers have ground-truth copy to imitate. Curate
  the most representative passages across registers — do not paste the whole report.

## Boundaries (do only this)

- Edit **only** `skill/references/voice-tone-vocabulary.md`. Don't touch tokens, templates, or other
  reference files, and don't restyle the site.
- Don't soften or rewrite the brand's verified facts (spelling rules, the navy ink, the values order).
  This is an additive update to *voice*, not a redesign.
- Every quote must be verbatim from a source you actually read. If you can't point to it, don't
  attribute it. Don't paraphrase a quote and present it as one.
- Preserve the file's existing structure and markdown style; match its heading depth and table format.
- When you have enough to act, act. Don't survey options you won't take.

## After editing

1. Run `bash scripts/sync.sh` to mirror the reference into `site/brand/references/` and rebuild the
   skill zip. Confirm the mirror updated.
2. Report what changed: list the new registers, the new vocabulary, and the exemplars you added,
   each tied to its source. State plainly if anything in the sources conflicted with a verified fact.
3. Do **not** publish the site or push to GitHub — those are separate, manually-authorized steps
   (publishing requires the maintainer's here.now account; pushing requires the `rafathebuilder-ZK`
   GitHub account). Leave the working tree staged for the maintainer to review.
