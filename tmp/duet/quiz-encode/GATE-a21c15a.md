# GATE-a21c15a sweep: PASS (rgram 1222/1222, T8A1 16x16)

- tip: lanes/encode-writer2 @a21c15a (parent d346251 gated PASS). rgram.py
  +45/-0, cells to 11168, pins 1192->1222 (+30/-0).
- code read (ALL): _T8A1T 16 tabs + _T8A1B 16 block-words + _T8A1C consts
  (46 keys, unique) + branch n<=11168 (off=n-8735, m=(off-2178)&15,
  q=(off-2178)>>4): m<=15 (16 tabs), q<=15 (16 blocks), contiguous after
  T8Z (off 2178 follows 2177), b5 0x55 + steps @2273/2401 matches message.
  ordering verified.
- NIT (no FAIL, same class as T8Z): message "(1224 pins)" counts 2 csv
  comment lines; data rows 1222 (battery set-eq decisive).
- battery: GATE-PASS (outdir gate-w2-a21c15a-s4): HYGIENE/CONTAM clean,
  RGRAM n=1222, PINS-RGRAM set-eq 1222/1222, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 111/111 (NOTE-092 baseline + 4), ZERO holds.
