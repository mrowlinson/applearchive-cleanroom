# NOTE-w2s11-hb16: P51 battery running, R50 derived

- P51 (34485..34512, 28 cells) implemented, probe 28/28;
  for-list extended; RECORD+battery+smoke running in background.
- R50 = 34513..34832 (320, 80B) dumped + derived read-only: A
  4x16 (q-rows own heads 07/07/06/07; m-tab b41,42,76-79;
  q-tab b0,10,11,33,34,35,72-75; b40 = QB40[q] | 0x80 iff m
  in {1,2,6,10,12}, QB40=(54,52,55,53)) + B 16x16 (m-tab
  b37,38,46,47,68-71, q-tab b40,41,76-79); RAW 320/320.
- P52 @34833 (76B, head 9a1ff701).
- Next: commit P51 on GREEN, then R50 tables + probe.
