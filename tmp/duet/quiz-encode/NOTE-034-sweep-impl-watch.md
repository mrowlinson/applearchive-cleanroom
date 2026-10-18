# NOTE-034 sweep: all quizmates read, IMPL watch armed, polling

- read: VERIFY-ac38c8a (concurs GATE-ac38c8a incl p0-DIFF
  honesty ✓), A-16 (libzbitmap READ granted read-only;
  sweep instruction: load-scan unchanged, first copied
  byte w/o nomination = violation), PRE-003 (Apple
  encoder OSS NONE-FOUND), NOTE-033/034/035-viewer,
  NOTE-w2s3-7/8 (IMPL plan: src/rb2.py + test_rb2.sh next).
- IMPL-gate checklist armed for rb2.py commits: (1) A-16
  provenance cites (OSS files read) in commit/note;
  (2) no OSS bytes (hand-written; load-scan + read-through);
  (3) PARENT-003 survey-naming already in A-16; (4) LIBCOMP
  deny per PARENT-007; (5) SMOKE-IMPL legs when adapters land.
- coverage: 21/21 gated, ZERO holds. no DONE anywhere.
