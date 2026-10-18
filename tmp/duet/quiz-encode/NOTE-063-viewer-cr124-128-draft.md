# NOTE-063 viewer: CR-124..128 DRAFT (for lane commit when shell recovers)

```
CR-124 [MEASURED] lzbitmap chunk table = 12 entries x 10b LSB-first @chunk_end-17;
membership = top-12-by-op-count EXACT; order = tie-lottery (count-independent)
stage: probe
artifact: WS scratch-viewer3/zbmbed.py (lc-oracle 0x702 + OSS + table reader, sha TBD-shell)
numbers: tag80(gen fwd) B80=19461 ZBM-raw; flips @18503(+0)/18504(+1)/18540(+2,^01-only)
  reorder (ff 2->1 etc); value-INDEPENDENT @18503/18504 (4/4 values same table);
  w2 210/210 membership-exact + 38/210 reorders own-count-fixed + 11/11 tie-hyps dead
verdict: NEW (table layout from OSS READ-grant; lottery model A-25 CONFIRMED both seats;
  closes Q-22#1/#2 fully incl boundary-tie micro)
body: entry = (bitmap u8, pbc u2). WHO sits = count-EXACT deterministic; WHERE =
  DP-tie outcome (deterministic per input, unpredictable from summary stats).
```

```
CR-125 [MEASURED] OSS libzbitmap 574abea DIVERGES from lc-oracle on EVERY compressed output
stage: probe
artifact: zbmbed.py oss-vs-lc bed; OSS dylib sha 43d4f5e9... (pin 574abea, MIT)
numbers: tag0/30/80: lc=19482/19480/19461 vs oss=19951/19935/19953, 0/3 match;
  both sides roundtrip-decode exact; concurs w2 108/108 (12 matches = uncompressed only)
verdict: NEW (rewrite-sign half; OSS-link covers uncompressed-path ONLY per w2s5-16)
body: divergence structural (optimal-parse+ties vs greedy). OSS READ granted, LINK insufficient.
```

```
CR-126 [MEASURED] raw lzraven frame = magic 2b00caec[0:4] + hdr[4:12] + payload[12:12+pl] +
trailer[4]; zeros128 -> 60B (pl=352); aa-container output avalanches (beds must use ct)
stage: probe
artifact: WS scratch-viewer3/ravbed.py (sha TBD-shell)
numbers: pos100=ff -> 1B diff @file17 (=payload bit40); framed-store +16 = 12+4;
  aa -a lzraven 1B dev -> 163/176B differ + len+4 (NOT a shift; outer layer)
verdict: NEW (bed-path ruling + layout pin; PRE-007)
body: all raven bit beds use compression_tool -encode -a lzraven; aa path unusable for bits.
```

```
CR-127 [MEASURED] raven zeros-128 = 96b skeleton + 256b value-holes; response class by tier:
tail pure-holes, early skeleton-rewrite, mid +token; markers value-blind presence-knobs;
geometry moves ~every N; spread = stable split-holes + growing presence rewrite
stage: probe
artifact: ravbed.py beds (A-23/A-27/PRE-006..009)
numbers: 32 tail pos x 8 EXCLUSIVE holes; early dev n~60 scattered; mid +4B @19..76 (N=128);
  count>=2 in 0..95 -> tier change; m67 immune 0/128; m226 excl 0,2 / m322 excl 0;
  N=129 common-10 + exact-8@{3-6,50-53}; N=131 common-39 same slots (N=130 common-24 predicted+confirmed)
verdict: NEW (NO-TAG reframe joint w2; Q-21/Q-24 closed; absolute-offset reads across N VOID)
body: tags pre-exist in zeros base (skeleton = match-token stream); values land in holes;
  T0/T1 form-flip @N=125 (fields early->late) unifies geometry jumps.
```

```
CR-128 [MEASURED] T3 period-64 combs = tail value-hole placements at stride-64 offsets
(no separate field); teeth 64/192 skeleton-only-never; op3=220 resync edge offset-pure
stage: probe
artifact: ravbed.py T3 beds (A-28/A-29/A-30/A-31)
numbers: d-map N-ind @760/780/800: d=24->89, 20/19->128, 18->153+128, 9->25;
  89/192 const-0 all 309 zeros-N; 64/192: ~6700 intact negatives (876 singles + 656 pairs
  + 4960 triples exhaustive + 200 runs), 0 lights; triples: 30 breaks all contain (17,29);
  220-edge: 14/14-bit coherent inversion @472/473, p445+ transparent, p<=442 mask-or-tierchange
verdict: NEW (Q-25/Q-26/Q-27 closed; middle teeth content-only; edge = tier-offset function)
body: stride lives in hole allocation; 64 = N-knobbed skeleton (on@off218+), 192 const-0.
```

## Derivation appendix (to file with lane commit)
inputs: /usr/bin/compression_tool (sha re-match TBD), libcompression.dylib (system),
  WS scratch-viewer3/ravbed.py + zbmbed.py + q27triples.py (shas TBD-shell),
  OSS libzbitmap 574abea (READ-grant A-16, dylib 43d4f5e9...),
  w2 exhibits as CONFIRM targets only (tailmap/offsets/zone/echo/halted-clock all
  cross-confirmed to the bit both directions), never as evidence
not-consulted: decompiler output, port/reference sources, vendor implementations,
  decode-side answers, other lanes beyond verify duty
outputs: 5 clause drafts (CR-124..128 MEASURED), 0 promoted
findings: bitmap-lottery, oss-divergence, raven-layout, skeleton-holes, t3-combs-edge
base: lane tip TBD at commit
