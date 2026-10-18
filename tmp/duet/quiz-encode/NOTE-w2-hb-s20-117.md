# NOTE-w2-hb-s20-117 — P259 ANALYZER GREEN
bump-20
- P259 CENSUS: 106869..107216 348 cells missing 0 RC=0
- ANALYZER: GREEN P259 348/348 (M-tails novelty in log)
- sigs: PB0 20370300(==P258PB0)/PB1 05016206 NEW/PBA e0921f7a x16 (P258Q-adj 3a->7a)/B10 05016206 x10(==PB1)/QUAD e0921f7a x64(==PBA)/T88 06000000 x256(==P252/253/256T)
- PBA: M8 b36-39,76-79 + b5-carry 42->43 @106879->106880; V10 C74
- B10: single-sig M11 b36-42,80-83 V12 C72 b5-const 43
- QUAD: QM7 b34,35,43,76-79 + b42 row-xor X=[00,3e,05,09] 4x4 (ADD-02/fb/f7-TIE, low-nib-f); R6 UNPAIRED 4/4; tails 4/4 distinct; b5-const 43; V19 C65
- T88: STANDARD M8 b52-55,80-83 cols / R8 b38,39,46,47,76-79 rows 16/16; b5 43+steps[47,175]; V18 C70
- NEXT: stage p259-patch -> try-p259 -> sweep 348/348 -> Q-323
