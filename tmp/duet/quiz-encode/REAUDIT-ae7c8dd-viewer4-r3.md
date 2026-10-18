# REAUDIT-ae7c8dd-viewer4-r3: band172 T10P128 (n<=61372, 816 tiers) — PASS

Interim re-audit (turf starved: 166/169/172/175/178 VERIFY-complete,
181 uncut). Post-GATE first-hand re-confirm of r1 VERIFY: GATE-ae7c8dd
landed during r2, after r1's pre-GATE VERIFY.

First-hand in WS detached tree
WS/tmp/encode-viewer4/reaudit-ae7c8dd/tree
(detached HEAD ae7c8dd), seat-private
build .../reaudit-ae7c8dd/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1844280 bytes — same size as r1; PINS 7780 + 2 header).

- PYID (RGRAMC=own C, seeded oracle corpus, all comparisons fresh):
  RGRAMC-PYID 3890/3890 covered=3890/3890, RGRAMC-GREEN, rc=0.
- CBAT (RGRAM_BIN=own C, fresh oracle): 7780 PASS / 0 FAIL,
  RGRAM-GREEN, rc=0, tail g-z61372.
- PYBAT (python impl, same suite, fresh oracle): 7780 PASS /
  0 FAIL, RGRAM-GREEN, rc=0, tail g-z61372.
- Own-loop fresh-oracle 61117..61372: pass=256 fail=0 pins=20
  pinfail=0, OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band diff (src/c/rgramc.c only,
  +1481/-1001; cpat|libcompression|depload|dlopen|dylib): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in lane diff).

VERDICT: PASS — confirms r1 VERIFY + GATE-ae7c8dd PASS-functional.
Trees + logs retained under WS tmp/encode-viewer4/reaudit-ae7c8dd/.
Not a counted VERIFY (no new band); run VERIFY total stays 0/4.
