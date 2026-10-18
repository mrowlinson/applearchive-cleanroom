# REAUDIT-9afecce (viewer2 r5): band174 T10P129 — PASS

Interim re-confirm of filed VERIFY-9afecce (turf-starved
wait; viewer4-r3/r4 precedent). Full 5-leg first-hand
re-battery in existing detached tree WS
tmp/encode-viewer2/9afecce/tree (HEAD 9afecce98a2d6b2
confirmed, status clean), fresh seat-private build
re-r5/rgramc-own (cc -O2 -Wall -Wextra -std=c11 rc=0,
0 warnings, 1861176 bytes — byte-identical size to
filed VERIFY build).

- RGRAMC-PYID 3915/3915 covered=3915/3915 GREEN rc=0
  (fresh-oracle corpus, 0 FAIL).
- C-leg RGRAM-GREEN 7830 PASS / 0 FAIL rc=0.
- py-leg RGRAM-GREEN 7830 PASS / 0 FAIL rc=0.
- own-loop fresh-oracle 61629..61720: 92/0 (py+C agree
  CLOSED all 92, rc+stdout+stderr identical); pins
  26/26 (13 pinned cells x closed+sha, fresh .rav
  hashes match PINS).
- PINS 7832 lines; lane-diff rgramc.c-only +1470/-1007
  (reconfirmed); tables 60 T10P129 lines (matches filed
  VERIFY); wall-grep PARENT-032 scope 0 hits.

Verdict: PASS (re-confirmed). No commits, no push.
