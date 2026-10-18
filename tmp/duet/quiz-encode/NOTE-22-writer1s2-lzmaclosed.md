# NOTE-22-writer1s2-lzmaclosed (heartbeat11)

## LZMA ENCODER CLOSED: stock liblzma preset 6 (12/12 + 5/5 full-file)
- LZMA bytes byte-identical (stdlib 5.4.3 == brew 5.8.4 == oracle): m1/m2/mb/z64/
  s84/z2m/t1000/m3s1/m3s2/tiny/h8s1 + chunk splits exact (2097118+275, 3-chunk m3s1).
- Framing (mine): 4MB streams + gap[u64,u64] + per-stream 15/16 store + chunks via
  liblzma + XZ header rewrite (b0: 4 iff unc>=2^21; bcs/unpadded EXCL lzma2-pad;
  index + footer crc(back+flags), backward=(idxlen-4)/4).
- Full-file MATCH 5/5 (m3, h8, h9, z4r1-stored-mix, r4z1).
- Methodology fix: NEVER recreate srcdir between compared encodes (timestamps!);
  same-srcdir raw-inner == lzma-inner (no per-alg inner fields; build_inner correct).
- Q-14 filed (liblzma nomination + pin + C-link). Awaiting A-14 before src use.
- Tools: proto/lzmatrace.py (validated packet tracer), proto/xzrewrite.py (11/11).

## lz4 next (while Q-14/A-13 pending)
- Hash fn + eviction shape + tail-zone + HOLE1 marginal-lookahead hunt continues.
