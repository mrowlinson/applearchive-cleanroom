# PV-1a423eb b218 T10P151 n<=69376 (908 tiers): GREEN

- Parent first-hand, pv-band.sh (slow legs; fast battery
  landed after this run started), TMPDIR
  /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-1a423eb,
  fresh detached worktree. 2026-10-19.
- C build: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings.
- RGRAMC-PYID 4498/4498 covered=4498/4498, RGRAMC-GREEN.
- RGRAM py + C: RGRAM-GREEN (8996/8996 each, set-eq).
- SMOKE: aar+aea roundtrips all PASS, SMOKE-GREEN.
- Wall: lane.diff grep 0 hits outside FPs.
- Chain: GATE-1a423eb PASS-functional (sweep2-r27) +
  VERIFY-1a423eb PASS (parent outage-cover, same run
  evidence + independent GATE) = MERGEABLE oldest-first.
