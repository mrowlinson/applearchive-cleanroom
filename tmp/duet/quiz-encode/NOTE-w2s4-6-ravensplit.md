# NOTE-w2s4-6 writer2: raven STORE==raw, MIN-64, 512K-split, F3-freeze

- STORED payload == raw EXACT 3/3 (8B/1K/100K). trailer 00000000
  everywhere. F3 = PAYLOAD*4096+STORE 14/14 single-frame.
- MIN-SIZE 64 EXACT: zeros <=63 STORED, 64+ COMPRESSED (44B);
  random STORED all sizes (incompressible fallback). rule =
  (raw<64) OR (incompressible); comp~raw edge TBD.
- MULTI-FRAME at 512K: 600K-stored = hdr12 + raw[0:512K] +
  4B 2nd-hdr (75712*4096+1 EXACT) + raw[512K:] + trailer.
  F3-freeze 0x80000001 = first-frame cap 512K (NOT saturation).
  F3 rule holds PER-FRAME. 3-frame + freeze-boundary queued.
- F2 = f(rawlen) ONLY (seed/content-independent; same for
  zeros-compressed and random-stored @100K). step function,
  transitions ~81K/98K/198K/..; 200000 topbyte anomaly (28)
  needs re-verify; full bisection queued (table-able).
- zeros payload scales log-ish (44B@64..512, 48@1-2K, 56@4K,
  60@8K, 68@16K, 84@64-100K). per-1 head == zeros head.
  per-32 likely STORED (payload starts with raw).
- plan: freeze-boundary (524288/9) + 3-frame (1.1M) + F2
  bisect + payload titration (len/offset/literal) -> ravframe
  PINS commit (framing-first, rb2-precedent). Q-17/18 open.
  claim HELD.
