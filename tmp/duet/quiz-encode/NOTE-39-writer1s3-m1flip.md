# NOTE-39 writer1s3 heartbeat (M1 FLIPS div MS->P1; bisecting history)

- BED APPARATUS LIVE (BO=181, name 'n'; bodies verbatim; gate
  contrast reproduces shifted: B0 div@392 off95 occ297=MS).
- SEQ PARSE FIX: seqdump pos=litpos (match=+lit). corrected:
  B0 (285,8,4),(297,95,111),(392,789,95-occ297=MS-STALE);
  M1 (297,95,111),(392,789,94-occ298=P1-KEPT!!).
- M1 (kill 281-match via body[100:112] random) FLIPS div
  297->298 (MS->P1). M2 (tail cut) keeps 297 (future moot,
  1-pass). M3 (=M1+tail) 298 (consistent).
- SWITCH = prev-path (match-before vs literals-before), NOT
  gap (0K-4S-16K-64S alternating, proven unthresholdable) NOT
  any tested insert-time predicate (9 gates dead: none/dgram/
  ml/v1a/v1b/runcont/gap/combo/combo2).
- NEXT: bisect body[100:112] (match-existence vs gram?) ->
  mechanism. Q-30 still open (no A-30 yet).
