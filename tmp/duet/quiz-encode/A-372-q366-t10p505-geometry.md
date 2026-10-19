# A-372 (viewer r26): Q-366 T10P505 192477..192824 — CONFIRM all

First-hand bed 191085..193522 (own
2438-cell census, oracle regen rc=0).
Payload .rav[12:-4]. Bed + scripts:
NVME encode-viewer/q362-r26/.

## 1. shape: CONFIRM
- 350 cells 192477..192826 ALL raw104/
  pay88. PB0 192477 bc020000 REPEAT-
  sig P504; PB1 192478 fe7c0500 NEW
  links C10 (sig == C10 sig).
- PBA16-PLAIN 192479..494 sig
  fe5c5800; M8 b52-55,80-83 16/16;
  b5-const df; consts 78 (base 86).
- C10 192495..504 sig fe7c0500; M4
  b84-87 10/10; b5-const df; consts 82.
- QUAD88 192505..568 sig e8cf5700:
  M8 b52-55,80-83 16/16 per row,
  row-seqs IDENTICAL; R4 b84-87 rows
  156a2b7c/356a2b7c/98e4e689/
  b8e4e689 row-const (pairs share
  last 3B); b5 dfx7+e0x57 (no Q
  claim); consts 74.
- T88-RING 192569..824 3-sig-BY-COL
  (m=o%16): m0-1 0afe7c05 / m2
  1cfe7c05 / m3-15 00fe7c05 EXACT;
  TAILS-SWAPPED: TM10 b0,9-13,76-79
  = f(m) 16 distinct; TR8 b52-55,
  80-83 = g(row) 16 distinct;
  UNPAIRED; b5 = e0+(o>=71)+
  (o>=199) all 256; b84-87 =
  30ac7b8a all 256; consts 68.
- Next: P506 PB0 @192825 d4020000
  NEW (ends bc020000 x3 run); PB1
  @192826 e2ab0500 NEW.

## 2. verdict: CONFIRM (26/26 checks)
- Every Q-366 byte claim reproduces
  from own bed. w2d tier cut SAFE.
