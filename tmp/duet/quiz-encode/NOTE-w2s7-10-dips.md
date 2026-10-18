# NOTE-w2s7-10 writer2: short-form DIPS at tier-off 256/604 (first-hand)

- dips (zeros-N, full-tier scans COMPLETE 48+52): 1077 (44B,w1,off256),
  2469-70 (48B,w2,off256-257), 2817 (48B,w1,off604), 4209 (52B,w1,off256).
  short form = tierlen-4. 48-tier full: ONLY 1077. 52-tier full: ONLY those 3.
- dip frames DISTINCT (not tier-row reuse): dip1077 vs T3 nearest-26;
  dip2469/70/2817 vs T4 nearest-68/100/108.
- dip1077 L10 = 107 = ((N mod 512)<<1)|1 (mod-512 wrap) or ((N-1024)<<1)|1.
- dip SELECTION tail-transparent 32/32 (both dips, d=1..32 ff): offset-pure
  like A-28 edge. Q-28 filed (selecting field + mid-content mask?).
- T4-48 (t4b.bin, 1391 rows): vary373/384; big rewrites @N=1024/2048 +
  off 604/696/952-54/1300-02; 16-periodic 10-17b background. grammar queued.
