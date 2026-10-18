# NOTE-092-sweep: coverage AUDIT — count drifted 17, true 107/107 substantive

- AUDIT (first-hand): every lane commit vs GATE provenance. w1 = 18, w2 =
  89 from base 0999654 (merge-base confirmed, no merges) = 107 TRUE.
  predecessor "77/77" @94-true era drifted -17 (range-gates undercounted);
  my "90/90" inherited it. counts were wrong, coverage is substantively
  COMPLETE: all 89 w2 + 16/18 w1 named in >=1 GATE file.
- GAP closed retrospective (this shift): dc87389 (adopt+harness+rawenc
  prototype+6-cell battery, 431 lines READ: black-box framing, libc-only
  xattrs, honest cmp tests) + 8a0a67e (put_int min-width + DEV/B/C/S +
  c9/c10 cells + units, READ: behavior-derived, honest). scans: dc87389
  artifact/CPAT/deps-CLEAN (implicit PASS); 8a0a67e CPAT/deps-clean BUT
  2 pyc IN TREE (rawenc pyc MODIFIED) = HISTORICAL-HYGIENE-FAIL, already
  remediated forward (8a79248, FLAG-CLEARED-w1-pyc). no action, recorded.
- CORRECTED BASELINE: 107/107 substantive (105 explicit-gate + 2
  retrospective-here), ZERO holds. future GATEs increment from 107.
  prior "N/90" lines stand as filed (superseeded by this NOTE).
