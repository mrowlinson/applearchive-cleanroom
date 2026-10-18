# PRE-056b H-zone 4997..5252: quiet-256, 16-tabs + 16-bands (w2 T6H)

## census (v5ac/v5ad, 256 rows all 56B, 12 var)
- 15 edges>=8 @5013..5237 step-16 EXACT. no triple, no chatter,
  no dips. simplest zone since D.
- 16-tabs from 4997 (x16 strict): b6=(34 9e dc 27 b2 40 7d bb
  80 be fb 94 fe 8c c9 62), b7=(8b 2b ab 3b 9b ab 2b ab 3b
  bb 3b ab 4b 5b db 4b), b8=(1b 7b 7b 9b 7b 7b 9b 9b db db
  fb db 3b 3b 3b 3b), b9=(d2x4 d3x4 d4x3 d5 d6x3 d7).
- b5: 16-cycle (c7 c7 27 c7 47 87 e7 47 a7 07 67 27 27 67
  c7 87) + low-nibble 128-plateaus (x7/x8/x9 @4997/5120/5248).
- b4: L10-lo ramp (+2/row, wrap 5120/5248).
- bands: b54/b55 strict 16-bands from 5013; b52 16/32/48 mix;
  b53 16s + one 32 (5045-5076:ad). b50: 112-plateaus ad/ed/2d
  @4997/5109/5221. b51: 5d->5e @5221.

## sectioning (one commit 4997..5252, or split at 5120/5125)
- H0 4997..5124 / H1 5125..5252 split point: b5 nibble x7->x8
  @5120 + b52 48-band 5125-5172. either shape shippable.
