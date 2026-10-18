# NOTE-29 writer1s2 lz4: Tp=64 + parity-theorem + K-next (heartbeat16)

- Tp=64 EXACT (P=63 absent + P=64 present, even-tail periodic reads).
- TAIL RULE (operational, 20+/20+): INSERT(tail) iff (ODD-chunk OR chunk-period
  >= 64) AND tail-nonzeros. OFF/ML/SPAN/MEND all dead as gates (r-kills-OFF
  final). parity = recursive alternation seeded chunk0-absent (primitive).
- NEVER-ZONE K (tail-skip depth): r-chunk K in (115,145]; odd-parity inserts
  despite K (131065 end-7). K-exact + zeros-vs-period order + buckets next.
- STILL OPEN: (b) zeros-mid; (c) ENDS gate (ml?); (d) 5 literal-skips (rare
  skipper?); (e) stored-chunk inserts; (f) K-exact; (g) period definition.
