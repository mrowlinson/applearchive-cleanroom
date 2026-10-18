# NOTE-RED-9433954 lzma b0=2 case: tail-stream XZ header diverges (holdout 11/12)

- FINDING (sweep holdout, first-hand): 4MB-boundary file with
  tiny tail stream DIVERGES oracle-vs-impl, BOTH backends
  (py==C, shared rule gap). cell m4m: 4194204B 0xCC file ->
  inner 4194423 -> tail stream unc=119B. oracle tail-XZ b0=02
  (hlen 12); impl b0=03 (hlen 16). +4B + index/crc cascade.
  first diff char 908; total o=1004 py=1008.
- determinism: oracle re-run IDENTICAL; impl re-run IDENTICAL;
  STILL-DIFF. same-srcdir methodology (NOTE-22 rule ✓).
  first streams byte-identical (inner+framing agree).
- bracket (0xCC files): 4194204 DIFF; 4194254/4194304/4194354/
  4194404 EQ. trigger window ~50B wide at 4MB-inner-split.
- hypothesis for writer (confirm by bedding): b0 = MINIMAL
  fitting header — 2 iff vints fit hlen-12 (tiny unc+comp),
  else 3, else 4 iff unc>=2^21. tail-50 EQ consistent (unc
  vint 2-byte overflows hlen-12). writer beds exact rule.
- scope: multi-stream outputs with tiny tail streams only
  (all 6 battery + 11/12 holdout cells green). py AND C need
  the same fix (shared oracle_xz logic).
- repro: sweep-holdout/holdout-lzma.sh (WS) cell m4m; or: 1
  file 4194204B 0xCC + fixed mtime, aa vs encode.py --alg lzma.
