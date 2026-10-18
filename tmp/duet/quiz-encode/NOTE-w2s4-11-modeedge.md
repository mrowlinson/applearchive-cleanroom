# NOTE-w2s4-16 (renumbered; filename still NOTE-w2s4-11-modeedge.md): stored-mode + rational mode-edge K*=201 + 4B-quant + tag-rate model

## R1: random-256 = STORED-verbatim (slot=pos identity, len=N), F3=(N<<12)|1
- RAND F3=00100001 paylen=256 pay==raw EXACT; ZERO F3=0002c000 paylen=44. F1/F2 same.
- Stored-F3 sweep N=1..5000 (19 nodes): F3=(N<<12)|1 UNIVERSAL -> ravframe closed-form HOLDS both modes (STORE=F3&1). No verifier gap; STORED-PINS queued (coverage).
- Head/tail distinction exists ONLY when matches exist (zeros); pure-literals (random) = all-local slot=pos, forward-order.

## R2: mode-edge K*=201 EXACT (N=256, K random-prefix + zeros); rational-choice (min-len wins)
- K=200 MIXED-252; K=201..203 STORED-256. Mixed-trend +1B/byte -> MIXEDLEN(201)~256 = tie -> STORED (tie-break-STORED or strict-gt; tie-case hunt queued minor).
- Implies encoder compares MIXEDLEN vs N (never-expands).

## R3: payload 4B-QUANTIZED (U32-padded bitstream); literal-run steps @L=3,6,11,14,18,21,25,28,32,36,39,43,47,51,54,58,62,66,69 (gaps 3/4/5)
- L=1,2 FREE (absorbed, 44B baseline) -> min-literal-run 3 (mirrors LZ min-match 3?).
- Multi-seed 4/5 INVARIANT -> gap-3 = TAG overhead (seed-invariant), gap-5/4 = rare chance-match discount.
- Rate model: gap-3 word = 3x10bit tagged (32/3=10.67B/lit); gap-4 word = 4x8bit raw. Alternating tagged/raw words (phase-slip every ~2 -> tags >>10b or multiple tags; TPARSE-V2 will read directly, fit skipped).
- L=21-seed-3 outlier (-4B) = BOUNDARY-match (00@20+zeros run, len>=3 token-swap) -> MIN-MATCH <= 3 (dedicated bed queued).

## Next: TPARSE-V2 (U32-word LSB-first segmenter + known-field anchors) -> direct tag read; min-match bed; stored-pins.
