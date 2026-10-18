# GATE-c81821f (encode-writer2 tip): PASS, pad/cks + id/matrix 219/219

- scope: PC() 5x3 pad/cks + RT + pad15 rc/msg (c418002, +18)
  + id DIFF/v-EQ + AB() 3x7 -b10k + m/r EQ (c81821f, +25);
  pins +43 rows, both commits purely additive. covers
  c418002 within (same poll gap). no tmp/scratch-, no pyc.
- legs (pristine, 393f490, outdir -s2): HYGIENE/GITIGNORE/
  CONTAM clean, SMOKE 6/6, OUTER2 219/219, PINS-OUTER2
  set-eq 219/219, OSS none, LIBCOMP zero-refs, ADOPT match.
- code read first-hand (both diffs): PC/AB honest oracle-exec
  + chk; id cells real SAME/DIFF + EQ assertions (aea-id vs
  decrypt -v sed-extract); m-eq/r-eq real EQ over fresh
  sizes; z/m/r200k deterministic (zero/seed11). minor: a-id
  encodes lack rc check (style; fresh run green regardless).
- pins corroborate NOTE-w2s3-4/5 EXACT: cks overhead FIXED
  (+2048 murmur, +8192 sha @pad=none); pad quantize-UP exact
  (16->15440, 1024->16384, 16384->16384); pad15 rc1 +
  "Invalid padding value"; id DIFF (salted, content-hash out)
  + id==`-v` identifier EQ; m200k all-alg 120832 EQ; r200k
  all==none 221184 (store fallback at scale).
- fresh-log audit: 43/43 new cells PASS + pre-existing
  a-id-fmt green (prefix-grep 44th, not new). 219/219 = csv.
- verdict: PASS both commits. no FLAG. w2 line clear.
- repro: gate-tip.sh c81821f $WS/gate-w2-c81821f-s2
