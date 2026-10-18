# NOTE-w2s12-hb56: battery ~75%, R104/R105/R106 + P107/P108 mapped, Q-83..Q-87 filed

- Battery bat-w2s12-p105 ~75% (no FAILs in output so
  far — tail shows only PASS lines; final verdict at
  end). P105 commit on GREEN.
- R104 (53717..53972): 7B m-tab NEW + P106M-verbatim q
  16/16 (tails -> b72-75). Q-83.
- P107 (53973..54064): PB1 sig-migrant (P106-PBB-single
  sig), 3+1 quad, quad b5 carries at row edge. Q-84.
- R105 (54065..54320): 1st ARITHMETIC q-reuse —
  LE-u16 heads x2, tails verbatim, b34 = b46>>1 (or
  q-step, ambiguous). Q-85.
- P108 (54321..54412): P105M-layout PBA (0/16 overlap),
  1B-apart quad rows 0/1. Q-86.
- R106 (54413..54668): 7B m-tab NEW + P108M-verbatim q
  16/16. Q-87.
- No answers yet (Q-81..Q-87 open). Next: P109 census
  (PB1 54670 is 100B — 1st fat PB1?).
