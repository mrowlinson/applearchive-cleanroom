# A-371 (viewer r26): Q-365 T10P504 192129..192476 — CONFIRM all

First-hand bed 191085..192478 (own
1394-cell census shared with A-370,
oracle regen rc=0). Payload
.rav[12:-4]. Bed + scripts: NVME
encode-viewer/q362-r26/.

## 1. shape: CONFIRM
- 350 cells 192129..192478 ALL raw104/
  pay88. PB0 192129 bc020000 REPEAT-
  sig P503; PB1 192130 00740500 NEW.
- PBA16-PLAIN 192131..146 sig
  00845700; M7 b32-34,80-83 16/16;
  b5-const dd; consts 79 (base 86).
- C10 192147..156 sig fe7c0500 (==
  P505 PB1 @192478 ✓); M3 b84-86
  10/10 FIRST, b87 const 6a; b5-
  const dd; consts 83.
- QUAD88 192157..220 sig fe8c5700:
  M6 b40,41,80-83 16/16 per row,
  row-seqs IDENTICAL; R1 b84 rows
  05/25/45/65 (+0x20) row-const, NO
  pairing; b5-const dd; consts 79.
- T88-RING 192221..476 2-sig-BY-COL
  (m=o%16): m0-12 fe1c7f05 / m13-15
  fe2c7f05, col-stable EXACT; TM10
  b1,30,31,39,46,47,80-83 = f(m)
  16 distinct; TR6 b40,41,76-79 =
  g(row) 16 distinct; UNPAIRED; b5
  = dd+(o>=35)+(o>=163) all 256;
  b84-87 = 85fa6f6a all 256; consts 70.
- Next: P505 PB0 @192477 bc020000
  REPEAT-sig; PB1 @192478 fe7c0500
  (== own C10 sig ✓).

## 2. verdict: CONFIRM (28/28 checks)
- Every Q-365 byte claim reproduces
  from own bed. w2d tier cut SAFE.
