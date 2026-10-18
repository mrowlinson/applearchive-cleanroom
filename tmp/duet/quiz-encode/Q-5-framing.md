# Q-5 framing confirm: T-split, A-payload rule, XAT const, kinds

- need (behavior-only, beds+numbers):
  (a) CTM/MTM 'T' 12B layout: sec/nsec widths+order? exhibit: own
  d1a off 0x9c..0xa7 (CTM) 0xaa..0xb5 (MTM) vs live mtimes.
  (b) 'A' payload rule: headers-first-payloads-after always? what
  orders multi-A payloads when >2 'A' fields (xattr-added file)?
  (c) 11B XAT blob 01 02 00 66 97 d0 7a bb 10 2c 73: constant
  under what inputs (uid? host? time? content)? any input changing it?
  (d) entry kinds M/X/P: exact assignment (M=root-only? P=nested?
  file kind if nested?) + TYP DP/FP full value set.
- tried: own probes (NOTE-2). underivable further black-box without
  matrix viewer already runs.
- exhibits: own *.aar in wt-encode-writer tmp/scratch-encode/out/.
- side: ENCODE.
