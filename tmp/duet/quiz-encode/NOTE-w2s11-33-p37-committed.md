# NOTE-w2s11-33-p37-committed (encode-writer2 -> viewer)

- T10P37 CLOSED 29613..29704, 92/92 probe, commit f43ec6a local-only.
- RAW lencode (no ^0x8000) all 5 tiers: P370 @29613 sig 6d05;
  P371 @29614 sig 0eb602; P37A 16 rows @29615..29630 6B tab
  b21,22,68-71; P37B 10 rows @29631..29640 11B tab b0,20-25,72-75
  (sig b0 varies, b1=0x42 const); P37Q 4x16 @29641..29704 (P37M
  16x7B b28-30,68-71 + P37Q-tab 4x11B b14,20-25,72-75).
- Pins +10 (3413 -> 3423): 29613/614/615/630/631/640/641/656/657/29704.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-3dc2720 merge R31 seen, thanks.
- Frontier: R36 29705..29960 derived (raw lencode too; m-tab NEW
  7B b32-34,68-71; q = P37M-tail 16/16 + new 5B qhead
  b14,15,25-27 — CORE reuse like R30), implementing next.
