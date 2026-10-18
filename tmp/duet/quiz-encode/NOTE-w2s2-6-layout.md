# NOTE-w2s2-6 writer2: outer layout CLOSED (raven/bitmap extend A-6(f))

- layout (own beds, 12+ pts): 12B prefix (magic+0+BE blocksize) +
  blocks[16B hdr (0,BE unc,0,BE comp) + comp bytes]. comp EXACT
  everywhere (80/94/200/218/236/271/232/1248/64/90). chain closes
  byte-exact: raven b10k 28+216+864+64=1172=file ✓; bitmap
  28+234+990+90=1342=file ✓. NO stream footer (random tail16 =
  compressed bytes). stored ⟺ comp==unc, payload = raw bytes.
- unc rule: non-last blocks read slice EXACT (10000); LAST block reads
  slice+28 (7-pt sweep + singles: 285/321/200223/223/473/... all
  inner-slice+28). invariant: sum(unc)-28 = inner length (closes on
  raw-measured inners 257/80195/85195/100195/200195). corrects my
  NOTE-w2s2-5 "+30" (artifact of assumed metadata 193; actual 195).
- A-6(f) gaps closed from w2 side: per-alg flip points (were UNPINNED,
  now 103-pin battery) + raven/bitmap layout (were lzfse/zlib-only).
- Q-14 update: (a) SELF-ANSWERED (unc+28 last-block rule above);
  (b) WITHDRAWN (no asymmetry — comp exact; my span-split artifact).
  viewer confirm welcome, nothing blocked. Q-13 still open.
- next: UNC-rule battery cells + commit. claim HELD.
