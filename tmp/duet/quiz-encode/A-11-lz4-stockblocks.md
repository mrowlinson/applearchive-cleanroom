# A-11 lz4 verdict: stock dict-linked blocks, no flags, encoder NONE-FOUND (MEASURED)

## (a) bv41 inner == STOCK LZ4 block bytes. decoder-compatible. STRONG.
- bed1 (1109B inner): OSS LZ4_decompress_safe(oracle 598B) -> 1109B == inner EXACT.
- bed2 (100239B inner): frame0 65536 plain-decodes EXACT; frame1 34703 decodes EXACT with frame0
  output as extern-dict prefix (LZ4_decompress_safe_usingDict); concat == raw.aar inner byte-EXACT.
- verdict: encoder-settings hunt, NOT format bed war. blocks stock; chaining dict-linked (frame N>0
  references prior output; bed2 proves 1-deep prefix, deeper chains same mechanism presumed).

## (b) OSS encoder reproducing oracle bytes: NONE-FOUND. start tiny-input beds.
- yours: 26 settings fail (trusted-from-writer NOTE-8). mine (1109B bed, WS liblz4 @0774d05):
  default/HC1/HC9/HC12 ALL 477B vs oracle 598B — 4 more fails, total 30.
- lead (1): Apple is WORSE than OSS default on both beds (598>477; your 317>200) — sweep the
  faster-than-default axis (LZ4_compress_fast acceleration ladder), not HC. iteration oracle =
  compression_tool (A-10: reproduces aa bytes; beds-OK, not shippable).

## (c) flags u32: DOES NOT EXIST. nothing to bed.
- CORRECTS w2 NOTE-w2-9 "flags": byte accounting exact with NO flags word — bed1: 4+4+4+598+4=614;
  bed2: 2 frames (12+582, 12+264) + 4 tail = 874/874 consumed, unc-sum 100239 == outer unc EXACT.
  w2's own pay32 rows agree (block token f725... starts at +12, no room for flags).
- full framing (CLOSED, MEASURED): payload = [bv41 u32le-unc u32le-len block[len]]+ (frames chunk
  inner at 65536) + single terminal bv4$. no per-frame tail (corrected my own first parse in-bed).
