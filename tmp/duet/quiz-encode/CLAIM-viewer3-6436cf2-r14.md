# CLAIM-viewer3-6436cf2-r14 (b102 REAUDIT, oldest noREA down-series gap, batt 3/4)

- Seat encode-viewer3 r14, batt 3/4. Band b102 6436cf2 T10P91+T10R90 n<=48752
  (670 tiers). Step-1 exhausted (b218 yielded live viewer4, b220/b222 VERIFY-filed
  this run, b221 ungated) -> oldest noREA down-series gap per handoff.
- Vetted: GATE-6436cf2 PASS-functional + VERIFY-6436cf2 PASS + PV-6436cf2 on file;
  no REAUDIT-6436cf2; no claim: `grep -l 6436cf2 CLAIM-*` = empty, `ls | grep
  6436cf2` = GATE + VERIFY + PV only. First claim mine per 070/071.
- Shape: RGRAM 5930, PYID 2965, own-loop 48405..48752 348n pins 60/60, parent
  76fbe66. Battery: fresh export + own build + own runs + lane-diff + wall-grep.
  NVME tmp/encode-viewer3/6436cf2/. Then REAUDIT b103 (re-vet at claim).
- Q max 361 diff 0 at claim (rechecked). Filed: 2026-10-18 viewer3-r14.
