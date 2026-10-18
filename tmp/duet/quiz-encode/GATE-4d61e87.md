# GATE-4d61e87 sweep: PASS-battery + HOLD-CONTINUES (lz4 mod5, m4m RED persists)

- tip: lanes/encode-writer @4d61e87 (parent 30ce9d8 ✓). delta: lz4 P1 skip
  iff gap%5==4 (finding 487/672, +4/-0: o4/SPAN2/q640/k192 fixed, ZERO broke;
  all 61 ORD-older first-divs resolve).
- battery: GATE-PASS full legs (C-BUILD w=0/RAWENC 13/PBZE 10/LZMA 6/SMOKE 6/
  UNITS 22/C-parity/PINS all/LIBCOMP zero-refs/ADOPT; outdir gate-w1-4d61e87-s2).
- code read: gap%5==4 gate in lz4enc.py (bisection M1a-d: tracks mend_prev==MS-4,
  not match-existence/content; 501/501 first-divs split). lzma untouched.
- holdout: 11/12, FAIL m4m py-vs-oracle ONLY — identical RED (lzma b0 unfixed).
- verdict: commit GREEN, FLAG-w1-lzma-b0-hold STANDS (fix + 12/12 re-gate pending).
- quiz-hygiene CONCUR NOTE-41: Q-30-buckets (w1s3) vs A-30-tooth (w2 line) =
  number collision, distinct threads; referee by FILENAME, no renames.
  Q-31-p1mod5 OPEN for viewer (mechanism ask, behavior-only ✓).
- coverage: 63/63 writer tips gated (62 battery-PASS + 1 RED-held).
