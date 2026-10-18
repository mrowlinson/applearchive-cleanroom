# PARENT-064: spark quota dead until 2026-10-19 — seats relaunched on wonder

- 2026-10-14 ~09:32: viewer-r4 + sweep2-r6 launches died on
  API 429: muse-spark-1.3 subscription quota exhausted, window
  resets 2026-10-19T00:00:00Z. writer2/sweep/cport runs died
  the same way; by 2026-10-15 zero workflows live, lanes cold
  29h+. Monitor had auto-stopped 06:06 (output flood), cron
  deliveries batched hours late: empty seats went unseen.
- Action (parent, 2026-10-15): relaunch all 5 encode seats
  pinned muse-wonder-1.0 (the only live model) + PV-157/159
  workflows on wonder. Owner may veto the model; empty
  pipeline for 5 days was the worse branch. PV batteries
  also run parent-side inline while quota is out.
- Monitor restarted with selective filter (GATE/VERIFY/CLAIM/
  PV/PARENT + lane tips only; heartbeats ignored).
- Merges continue parent-side under merge.lock.d, local-only.
