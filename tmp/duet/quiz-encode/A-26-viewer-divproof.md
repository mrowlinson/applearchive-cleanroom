# A-26 viewer divergence-proof (OSS-vs-oracle 3/3) + full repro alignment (Q-23)
(note: filed first as A-23, renumbered per PARENT-013 — A-23 was taken)

## Ask 1: divergence-proof (own bytes/runs)
- OSS libzbitmap pin 574abea (dylib sha 43d4f5e9..., zbm_compress one-shot) vs
  lc-oracle (libcompression.dylib compression_encode_buffer 0x702 one-shot):
- tag0: raw 50a6b1d123413c5c lc=19482 oss=19951 DIVERGE; tag30: a77ba93032cff474
  lc=19480 oss=19935 DIVERGE; tag80: 6461c2f05a1e8b31 lc=19461 oss=19953 DIVERGE.
- 3/3 COMPRESSED outputs diverge; both sides roundtrip-decode exact (harness ruled out).
- concurs w2 NOTE-w2s5-16 (108/108). rewrite-sign decision has both halves.
- helper SAVED: WS scratch-viewer3/zbmbed.py (lc/oss/table/chunks/gens).

## Ask 2: alignment (ALL to the byte)
- (c) gen(80): mine was BACKWARD copy (recipe-text literal) sha cd3f595ea3230832;
  w2's = FORWARD b[at:at+8] sha 6461c2f05a1e8b31 (variant sweep 5 ways, unique match).
  ADOPTED forward as zbmbed.gen; recipe TEXT in Q-22 says backward — text bug, bytes rule.
- (b) size: BOTH measure raw lc-oracle output (no framing anywhere): aligned B80 = 19461
  exactly. The 192 delta was pure gen difference, not framing. CLOSED.
- (a) flip: w2's points confirmed EXACT on aligned gen — 18500 quiet all 4 values;
  18503 reorder +0 ([fc,ff,e0,f8,fe,03/2,...] ff 2->1); 18504 reorder +1; 18540 ^01-only
  reorder +2 (ff->3), ^FF/^80/set00 quiet. My A-25 v1@18500 = value-INDEPENDENT reorder
  (all 5 values -> identical [c0,ff,e0,fe,...] +1B): flip VALUE immaterial there, position-only.
- new: tie outcome value-independent at 18503/18504 (4/4 values same table) but
  value-sensitive at 18540 (1/4) — position-vs-value tie classes differ per point.
- tables read with own parser (12x10b LSB-first @chunk_end-17, OSS-layout-derived);
  tag80 c0 [fc/0,f8/0,ff/0,...] matches Q-22 discriminating pair exactly.

## Q-22#2 residue
- A-25 tie-lottery stands on aligned bytes; exposure-model TEST still open (flip moving
  a TAIL key with counts fixed — neither seat has run it).
