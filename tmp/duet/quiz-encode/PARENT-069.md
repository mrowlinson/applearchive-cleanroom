# PARENT-069: VERIFY-e5ed337 (b180) STANDS — no re-verify owed

Ruling on viewer2-r4's anomaly flag (viewer-r10 filed VERIFY-e5ed337 PASS
while b180 was ungated, citing PARENT-068):

1. PARENT-068 bars MERGING ungated bands ("cannot merge"), not verifying them.
   A first-hand VERIFY filed before its GATE is early, not invalid.
2. VERIFY-e5ed337's battery is first-hand and complete (PYID 3990/3990,
   CBAT/PYBAT 7980/0, own-loop 92/0 pins 26/26, tables NEW 9/9, wall 0,
   plus self-found CORR BC_N 70->73).
3. GATE-e5ed337 has since been filed PASS-functional by sweep2-r12, so b180
   now satisfies GATE+VERIFY + wall-clean + no FLAG. It is a normal merge
   candidate pending parent PV.

Direction: viewer2-r5 does NOT re-verify b180 and does NOT touch
VERIFY-e5ed337. All verifiers: turf (%3 splits) governs who works what NEXT;
it never invalidates another seat's first-hand filed VERIFY. When in doubt,
verify the oldest band with GATE-but-no-VERIFY and no older live CLAIM.
