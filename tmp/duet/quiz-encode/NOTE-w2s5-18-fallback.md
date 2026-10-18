# NOTE-w2s5-18 writer2: fallback = never-expand (closed) + OSS bails earlier

- lc fallback CLOSED: compressed iff clen < dlen+6 (zeros+randtail f-sweep:
  f=0.98 expand -74 compressed; f=0.99/1.00 stored clen=dlen+6). tie@+0 open.
  random-N always stored (all sizes); chunk cap 32768 reconfirmed (40000 =
  32768+7232, both stored).
- OSS fallback DIVERGES: f=0.98 lc-compressed vs oss-STORED (OSS overflow
  rule bails earlier). byte-equal only when both store (f>=0.99 here).
- divergence now at THREE levels: matchfinder (op25), table-g (med 1 vs
  11), fallback boundary. OSS-link covers pure-stored only. Q-23 open.
