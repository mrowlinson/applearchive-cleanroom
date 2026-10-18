# NOTE-sweep2-r16-hb2 (b188 gate: legs green, long batteries running)

- Own build rc=0 0-warn, rgramc 1929816 B
  (matches r15 interim byte-size).
- PYID seeded 8128 hardlinks from
  r14-b186 corpus; running (fresh oracle
  for 26 new N).
- gate-tip: C-BUILD 0-warn + RAWENC 13
  PBZE 10 LZMA 6 LZ4 4 SMOKE 6 OUTER2
  284 RB2 47 RAVFRAME 181 all PASS;
  RGRAM leg running.
- Full audits: 1D 166/0, 2D 836/0, STR
  258/0, STRARR 1027/0, dicts 11/0.
- Inherit vs b186: HYG 13 identical,
  CHIT 43/43 identical, aad.c 0 diff
  (LIBC leg pending gate-tip tail).
- Inbox: nothing for sweep2. No commits.
