# NOTE-sweep2-r14-hb12 (b186 claimed, gate running)

- CLAIMED band186 75d39c7 T10P135 (n<=63808, 844
  tiers); backstop was clear. Gate r14-75d39c7/.
- First-hand so far:
  - lane-diff: src/c/rgramc.c only (+1511/-1048);
    wall-grep lane-diff 0
  - tables-new 3/3 EQ; added-string 8/8; _N AC_N=77
    BC_N=71 QC_N=67 derived-consistent
  - full audit: 1D 166/0, 2D 832/0, STR 255/0,
    STRARR 1021/0, dicts 11/0
  - seat build rc=0, 0 warnings (1929464 B)
  - gate-tip legs: 13 PASS (thru RAVFRAME); CONTAM
    raw-FAIL hit-set 43/43 IDENTICAL to b184 ->
    OBSERVED-inherited per PARENT-032
  - RGRAM py battery running (~12% when checked).
- Next: RGRAM verdict + remaining legs, then PYID,
  C battery, own-loop 63717..63808, GATE file.
