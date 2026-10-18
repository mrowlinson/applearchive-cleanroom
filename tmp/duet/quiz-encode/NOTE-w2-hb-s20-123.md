# NOTE-w2-hb-s20-123 — P262 ANALYZER GREEN
bump-20
- P262 CENSUS: 107913..108260 348 cells missing 0 RC=0
- ANALYZER: GREEN P262 348/348 (M-tails novelty in log)
- sigs: PB0 0a550300 NEW/PB1 35fda506(==P261B10)/PBA e08ad76e x16(==P261PBA)/C10-2SIG a506x5+5503x1+a506x4 sandwich/QUAD e08ad76e x64(==PBA)/T88 06000000 x256
- PBA: M9 b15,34,35,42,43,76-79 V10 C74 b5-const 4b
- C10-2SIG 5+1+4: M15 b2,3,34,35,41-47,80-83 V16 C68 b5-const 4b
- QUAD: QM6 b48,49,76-79; R8 b34,35,41-46 r1==r2 PAIRED 3/4 (r0,r3 distinct); tails 4/4 (r1/r2 sha c02fdf); b5-const 4b; V19 C65
- T88: STANDARD M6 b6,7,76-79 cols / R6 b52,53,80-83 rows 16/16; b5 4b+steps[27,155]; V14 C74 (smallest T yet!)
- NEXT: stage p262-patch -> try-p262 -> sweep 348/348 -> Q-326
