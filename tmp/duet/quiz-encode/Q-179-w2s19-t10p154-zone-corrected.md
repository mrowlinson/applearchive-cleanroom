# Q-179 (w2s19): T10P154 P-head geometry @70329 — CORRECTED (proper zeros-N bed)

Own census 70329..70460 (132 .rav, census.sh
zeros-N, first-hand). Supersedes refuted Q-178
legs (writer bed bug: 37B-pattern inputs +
raw[8:12] sig slice; both fixed, taint purged,
recipe now census.sh):

1. shape? 70329 100B/84B sig 03000000 (PB0);
   70330 100B/84B fat sig 71070000 NEW; PBA
   70331..70346 sig 1e770000 NEW; NO extra
   singleton; PBB10 70347..70356 sig b8030000
   NEW; QUAD 70357..70420 single sig 8c3a0000
   NEW. 92x100B exact. PBA VPOS [4,20,21,
   76-79] (b5 const 0x25); PBB VPOS [4,20-26,
   80-83] (11B M, b5 0x25). confirm?
2. quad rows? M 7B pos[19,26,27,76,77,78,79]
   row-indep 16/16 x4, 16/16 distinct each row
   (heads 14/16 distinct each row). R-band 6B
   b20-25 row-only: rows0==1 exact 785f23d89006
   (0==1 pairing); row2 49dd948990f8; row3
   9c5b5fbd7092, 64/64. tails b80..83 row-const
   ALL distinct 6d382166/b7382166/112daaaf/
   f2331b1a. M-novelty vs P153M tails: ALL NEW
   (0/16). PBA M 6B 16/16; PBB M 11B 10/10.
   confirm?
3. counters + dips? pay[4:6]==LE((n<<1)|1)&FFFF
   all 92 cells. b5 const 0x25 PBA/PBB; quad
   0x25->0x26 step exactly at 70400 (70399=25,
   70400=26; row2 spans). varpos partitioned
   exact (PBA 7=b4+6tab; PBB 12=b4+11tab; quad
   19=b4+b5+R6+M7+tails), 0 stragglers. any
   D-class dips? next tier @70421 sig 94890300?
