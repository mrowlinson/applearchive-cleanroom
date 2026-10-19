# PARENT-RANGE-01 (parent, 2026-10-19): parallel P-writers by range

Binding constraint was one P-writer (~0.6 tiers/h vs ~1300
tiers left). Ranges now (scope per MEMO-SCOPE-01-VERIFY):

- w2b lanes/encode-writer2b: P181-500 (continues, in-flight ok)
- w2d lanes/encode-writer2d: P501-850 (new, from P180 tip)
- w2e lanes/encode-writer2e: P851-1200 (new, from P180 tip)
- w2f lanes/encode-writer2f: P1201-1458 (new, from P180 tip)
- w2 lanes/encode-writer2: R176-R189, then converts to P
  overflow/audit (separate order at R189).

Rules:
1. No tier outside your range. Ever. Overlap = DROP.
2. NO-WAIT memo protocol (replaces ask-and-wait): file Q per
   tier, proceed IMMEDIATELY with own first-hand census.
   Commit tier when own census + RECORD + VERIFY + SMOKE all
   green. Memo CONFIRMs async; any memo DISSENT reopens the
   tier (rework before cport takes it). Cport ports ONLY
   tiers with memo CONFIRM on file. Two-eyes gate preserved,
   moved to cport boundary instead of blocking writers.
3. CT shim MANDATORY in all batteries (PARENT-CT-CACHE-01).
4. Cap 8 tiers/round, heartbeat every ~30min, HANDOFF + EXIT
   per PARENT-074 at cap.
5. N-start formula P_start(P)=83553+(P-192)*348 (verified at
   samples, NOT every tier): oracle-probe your range's FIRST
   tier start before bulk; any mismatch = halt range + Q.
6. Records shape unchanged (rgram.py tables + PINS rows +
   VERIFY 0 FAIL + SMOKE-GREEN per commit). Gaps between
   ranges are EXPECTED on range lanes; assembly in tier
   order is cport's job (partial-merge procedure, tiers in
   order, full battery per band as today).
