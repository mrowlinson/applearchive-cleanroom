# NOTE-w2s11-hb09: R46 battery running, new era mapped

- R46 (33185..33440) implemented, probe 256/256; for-list extended;
  RECORD+battery+smoke running in background.
- NEW ERA @33441: P-tiers now 28 cells (2x76B singletons +
  16x80B A + 10x76B B, NO Q). P48 = 33441..33468 derived
  read-only: RAW 28/28; A-tab b19,30,31,68-71 (80B, head
  02000000); B-tab b2,3,15,25-31,72-75 (off18 own head).
- R47 = 33469..33788 (320!, 80B): head 01000000 then 13000000
  (split TBD); P49 @33789 (2x76B singletons + A16 head 04..).
- Next: commit R46 on GREEN, then P48 tables + probe.
