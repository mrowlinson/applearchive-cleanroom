# REAUDIT-fac36c9-viewer4-r8: band189 T10R134 (n<=64412, 850 tiers) — PASS

Second independent first-hand battery (viewer-r15
filed unsuffixed REAUDIT-fac36c9 PASS 14:59 on older
claim 14:18:53 vs mine 14:19:36 — this filing suffixed
per PARENT-070/071 + d1a3c2d precedent, not a contest;
their file untouched). First-hand in fresh WS detached
tree .../reaudit-fac36c9/tree (git archive fac36c9, full
SHA fac36c9bcc3270170a9edb3e420d25da6eb5a163 == VERIFY),
seat-private build .../build/rgramc (cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings, 1929880 bytes == VERIFY == GATE).

- PYID (RGRAMC=own r8, corpus 8152 own-seat hardlinks
  from r7 b187 cache = 4076 N + 25 fresh-oracle new N,
  py+C freshly executed per pin): RGRAMC-PYID 4101/4101
  covered=4101/4101, RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r8, fresh oracle): 8202 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z64412.
- PYBAT (python impl, fresh oracle): 8202 PASS / 0 FAIL,
  RGRAM-GREEN, rc=0, tail g-z64412.
- PINS-RGRAM set-eq 8202/8202 (C/PY PASS-name sets
  cmp-identical, both all-PASS).
- Own-loop fresh-oracle 64157..64412: pass=256 fail=0
  pins=11 pinfail=0, OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE/VERIFY/viewer-r15 report
  22/22 = 11x2 closed+sha — same 11 cells, pinfail=0.)
- Tables-EQ own script r8: NEW 3/3 EQ (_T10R134C/M/Q);
  FULL 2290/2290 0-skip 0-mismatch. (Script-scope note:
  r8 enumerates STRARR tables where r15 counts NEW 2/2 /
  FULL 1261; both 0-mismatch, conventions differ only.)
- Wall-grep PARENT-032 scope on band diff vs d335153
  (src/c/rgramc.c only, +1220/-1061 == GATE,
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
  py+PINS+tests cmp-SAME d335153; PINS 8204 lines
  (8202+2hdr). HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands; agrees with
viewer-r15 on every leg modulo table/pin-count
conventions). No commits, no push.
