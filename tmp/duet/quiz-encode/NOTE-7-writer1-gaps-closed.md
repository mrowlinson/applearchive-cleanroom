# NOTE-7 writer1: gaps closed 11/11, turf ack, hardlink verdict

- read: A-6, VERIFY-dc87389/2d1ec2d (both PASS), NOTE-006/007,
  PARENT-001 (COMPLIANT: worktree identity already = those values),
  NOTE-w2-1/2, Q-7/Q-8, A-7/A-8.
- commit 8a0a67e: ALL VERIFY gaps closed. RAWENC-GREEN 11/11,
  UNITS-GREEN 16/16, PBZE-GREEN 4/4 (re-run this shift).
  #2 min-width 1/2/4 (c9: MOD 0x9ed/0x3ed/0x180, FLG'2' 32768,
  GID'1' — impl bytes cmp-clean vs oracle).
  #3 FLG=st_flags (same exhibits). #4 LNK bytes (was bytes since
  dc87389; c10 unicode link liën->réal PASS, LNK len 9 = bytes).
  #5 xattr sorted (adversarial: created zzz,aaa -> emitted
  aaa,zzz; recs 0x13/0x12 exact). #6 B/C/S+DEV (c11 live socket
  PASS; synthetic B/C units vs A-6 numbers 0x01000001/0x03000002,
  DEV-after-PAT, no DAT/XAT, hdrsize==len).
  c7/c11 compare-only documented in pins header.
- CTM=btime stands (NOTE-006; touch retrodates btime — solves my
  tm-stat mystery). 15/16 rule stands (mine 100/100 + viewer flip).
- hardlink: SETTLES A-6(e) OPEN (writer bed p8-hl): 2 independent
  F entries, content duplicated, hdrs 96/92. no link record.
- behavior: unreadable input -> oracle exit 1 "Archive encoding
  failed" (observed; impl raises too, stderr text differs).
- TURF (re A-7 provisional): mine = raw inner + lzfse outer +
  pbze.py/encode.py/batteries/pins (committed first per A-7).
  cede: AEA-encrypt + -b/-t matrix to writer2. adapter = RACE
  (filing mine; first green wins). other-algs IMPL: continuing
  in pbze.py (my file; NOTE-6 stated) — zlib/lzma/lz4 OSS-compare
  next; lzraven/lzbitmap via Q-9. PARENT may redraw; no writer2
  filename touched.
- gap: g6 DONE (raw+lzfse). g7 adapter race. g8 other algs.
  g9 C port (awaiting parent steer: now or after algs?).
- waiting: A-9 (Q-9: raven/bitmap, B/C stamps, >4GB).
