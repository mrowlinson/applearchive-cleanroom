# NOTE-sweep2-r14-hb2 (interim audits green, b186 uncut)

- Cport tip still 7c2e8d4 b185. No even to gate.
- Interim first-hand (seat-private b184 build, 0
  warnings, rgramc 1912584B = r13 byte-size):
  - own-loop ext1 63113..63460: 348/0, pins 48/48
  - own-loop ext2 62765..63112: 348/0, pins 48/48
  - tables re-audit b184: 1D 166/0, 2D 828/0,
    STR 252/0, STRARR 1015/0, dicts 11/0 —
    all match GATE-a31520e exactly.
- Next: b182-tree regression span + _N row-count
  re-verify; keep polling for b186.
