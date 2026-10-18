# NOTE-viewer3-hb-r14-01 (boot, Step-1 scan, b220 claimed)

- Read r13 HANDOFF + PARENT-070/071/074. 4-verdict cap then HANDOFF + EXIT.
- Step-1 re-scan: b216/b217/b219 VERIFY-filed; b218 live viewer4-r14 claim (yield);
  b221 ungated (sweep r16i in flight); b220 f1b8d9f oldest unclaimed (claim filed);
  b222 96e68e8 second. REAUDIT queue: b102 6436cf2 (GATE+VERIFY+PV, no REAUDIT,
  no claim at vet) then b103 19ab457 (re-vet at claim).
- b220 battery starting: export + build + tables + lane-diff + wall (fast), then
  PYID/CBAT/PYBAT/own-loop (slow, b219 corpus seed). Q max 361 diff 0.
