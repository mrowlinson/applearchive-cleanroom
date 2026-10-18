# Q-15 w2: AEA encode -a codec matrix + seg-alg IDs (granted AEA turf)

- context: w2 granted AEA-ENCRYPT beds (A-7(3)); AEA -t/-b SIZE
  matrices done (fb9d88b/0661787, GATE-PASS). PRE-001 OPEN list:
  "seg-alg IDs on encode" unbedded. predecessor bedded -a none +
  lzfse only (size effects), never the codec set or envelope IDs.
- Q: (a) which -a values does AEA encode accept (same 7 as AAR
  outer: none/lzma/lz4/zlib/lzfse/raven/bitmap?), (b) where in the
  AEA envelope does the per-segment codec choice manifest (byte
  offset/field, stable across reruns?), (c) does an unaccepted -a
  error or fall back (exact stderr/exit)?
- behavior-only; w2 beds in parallel regardless (oracle exec).
  pins the AEA codec leg of w2's battery.
