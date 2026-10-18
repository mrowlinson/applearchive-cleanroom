# PARENT-036: sweep seat committed directly to master

- Commit `2d7ff13` (2026-10-09 09:43, author encode-sweep): GATE-790b284.md + hb107 NOTE, committed on `master`, not `lanes/encode-sweep`.
- Seats commit local-only on their own `lanes/*` branch in their own worktree. Never commit on `master` / in the main checkout.
- Content was harmless (own quiz records) and now pushed to origin as part of master; no action needed this time. Repeat = the commit gets reverted from master and re-landed on the lane.
