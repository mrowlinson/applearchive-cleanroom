# NOTE-viewer2-hb-r8-02

- Tables-EQ r8 re-run: 2/2 GREEN (M 16/16,
  C 67/67 pairs, C_N=67 row-consistent).
  16 T10R134 refs in rgramc.c.
- Own-loop r8 (r8 bin, fresh oracle
  64157..64412): 256 pass / 0 fail,
  pins 11 cells x2 = 22/22 (fresh .rav
  sha match PINS). OWNLOOP-GREEN rc=0.
- Diff vs parent d335153: src/c/rgramc.c
  ONLY (+1220/-1061); py+PINS+tests
  byte-identical.
- Wall-grep rgramc.c (PARENT-032 scope):
  0 hits.
- Quiz: still max Q-361, A-361 confirms
  Q-361 first-hand; diff 0, nothing owed.
- Gate: no GATE-fac36c9 yet (sweep-r13
  running); VERIFY held.
- PYID running in background (r8 bin,
  work-pyid reuse + oracle growth).
  Next: collect PYID, run CBAT/PYBAT.
