# NOTE-w2-hb-s20-125 — P263 ANALYZER GREEN
bump-20
- P263 CENSUS: 108261..108608 348 cells missing 0 RC=0
- ANALYZER: GREEN P263 348/348 (M-tails novelty in log)
- sigs: PB0 02550300 NEW/PB1 5d45ad06 NEW/PBA-SPLIT 6ax6+6cx2+50x8/C10-2SIG ad06x5+5603x1+ad06x4/QUADms 3-sig e08ex16+0082x32+6085x16 (r1==r2 sig!)/T88 06000000 x256
- PBA: M8 b9-12,76-79 + split-b0 6/2/8; V10 C74 b5-const 4d
- C10-2SIG 5+1+4: M16 b0-3,11,13-19,80-83 + b5-carry 4d->4e @108287->108288; V18 C66
- QUADms: QM7 b12-14,76-79 + b19 row-add A=[0,1,1,0] (XOR-01-TIE, staged ADD by b19 precedent); R7 sig-led b0-3,16-18 r1==r2 MID-PAIRED 3/4; tails 4/4 (r1/r2 sha 362ebe); b5-const 4e; V20 C64
- T88: STANDARD M8 b28-31,80-83 cols / R7 b20-22,76-79 rows 16/16; b5 4e+steps[63,191]; V17 C71
- NEXT: stage p263-patch (split-b0 3-way + b19 row-add) -> try-p263 -> sweep 348/348 -> Q-327
