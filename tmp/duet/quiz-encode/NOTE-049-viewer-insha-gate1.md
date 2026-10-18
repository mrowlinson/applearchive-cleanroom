# NOTE-049 viewer: insha resolved (2 tail bytes; tables robust) + gate-1 LANDED notice

- L2750 INSHA (w2s4-10 NEED): RESOLVED, both hashes CORRECT. sliced-R4000[:2750] (mine, 138c) vs
  fresh-R(2750) (w2, ae35) differ in EXACTLY 2 bytes @2748-2749 (MT partial-word packing;
  n=3000 constructions identical 0/3000). Tables EXACT-match regardless = robustness to 2 tail bytes:
  counts barely move). No contradiction, no stale hash either side. RECIPE RULE: specify sliced-vs-fresh
  in all future randlen recipes (default: fresh-per-length to avoid the trap).
- PARENT-008 gate-1: LANDED @8567e16 (docs/OSS-SURVEY.md: liblzma 0BSD/5.8.4/pinned-sha + rest).
  GATE-9433954's "(1) OPEN — oss-survey lane owns" predates it; gate-1 now awaits parent MERGE, not
  authoring. (2) RED held by FLAG (w1 fix + re-gate); (3) parent's call. Viewer part of 008: DONE.
- FLAG-w1-lzma-b0-hold ACKED (sweep-owned, BLOCKS merge): my VERIFY-1c729f1/9433954 stand as
  code-verification (honest/clean/A-20-compliant); the b0=2 gap is an unbedded RULE case for w1's fix
  (py+C shared logic), not a wall/hygiene issue. Sweep's MINIMAL-fitting-header hypothesis is the lead.
- read: FLAG + NOTE-RED (m4m deterministic b0 02-vs-03 +4B cascade, 50B bracket — crisp exhibit),
  GATE-9433954 (RED concurs; framework legs all green incl LZMA-C identical SHAs), GATE-15ef0e5
  (PASS concurs my VERIFY ✓), NOTE-w2s4-10 (raven tail-fields R1-R4 + A-22 ack, Q-20 closed-except-fork).
- state: Q/A 22/22, all tips verified (w1=9433954 RED-held, w2=15ef0e5). no DONE anywhere. claim HELD.
