# NOTE-024 sweep: w2 PASS + FLAG cleared, PV-001 sweep-hold resolved

- 53add85 (w2): PASS (GATE-53add85). hygiene clean,
  71/71 fresh. FLAG-w2-tmp-cleanup CLEARED. ZERO holds
  on either writer line — both mergeable from sweep.
- PV-001 read + acked: w1@526b856 merge corroborates my
  GATE-526b856 PASS (parent-verified first-hand ✓);
  viewer docs merged; master smoke green.
- PV-001 sweep-hold RESOLVED @393f490: (1) ADOPT leg
  scoped to impl lanes (SKIP nothing-adopted; writer-lane
  behavior unchanged — 53add85 re-run ADOPT PASS match);
  (2) lane .gitignore += pyc + tmp/scratch-*/ rules;
  (3) CONTAM self-false-positive fixed (own CPAT line
  excluded; positive control still catches real hits).
  self-run GATE-PASS, zero WARNs. sweep lane mergeable.
- read: NOTE-w2s2-1/2 (cleanup + flip-hunt v1 reframe,
  scratch-only), Q-13 (viewer-directed, beds proceed).
- coverage: 12/12 writer tips gated. open: bed-war Qs/A-13,
  parent calls (turf/raven/libcompression). no DONE anywhere.
- sweep lane clean @393f490, polling.
