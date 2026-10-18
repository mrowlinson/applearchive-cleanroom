# CLAIM-viewer3-e25ae48-r13 (b100 REAUDIT, oldest noREA gap, batt 1/4)

- Seat encode-viewer3 r13, batt 1/4. Band b100 e25ae48 T10P89+T10R88 n<=48056 (662 tiers).
- Vetted per 071: GATE-e25ae48 PASS-functional + VERIFY-e25ae48 PASS + PV-e25ae48 on file; no REAUDIT-e25ae48; no live claim (`ls` GATE/VERIFY/REAUDIT/PV/CLAIM*e25ae48* = GATE+VERIFY+PV only; full CLAIM head: no e25ae48 entry). Oldest noREA down-series gap (REAUDIT frontier b110-b132 except b111/b112/b116; b112/b116 live viewer2-r15; b100-b109 + b111 claim-free, b100 oldest). Same-shape band (RGRAM 5808, PYID 2904, own-loop 47709..48056 348n pins 46/46).
- Battery: fresh git-archive export + own build (-O2 -Wall -Wextra -std=c11) + own runs (PYID/CBAT/PYBAT/set-eq/own-loop/tables-EQ) + lane-diff vs 2d41980 + wall-grep. First-hand only, all data NVME tmp/encode-viewer3/e25ae48/.
- Q max 361 diff 0 at claim. Filed: 2026-10-18 viewer3-r13.
