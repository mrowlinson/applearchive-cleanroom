# NOTE-sweep2-r18-hb4 (mid-range second pass b40 b60 GREEN)

- PARENT-071 consumed: claim check
  before re-audits. Band CLAIM files
  cover head bands only (b164-b190 +
  b168-b186 evens); floor + mid-range
  clear. Skipping b160 (stale CLAIM-
  sweep2-5edb95d on file) per advisory.
  PARENT-069/070 read, no gate impact.
- b40 1b84bca 31445..31700: 256/0
  pins 20/20. b60 8255033
  35905..36252: 348/0 pins 40/40.
  Builds rc=0 0-warn, fresh oracle.
- Run total: 4424 N green, pins
  1940/1940, 10 builds 0-warn. Zero
  discrepancies.
- Cport tip still 05efb6d (no b192).
  Quiz diff 0. No commits.
- Next: b80 9c4264a 41125..41472.
