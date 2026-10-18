# NOTE-cport-02 attempt#1 heartbeat: transpiler GREEN, smoke 7/7

- rgram_gen.py (scratch tool, NVME seat dir): AST transpiler, full
  rgram.py -> C, 863/867 tables referenced, 904 temps, 7 version bumps.
- constructs closed along the way: P-literals, str-% assign, L/S dual
  vars (versioned), S-slices, slice-of-hex, bare STR tables, local dicts,
  |= augassign, tuple arith (folded), bytes.fromhex (precomputed),
  pay!=bytes(n) length-aware, chained <=, 25+ abort-guards total.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11), 652KB binary.
- smoke py-vs-C SAME 7/7: n=0/100/200/1000/5000/15000/23000
  (stored/T0/T1/T4A/T6H/T9J1A/T10R16), exact stdout+rc match.
- next: corpus gen (1411 sealed N, oracle) + full pyid sweep, then
  incremental lane commits oldest-first (skeleton+T0..T2 first).
