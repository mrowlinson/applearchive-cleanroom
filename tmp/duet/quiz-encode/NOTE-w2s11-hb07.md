# NOTE-w2s11-hb07: R45 battery running, P47 derived

- R45 (32837..33092) implemented, probe 256/256; for-list extended;
  RECORD+battery+smoke running in background.
- P47 = 33093..33184 (92) dumped + derived read-only: RAW lencode
  92/92; A(2..17) is 80B-pay (tab b8,9,10,15,72-75, head
  01000000); B(18..27) 76B per-offset heads embedded in tab
  (b0,1,2,11,12,13,14,72-75); Q 4x16 row-heads, m-tab
  b16,17,68-71, q-tab b0,1,2,11,12,13,72-75; 2 singletons.
- R46 @33185 (80B, head 0c000000).
- Next: commit R45 on GREEN, then P47 tables + probe.
