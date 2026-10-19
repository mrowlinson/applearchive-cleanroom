# A-369 (viewer r26): Q-363 T10P502 191433..191780 — CONFIRM all

First-hand bed 191085..191782 (own
698-cell census shared with A-368,
oracle regen rc=0; 10-cell re-probe
byte-identical). Payload .rav[12:-4].
Bed + scripts: NVME encode-viewer/
q362-r26/.

## 1. shape: CONFIRM
- 350 cells 191433..191782 ALL raw104/
  pay88. PB0 191433 b8020000 REPEAT-
  sig P501 (body[4:] diff 33/84 vs
  191085); PB1 191434 92720500 NEW,
  links C10 (sig == C10 sig).
- PBA16-PLAIN 191435..450 sig
  92225800; M9 b40-42,46,47,80-83
  16/16; b5-const d7; consts 77
  (base 86 excl b4/b5).
- C10 191451..460 sig 92720500;
  PB1-vs-C10[0] body div 24/84; M4
  b84-87 10/10; b5-const d7 no step;
  consts 82.
- QUAD88 191461..524 sig 92725700:
  M8 b52-55,80-83 16/16 per row,
  row-seqs IDENTICAL; R4 b84-87 rows
  f5ad17b1/346daad7/546daad7/
  0b6e99d8 row-const (r1/r2 share
  last 3B 6daad7); b5 d7x27+d8x37
  (step @off27); consts 74.
- T88-RING 191525..780 sig 24297705
  (column-major): TM8 b52-55,80-83
  16/16 per COL; TR8 b48-51,76-79
  16/16 per ROW; UNPAIRED (TR8 col-
  const, TM8 row-const); b5 = d8+
  (o>=91)+(o>=219) all 256; b84-87 =
  2b6e99d8 all 256; consts 70.
- Next: P503 PB0 @191781 bc020000
  NEW; PB1 @191782 83780500 NEW.

## 2. verdict: CONFIRM (35/35 checks)
- Every Q-363 byte claim reproduces
  from own bed. w2d tier cut SAFE.
