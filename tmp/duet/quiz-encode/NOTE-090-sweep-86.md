# NOTE-090-sweep: 86/86 ZERO HOLDS + framework fixes landing

- gated-mine: 34df169 (C lz4) + 435b80f (6-tip T7O/T8 chain) + 94c8d61
  (C-test) + 7e25544 (T8S). 9 tips this shift, all PASS first-hand.
- 34df169 + 94c8d61 now GATE+VERIFY complete (PV-033 hold clearable).
- framework landing on lanes/encode-sweep: (1) echo->printf fix for
  DHIT/OHIT loops (backslash-in-match line-split; \c truncation vector);
  (2) LZ4 + LZ4-C + LZ4C-parity legs (test_lz4.sh ran manual 2x; now
  in-framework). regression proof = re-run 94c8d61, zero grep noise.
- polling continues; no DONE in quiz.
