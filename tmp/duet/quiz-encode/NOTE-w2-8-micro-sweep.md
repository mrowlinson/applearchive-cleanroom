# NOTE-w2-8 writer2: micro-beds closed, sweep heads-up, raven/bitmap next

- -b suffix tail CLOSED: 16b=16B (2465 arith EXACT), 1kb=1k=1024,
  4m dflt, 128m OK (0x8000000), 129m/0 REJECT ("Failed to create
  compression stream"). matches NOTE-008 bounds exactly.
- AEA nondet p0/2/3/4: p2/p4 char 13 (like p1/p5); p0/p3 char 14
  2/2 runs — byte12 STABLE: p0=0x30 (DER SEQ sig), p3=0x04 (EC
  point prefix). prologue-typed, explained. hdr12 pins unaffected.
- SWEEP heads-up (re NOTE-018): d6e2d7f does NOT contain
  impl2-adapter (race conceded NOTE-w2-7, file removed). IMPL2 leg:
  expect SKIP, not FAIL. OUTER2/PINS-OUTER2 legs: run; schema =
  name,check,expect,bytes,generator,os,backend; checks sha/size/
  str/rc (AEA nondet by design, zero .aea shas).
- read: NOTE-8 (w1 hygiene clean, HLC/DAT'C'/razors, zlib done,
  ACCEPTS NOTE-008), Q-10 (w1 OSS/lzma steer, viewer-owned),
  NOTE-018 (gate v2 + outer2 legs).
- turf: w1 accepts NOTE-008 (parent sign pending). writer2 starts
  raven/bitmap BLACK-BOX byte beds (aa-only; payload capture +
  structure; zero impl files until parent signs). compression_tool
  use needs cleanliness ruling — Q when beds require it.
- next: per-alg -t EQ bed (5MB t1/t18 x 5 algs) + raven/bitmap
  ladders. gap: g-beds EXTENDING; all grants green or conceded.
