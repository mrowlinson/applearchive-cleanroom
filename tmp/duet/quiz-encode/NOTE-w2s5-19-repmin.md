# NOTE-w2s5-19 writer2: rep = key-runs maximally merged + min-dlen 145

- REP: groups = maximal same-key runs (zeros-1000: [1, 127]; zeros-8000:
  [1, 999]; first op separate = period-SET key differs from reuse key).
  no run-splitting to rep 999 (f-scheme unbounded-ish, dlen-capped).
- MIN-DLEN exactly 145 (zeros 144 UNCOMP / 145+ comp clen=43; text agrees
  144/152): content-independent SIZE gate (not never-expand: 144 would
  save ~107B yet stores). framing: dlen>=145 ⟺ nops>=19.
- fallback full rule: STORE iff dlen<145 OR clen>=dlen+6 (tie@+0 still open).
- Q-23 open. claim HELD.
