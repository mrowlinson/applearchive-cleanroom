# NOTE-scout-r1-08: r1 charter COMPLETE (round 10) — entering poll loop

## Checklist vs PARENT-067 charter (all three work items done)
1. Vendor-doc + OSS container survey: NOTE-02 (theapplewiki framing/
   TYP table, Eclectic Light battery edges, man-field flags incl
   SIZ-confirm + SH2/IDX/IDZ/SLC, dev-docs fetch-limited) + NOTE-03
   (link re-verify, Apple-404 HOLDS, lzraven leads wall-flagged,
   compression_tool codec framings) + NOTE-05 §B (`aa -h` field
   vocab, TYP 9-vs-11 discrepancy).
2. Fixture inventory: NOTE-04 (selfgen pins re-verified PASS, WS
   scratch counted 70/13501/2172 unpinned, T1/T2/T3 generation plan,
   DRIFT-FAIL restated). Hashes-not-bytes honored; zero vendor bytes.
3. Harness skeleton on lane: b53969c LOCAL ONLY lanes/encode-
   container (adapter stub + tests/container T0 5 cells + entry
   point). T0-CONTAINER GREEN x2 first-hand. NOTE-05 filed.
Bonus probes: NOTE-06 (header walk 82/98/99, 36B framing, pbz*
census, SLC resolved, list-json golden) + NOTE-07 (TYP 7 confirmed,
h/m/WRT open, fifo-block + single-entry edges).

## Hygiene verified (round 9)
- Lane worktree clean @b53969c; master untouched (only ?? tmp/
  scratch); nothing pushed; no map-lane reads; TMPDIR on NVME.
- Quiz inbox every round: no scout Qs answered-or-owed (map-turf
  only, other seats draining). Heartbeats 01-06 filed per ~10 calls.

## Stay-alive
- Entering sleep-60/poll loop. Polls check: scout Qs (answer iff
  in-charter), joint DONE (exit + remove claim), parent PROD.
- Claim tmp/duet/CLAIM-encode-container.md HELD until joint DONE.
