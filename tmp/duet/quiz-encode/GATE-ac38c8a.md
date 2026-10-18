# GATE-ac38c8a (encode-writer2 tip): PASS, AEA edges 252/252

- scope: NDP() nd-p0/2/3/4 + EB() lenient -b/-t + RT +
  VB() -v block echo x4 + SIGN() p1/p0/p2/un2 matrix,
  pins +33 rows, purely additive (64+/0-, 33+/0-).
  no tmp/scratch-, no pyc, no impl.
- legs (pristine, NEW framework ff42363 live-fire, cwd
  outside repo): HYGIENE/GITIGNORE/CONTAM clean, SMOKE
  6/6, OUTER2 252/252, PINS-OUTER2 set-eq 252/252, OSS
  none, LIBCOMP zero-refs, ADOPT match.
- code read first-hand: NDP dual-encrypt + cmp char (p0
  verdict-only DIFF — ECDSA-unstable c14/16/17 disclosed
  in comment, honest nondet handling); EB rc+size + RT;
  VB sed-extracts full `compression:` echo; SIGN rc/msg/
  SAME-MOD + RT roundtrips. all fresh-oracle + chk.
- pins corroborate NOTE-w2s3-6 EXACT: nd p2=c13 p3=c14
  p4=c13 (p1=c13 known); -b 0/bogus/129m + -t 0 ALL rc0
  + RT-OK (LENIENT vs AAR strict); -v floors "0 MB"
  16b/64k, exact 1/128 MB; p1 rc1/msg/SAME; p0 rc0/MOD/
  RT-OK; p2a/p2b rc1 pair-msgs; deferred flow rc0 -> undec
  rc1 "Failed to unlock container" -> sign rc0 MOD -> RT-OK.
- note: NOTE-w2s3-6 "p0=c14" was one observation; pin DIFF
  records the stable cross-run verdict (code discloses
  c14/16/17) — reviewed, honest, no contradiction.
- verdict: PASS. no FLAG. w2 line clear.
- repro: gate-tip.sh ac38c8a $WS/gate-w2-ac38c8a-s2
