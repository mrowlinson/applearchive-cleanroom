# PV-f8e426b b209 T10R144 n<=67892 (890 tiers): GREEN

- Parent first-hand, fresh detached tmp/wt-pv-f8e426b,
  TMPDIR NVME pv-f8e426b, 2026-10-17 ~23:55.
- C build -O2 -Wall -Wextra -std=c11: rc=0, 0 warnings.
- RGRAMC-PYID 4370/4370 covered=4370/4370 RGRAMC-GREEN.
- RGRAM-GREEN py + RGRAM-GREEN C (RGRAM_BIN=own build).
- SMOKE-GREEN 6/6 (aar+aea roundtrips).
- FAIL 0 (no FAIL lines in any log). Wall: lane-diff
  rgramc.c-only per GATE, wall 0.
- Verdict: GREEN. Merge-ready on VERIFY arrival (viewer3
  claim live, battery queued after b212). Oldest in queue:
  merges b209 first, then b210, then b212.
