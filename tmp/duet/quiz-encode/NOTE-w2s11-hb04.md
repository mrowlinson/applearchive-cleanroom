# NOTE-w2s11-hb04: P45 battery running, R44 derived

- P45 (32397..32488) implemented, probe 92/92; for-list extended;
  RECORD+battery+smoke running in background.
- R44 = 32489..32744 (256, FIRST 80B-pay tier, head 01000000
  const); P46 = 32745..32836 (92, 76B); next @32837 80B.
- R44 derived read-only: m-tab b36,72-75 (5B), q-tab
  b18,19,29,30,31,68-71 (9B NEW, no P45M reuse), raw lencode
  256/256.
- GATE-35d6de7 (P39) PASS-individual seen.
- Next: commit P45 on GREEN, then R44 tables + probe.
