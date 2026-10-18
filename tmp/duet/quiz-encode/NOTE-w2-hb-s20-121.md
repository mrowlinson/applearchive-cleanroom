# NOTE-w2-hb-s20-121 — P261 ANALYZER GREEN
bump-20
- P261 CENSUS: 107565..107912 348 cells missing 0 RC=0
- ANALYZER: GREEN P261 348/348 (M-tails novelty in log)
- sigs: PB0 0f550300 NEW/PB1 adecad06 NEW/PBA e08ad76e x16/B10 35fda506 x10/QUAD e08ad76e x64(==PBA)/T88 06000000 x256(==P252/253/256/259T)
- PBA: M8 b24-27,76-79 V9 C75 b5-const 48
- B10: single-sig M12 b24-31,80-83 V13 C71 b5-const 48
- QUAD: QM8 b21-23,31,76-79; R7 b24-30 r0==r2 EVEN-PAIRED 3/4 (r1,r3 distinct); tails 4/4 (r0/r2 sha a0e666); b5-carry 48->49 @107647->107648; V21 C63
- T88: STANDARD M7 b40-42,76-79 cols / R8 b25-27,35,80-83 rows 16/16; b5 49+steps[119,247]; V17 C71
- NEXT: stage p261-patch -> try-p261 -> sweep 348/348 -> Q-325
