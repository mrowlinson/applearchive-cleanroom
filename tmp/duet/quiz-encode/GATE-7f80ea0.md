# GATE-7f80ea0 sweep: PASS-battery + HOLD-CONTINUES (lz4 rescan, m4m RED)

- tip: lanes/encode-writer @7f80ea0 (parent 4d61e87 ✓). delta: chunk-start
  tail rescan (miss-only, [gpos-8,gpos-5] nearest-first); 488/672 (+1/-0:
  bis/131072 fixed). lzma untouched.
- battery: GATE-PASS full legs (outdir gate-w1-7f80ea0-s2).
- holdout: 11/12, FAIL m4m py-vs-oracle ONLY — identical RED.
- verdict: commit GREEN, FLAG-w1-lzma-b0-hold STANDS.
- w1s3: chunk-start WAR parked (~30 calls, net +1; K-pending/tailroom/ktail/
  tail-override all lose); pivot LEN 10!=9 x42. Q-30/Q-31 still open.
- coverage: 66/66 writer tips gated (65 battery-PASS + 1 RED-held).
