# A-29 T3 combs = tail value-holes at stride-64 placements (no separate field) (Q-26)

## teeth couple to tail-d, N-independent (identical @N=760/780/800)
- d=24 -> flips 89; d=20/19 -> flips 128; d=18 -> flips 153+128; d=9 -> flips 25.
  27/32 tail-d leave all teeth untouched. mapping is D-based, not position-based.
- tooth 192: NO single-dev owner in d=1..64 (open micro: deeper-d or multi-dev).
- tooth 64: no tail owner either (skeleton-only in this tier? also open).

## zeros-N behavior (full tier 512..820, all pl=352)
- teeth 89/192 CONSTANT 0 across all 309 (neighbors 88/90/191/193 constant too —
  no indexing drift; numbering cross-confirmed repeatedly).
- active teeth: 64 on@730+, 25 windowed 731..756, 153 on@748+, 128 oscillating
  (750-756 chatter, then 16-on/16-off blocks @773/789/805: period-32, duty 1/2).
- 25/153/64/128 = DUAL-USE (skeleton bits doubling as holes for d=9/18/19/20);
  89 = PURE hole (content-only, invisible in zeros-N).

## answer to Q-26
- NO field "advances with period-64 stride" — the combs ARE tail value-hole slots
  whose PLACEMENTS happen at d=64 spacing. the stride is in hole allocation, and the
  middle teeth are content-only (which is why zeros-N shows 4/6).
- puzzle for w2: if their varying-set is zeros-N-only, 89/192 cannot be in it (my
  309/309 constant). their combs likely union dev-dumps (holes entering via content).
  worth one line confirming dump family — decides whether ANY zeros-N-varying tooth
  sits at 89/192 (my data: no).
- discriminator delivered: dev@(N-24) lights 89; dev@(N-9) flips 25; dev@(N-1..8
  except listed) transparent — phase/shift knobs per tooth.
