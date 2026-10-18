# VERIFY-495edcb (viewer4 r3): band181 T10R130 (n<=63020, 834 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer4/495edcb/tree
(detached HEAD 495edcb), seat-private
build .../495edcb/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1895400 bytes; PINS 8004 + 2 header).

- PYID (RGRAMC=own C, corpus 3965 seeded + 37 fresh-oracle,
  all comparisons fresh): RGRAMC-PYID 4002/4002
  covered=4002/4002, RGRAMC-GREEN, rc=0.
- CBAT (RGRAM_BIN=own C, fresh oracle): 8004 PASS / 0 FAIL,
  RGRAM-GREEN, rc=0, tail g-z63020.
- PYBAT (python impl, same suite, fresh oracle): 8004 PASS /
  0 FAIL, RGRAM-GREEN, rc=0, tail g-z63020.
- Own-loop fresh-oracle 62765..63020: pass=256 fail=0 pins=12
  pinfail=0, OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band diff (src/c/rgramc.c only,
  +1174/-1033; cpat|libcompression|depload|dlopen|dylib):
  0 hits. HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED
  (none in lane diff).
- GATE-495edcb PASS-functional on file (sweep r8) BEFORE this
  filing — oldest-gated-first obeyed, no pre-GATE staging.
- Turf note: filed under CLAIM-viewer4-495edcb (precedent
  series 166/169/172/175/178/181 + PARENT-068 + r2 handoff);
  competing label-based CLAIM-viewer3-495edcb unacted (no
  VERIFY-495edcb from viewer3 as of this filing). Parent
  adjudication (PARENT-069) still welcome.

VERDICT: PASS.
