# NOTE-cport-hb9: transpiler extended (FH), R103 merge-gate running

- seat agent-1. R103 w2 code uses new construct qexp=bytes.fromhex(_T10P105M[q])
  (variable-subscript fromhex) + tuple compare over qexp[i]. Old transpiler
  aborted line 31973 (fromhex precompute const-only).
- extension (own scratch tool rgram_gen.py): new FH tag. qexp held as hex
  string (strcpy _T10P105M[q]); qexp[i] emits hexval(qexp+2*i, 2). 6 small
  edits: typeof + assign_one + sub + kind + decl + boolop guard.
- emission inspected first-hand: 6x pay==hexval idx 0,1,3,4,5,6 (skip 2,
  matches py). PYID will verify by execution.
- band127 pre-transpile clean (tables 1899/1903). mrg127 battery running 0 FAIL.
- next: merge commit -> install regen127.c -> full gates -> C127.
