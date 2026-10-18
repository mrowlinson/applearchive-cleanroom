# A-37 Q-30 FINAL (attempt#5): 4 minimized mate SETS + hash reads bytes 4-7

## bed (PH1-shape, exact recipe)
- PRE = 108B seed-51 random; T = PRE[100:108] = 94dd1fa95673375c.
- filler = 12000B (1500 x 8B grams); TAIL = 2000 zeros. outcome @T-pos:
  FIRES / MISS / COVER (cover = swallowed by earlier match — artifact).
- minimize: neutral-gram substitution (NEU=645906c8947cc6ad, verified
  inert single) keeps layout fixed; greedy drop-one to minimal.

## the 4 sets (hex, gram-index in 1500-filler, N = distinct count)
- set0 N=6: [819]f570a094b074e265 [898]4300e389383db78e
  [1009]ce758bd9ebb8a47e [1010]01189482f12eef0a [1350]f5ec9105456d76e7
  [1423]432e268e75a59d8a
- set1 N=8: 8e9a102abe008eea 7820194fc52dc52d 1d66d118bf6c9763
  27112360a0437dfe f0aa89473a25f658 e0fcaeb1f6075f2d 638d1932ac62aa22
  66ad6f516c007f4c
- set2 N=6: 47487a9587b2b863 a16af22a57acea1a c764adc96b70713b
  02507593c9f84a0b 72d863be3f6c438d 9fee2205ade732b4
- set3 N=9: 9ce3a4bd560529d2 5e6aeed2f0977fc9 8fe36282a3b597d7
  5c0c8fd92ebe92ac ae159ebab6fb7eee 5d5a66f8cbb86732 1c31c4492162bb15
  f610fb16e30c75f1 202d17b5fa0b6439
- (set1-3 gram indices in v5q30d.log; construction seeds 1102/1200/1301.)

## proofs (all first-hand)
- load-bearing: every drop-one → FIRES (29/29 across sets). full set → MISS.
- identity: every mate x2-3 random substitutes → FIRES (set0 18/18,
  set1 16/16, set2 12/12, set3 18/18). zero hitchhikers by this test.
- singles: 6/6 FIRES alone (singles never evict ✓ CR-129 0/9200).
- N /\ S-tension (REPORTED, not resolved): minimal N = 6/8/6/9, all
  identity-specific — MORE than S=5 predicts for pure 1-bucket overflow.
  candidates: (a) S up to 9, (b) T residence spans 2+ buckets (overlapping
  inserts), (c) 1+ mechanism pieces (refresh-kill). fit accordingly.

## mutant panel (set0 mate0 f570a094b074e265, xor-01 per byte)
- pos0-3 → MISS (stay lethal, same bucket); pos4-7 → FIRES (left bucket).
- verdict: hash sensitivity lives in bytes 4-7 of the aligned 8-window;
  bytes 0-3 INERT. readings: (a) hash over last-4, or (b) killing insert
  is the +4-shifted window. sharpest hashmode evidence in this answer.

## fit recommendation
- fit hash functions maximizing co-bucketing of each SET with T (not
  pairs — pairs cannot evict, A-36 interim). weight set0 highest (N=6
  minimal + full panels). hashmode must reproduce the 4-7/0-3 split.
- dual-seat: attempt#6 may file own A-36/37 — compare hexes; mine are
  the -attempt5-/-pairs5- files. Q-30 CLOSED by this answer (from my seat).
