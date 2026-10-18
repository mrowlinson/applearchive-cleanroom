# NOTE-w2s11-hb03: R43 battery running, P45 derived

- R43 (32141..32396) implemented, probe 256/256; for-list extended;
  RECORD+battery+smoke running in background.
- P45 = 32397..32488 (92, 76B); 32489 breaks to 80B pay (next
  tier new geometry).
- P45 derived read-only: RAW lencode full zone (b5=0xFD const);
  Q 4x16 single head, m-tab b14,15,25,26,27,64-67 with b14^0x04
  + b25|0x01 iff q>=2, q-tab b13,20-24,72-75; A-tab
  b21-23,68-71; B-tab b13,14,20-25,72-75; 2 singletons.
- Next: commit R43 on GREEN, then P45 tables + probe.
