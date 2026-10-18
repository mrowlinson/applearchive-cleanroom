# NOTE-RED 239a401: FAIL per PARENT-005 (tmp/scratch-* in tip) — behavior GREEN 71/71

- RED CAUSE (hygiene, state-based): tip carries
  tmp/scratch-encode2/* (probes + RESULTS). PARENT-005
  (filed ~2min AFTER this tip): rm -r --cached
  tmp/scratch-* next commit; repeats FAIL. -> FAIL per the
  new gate rule (live-fired same turn). TIMING: tip
  predates rule — NO writer fault; fix-forward + re-gate.
- BEHAVIOR all green first-hand (pristine extract): OUTER2
  71/71 (+8 m-rb cells), PINS-OUTER2 set-eq 71/71, SMOKE
  6/6, CONTAM 0, OSS none, ADOPT match. covers 285196e
  within (same poll gap, never observed as tip).
- claims corroborated: fresh m-rb-lzraven-z1k sha
  3d1a9c7f... MATCH pin; battery-vs-bed sizes EQ (212/
  1249/256/246/758); NOTE-w2-9 payload numbers EXACT from
  committed beds (r100 comps 292/288/237, xz magic x6,
  bv41 lead, 785e lead). probe-rb.sh read: black-box
  aa-only + ALGS param; battery diff (+8 m-rb) same
  established pattern, honest chk.
- verdict: RED (hygiene FAIL). merge BLOCKED by
  FLAG-w2-tmp-cleanup until rm --cached + re-gate.
  behavior needs NO rework.
- repro: sh lanes/encode-sweep#2b177a2:tests/gate-tip.sh
  239a401 $WS/gate-w2-239a401
