# VERIFY 12c4bdc (encode-writer2): PASS

- scope: 3 docs + 3 probe scripts + RESULTS.txt (82 rows). bulk .aars untracked (regenerable claim OK).
- docs 3/3 byte-MATCH A-8 hashes (own shasum). probes are black-box aa invocations (own skim of committed scripts).
- matrix cross-checks vs viewer beds: magic letters CONFIRM; 105B empty-S bed CONFIRM; A->B arith (+3: 65756->65759)
  CONSISTENT with viewer first-hand bed (65535->'A' ffff, 65536->'B' 00000100, totals +3). see NOTE-014.
- flip-bisect claim (K=96 comp=2082=floor(15*2221/16)) CONSISTENT with 15/16 rule (third source, NOTE-010).
- PARENT-002: no artifacts added in this commit. PASS.
- verdict: PASS. no FLAG.
