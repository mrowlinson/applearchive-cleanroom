# PRE-060b 60-tier head 6041..6296: 16-bands + per-row bytes (T7A stage)

## census (v5ai60 first-hand, 256 rows all 60B, 12 var)
- 14 edges>=8 @6057..6281 step-16 + one 32-gap (6185-6217).
  var = 0/4/5/6/7/9/10/11/12/13/20/21 (== v5i EXACT ✓).
- bands from 6057: b5 (8f/0f/af/4f/8f/ef/cf|d0-nibble-split
  @6144/90/f0/d0-32/70-32/d0/30/31/71), b6/b7 clean 16s+32s,
  b12 16/32s (a9/b1/d9/da/02/0a/32/33/59/62/63/89).
- b13: single edge 6f->70 @6137. b4: ramp.
- per-row: b0 {08,09,0b}-walk (nruns 192), b9 (192), b10
  f0-f3 ramp-ish (161), b11 full-var (256), b20 (144), b21
  32-plateaus (32). tab-shape OPEN (ask if needed).
- 6041..6056 quiet-16 head (all bands at first values).
- split suggestion: 6041..6143 / 6144..6296 (b5 nibble @6144).
