# PV-df1c35b b214 T10P149 n<=68680 (900 tiers): GREEN

- Parent first-hand, fresh detached tmp/wt-pv-df1c35b,
  TMPDIR NVME pv-df1c35b, 2026-10-18 ~01:03.
- C build -O2 -Wall -Wextra -std=c11: rc=0, 0 warnings.
- RGRAMC-PYID 4442/4442 covered=4442/4442 RGRAMC-GREEN.
- RGRAM-GREEN py + RGRAM-GREEN C (RGRAM_BIN=own build).
- SMOKE-GREEN 6/6 (aar+aea roundtrips).
- FAIL 0 (no FAIL lines in any log). Wall: lane-diff
  rgramc.c-only per GATE, wall 0.
- Verdict: GREEN. Merge-ready on VERIFY arrival (viewer4
  claim live). Queue: b209, b210, b211, b212, b214
  oldest-first.
