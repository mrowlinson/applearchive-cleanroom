# NOTE-10 writer1: C port parity, shift checkpoint @e72aa4c

- commit e72aa4c: src/c/aae.c + Makefile + ENC_BIN override.
  C byte-parity first-hand: rawenc 12/12 (pins match), pbze 10/10
  (pins match), socket IDENTICAL, 4.5GB DAT'C' IDENTICAL.
  build: zero warnings (-Wall -Wextra), binary ONLY in
  /Volumes/NVME/applearchive-cleanroom-ws/build/aae (never repo).
  bug caught+fixed in-test: getattrlist packed-offset (crtc 0).
- race: writer2 conceded (NOTE-w2-7); impl-adapter stands as the
  encode backend. w2 corroborates codec framings (xz/bv41/785e).
- lane tips: dc87389, 2d1ec2d (GATE PASS), cea6ba0 (GATE PASS,
  FLAG cleared), 8a0a67e, fcac6c3 (behavior PASS, hygiene RED),
  8a79248 (pyc cleanup), a71622b (pin rename), e72aa4c (C port).
  8a79248+a71622b+e72aa4c await sweep v2 re-gate.
- pins: rawenc 11 rows (c7/c11 compare-only noted), pbze 10 rows.
- parked (no unblocked work left): lzma/lz4/lzbitmap byte-hunt
  (counts in CODEC-FINDINGS.md), lzraven parent path, A-10,
  turf sign, C-port gate. backing store: prototype py + C agree
  with oracle on raw/lzfse/zlib everywhere bedded.
- claim HELD (no joint DONE). seat healthy, handing shift.
