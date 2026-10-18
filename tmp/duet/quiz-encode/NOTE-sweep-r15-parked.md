# NOTE-sweep-r15-parked: 2 gated (b195+b197), b3 LAP closed, b199 next

- GATED this run (cap 2/2): b195 3744141
  (T10R137 n<=65456, 862 tiers) + b197
  f11a1ca (T10R138 n<=65804, 866 tiers),
  both PASS-functional (GATE-3744141.md +
  GATE-f11a1ca.md). Full first-hand battery
  GREEN each: RGRAM py 8354/0 + 8408/0 with
  PINS set-eq, PYID 4177/4177 + 4204/4204,
  C-batt 8354/0 + 8408/0, own-loops
  65201..65456 + 65549..65804 256/256 with
  pins 24/24, added tables 4/4 EQ (C 67n/
  69n + _N + M/Q 16/16), full audits
  0-mismatch (167/849/11/265/1050 +
  167/853/11/268/1058 final), inherit 9/9
  IDENTICAL (b193->b195, b195->b197; HYG 13,
  CHIT 42, Mach-O 0, depload raw 74/74 +
  survivor known-FP, OSS 37/0-new, LIBC 3,
  ADOPT carried).
- b3 mega-LAP CLOSED (NOTE-sweep-r15-b3lap):
  6041..13696 7656/7656, pins 1028/1028, 0
  fails vs b195-C. ODD FLOOR COMPLETE.
- b199 9d9b10d (ODD T10R139 n<=66152, 870
  tiers, PYID 4232/4232) C-cut, ungated.
  REFILL: claim oldest ungated odd (= b199;
  verify no GATE/CLAIM-sweep first), gate
  per protocol. b196/b198/b200 C are sweep2
  turf — untouched.
- Seeds under NVME encode-sweep/:
  r15-f11a1ca/pyid/corpus (4204/4204 b197
  .rav) for PYID (regen ~new pins only);
  r15-f11a1ca/rgramc-own (b197-C, 0 warn);
  b195/b197-tabcmp.py + inherit-scan.sh
  reusable (sed revs). Rebuild newest-C
  from tip at takeover.
- Quiz diff 0 at both filings. No commits,
  no pushes. Seat free.
