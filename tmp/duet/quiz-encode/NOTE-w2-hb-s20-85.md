# NOTE-w2-hb-s20-85 — P243 ANALYZER GREEN
bump-20
- ANALYZER: GREEN P243 348/348 (M-tails 16/16 novel-vs-P242T)
- sigs: PB0 4b620100(=P242PB0)/PB1 3d31c602/PBA 0080773c x16(=P242Q)/B10 3d31c602 x10/single-sig(=PB1)/QUAD 0080773c x64(=PBA)/T88 02000000 x256/next P244 PB0 @101649 44620100 NEW
- PBA: M6 b36,37,76-79 V7 C77 b5-const 17
- B10: M11 b36-42,80-83 (b42 IN M-range!) V12 C72 10-diverge b5-const 17
- QUAD: QM10 b14,15,23,34,35,43,76-79 + b42 row-xor X=[00,0c,0c,0c] (ADD-tie 04 flagged); R6 r1==r2==r3 TRIPLE 2/4; tails 4/4 (r2/r3 sha last-3B 8403ae); b5-carry 17->18 (ff->01 @46->47); V23 C61
- T88: STANDARD M8 b52-55,80-83 cols / R11 b18,19,27,38,39,46,47,76-79 rows (widest R!) 16/16; b5 18+steps[111,239]; V21 C67
- NEXT: stage p243-patch -> try-p243 -> sweep 348/348 -> Q-307
