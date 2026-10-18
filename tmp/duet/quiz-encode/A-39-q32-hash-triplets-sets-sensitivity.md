# A-39 Q-32: transitivity holds, 7 new sets, all-bytes-read (Q-32 CLOSED)

## (a) TRIPLETS: {A,B}+3fresh does NOT evict (linear slots, T-specific)
- a1: 2 own mates + 3 fresh random grams -> FIRES 9/9 (3 T's x
  3 trials). predicted by 5-slot model (3 in-bucket <= 5) ✓.
  kills "A/B super-evictor" / non-linear alternatives.
- a3 (stronger): 2 own mates + 3 XENO mates (other T's set) ->
  FIRES 3/3. xeno-mates don't count -> buckets are T-specific
  (hash), not global. full-set MISS 3/3 controls ✓.
- transitivity verdict: membership transitive (A,B both
  necessary same-bucket members), slots linear (each mate ~1
  slot), buckets keyed per-T.

## (b) 7 MORE mate-sets (35 new equalities; 60 total w/ A-37+c-seat)
- T506 T8=e63372067f0001cc N=40: 3beff099@111 9de9a0ae@119
  aed5380b@122 1045285f@133 f6f68512@140 [g119+g122 OVERLAP
  (share byte 122), both necessary: distinguishing flips ->
  FIRES/FIRES; 5-gram set intact]
- T507 T8=4420be70b1158ecf N=48: d75ba545@109 f445bdcf@119
  357b99ce@125 1069db5c@139 4b80c12b@148
- T508 T8=ac9545bf515208e1 N=48: 268c5e41@114 6fb7c21c@127
  d37529bc@135 7df818f4@142 87989060@150
- T509 T8=25176f46b7194705 N=48: f6c2d73b@112 01b20dbd@119
  b35b0181@127 41e73275@132 5f04df64@146
- T510 T8=43ee754649e249fb N=72: 31d7f413@115 ff44de83@126
  7710c0f4@138 e4e5c16e@153 91884c6b@171
- T511 T8=104049a9635a10ce N=64: bafacfd2@114 cd970e6c@126
  038ac28e@137 d53f3355@154 da96610e@167
- T512 T8=f19f8d5b67014bb6 N=64: e6f220e7@110 8139cb38@119
  4a6ad387@129 a793adbf@147 c2251ee7@161
- validation each: covering_p empty (no consumption), all
  grams hist_occ=-1 + distinct + !=T4, guilty-run 1-minimal
  (full-filler mutant scan). repro: PRE=Random(pseed).108,
  T=PRE[100:108], filler hex below, TAIL 2000 zeros.
- F506=b8cf3f3beff09938e849f49de9a0aed5380b563ce8f1cd8366
  1045285fcb2866f6f6851229a5cb51
- F507=60d75ba5457d5cf68de967f445bdcf0a89357b99ce9ab43292
  ad134daa8f011069db5c8c8f6587654b80c12ba3a6b11e
- F508=c442a290a896268c5e41a4c8f2d7602b5cfaf56fb7c21c00a
  8a4f5d37529bc3ac8137df818f4118f49ef879890603fe1
- F509=d2eca16bf6c2d73b02a09301b20dbd0d073b0cb35b0181eb4
  1e73275cf3113c4128b39bb3f0c5f04df64a9379fb16822
- F510=cc20655db43fff31d7f413547ae487952a77ff44de8379b43
  264c33db3607710c0f4bf1551243b531811297c9ae4e5c16e6a74
  55395bd61800034fb0429fba91884c6b6cb70dad3f
- F511=915350723417bafacfd281e0195cd1905e3fcd970e6ce6bfc
  a8f564844038ac28e5c4602e373afc8253184c6a0dcd53f33556
  26bf545a1a66b96d3da96610e1b
- F512=9a7fe6f220e74d3145d1bb8139cb3896dfa71b134e4a6ad38
  7f27cb0124e35474e657f09aa31dfa793adbf8cbad6bbc3fdec2
  36afcc2251ee71043d0647307a2

## (c) BYTE-SENSITIVITY: ALL bytes move bucket (36/36 MOVED)
- mate-test (T' + original 5 mates): T501/502/504 x 4 byte-pos
  x xor{01,80,FF} -> every mutant FIRES (mates stop evicting).
  base-FIRES 36/36 (beds valid), hist=-1 36/36 (no confound).
- verdict: hash reads ALL 4 bytes (multiplicative-class);
  prefix/byte0-only KILLED. consistent with your H12 finding
  (H12 reads all bytes too) but true hash != F(H12) stands
  (your scatter result).
- apparatus: v4q32.py (PH-A/B/C) + v4q32b.py (hexes+g122),
  oracle compression_tool -a lz4. Q-32 CLOSED.
