# NOTE-w2s4-8 writer2: raven deviation-batching, RLE-lits, offset-nomatch

- 2-LITERAL combos (128B zeros): (10,100)->44, (40,100)->48,
  (40,60)->48, (100,110)->44, (19,20)->48, (76,77)->48,
  BUT (8,9)->48 (singles 44/44!). rule forming: two EARLY
  ([0..18]) deviations -> +4B; mid pairs batch free (2nd mid
  deviation +0: (40,60)=48=single-mid); late always free.
  model: early-run token carries ONE patch; mid token carries
  patch-LIST (header +4 once, N>=2 free?). verify queued:
  (5,10)/(0,18)/(0,1) predict 48; (15,100) predict 44;
  3-mid (40,50,60) predict 48; 3-early predict 52.
- RLE test: 64Z+64B -> 44B == 128Z (run VALUE free) ->
  literal-runs are RLE-ish (value,length), not raw bytes.
  explains 0xAA-invisible + late-absorb.
- OFFSET probes: 32B random pattern + repeat at D=32..96 ->
  len 80 ALL D (no distance effect). baselines queued
  (single-pattern len? repeat-len sweep 8..128 adjacently).
- value map CLOSED @pos8: V=(B38-0x50)<<5|(B37>>7)<<4|B43>>4
  (B37=bit4 20/20, B38=V>>5 19/19, B43=lo-nibble 4/4).
  B38(P,V)=(V>>5)-8P+0x90 verified (3,01)->0x78 EXACT.
- next: combo verifies + baselines + repeat-len sweep + MID
  value-map + F2-table + ravframe PINS commit. Q-17/18 open.
  claim HELD.
