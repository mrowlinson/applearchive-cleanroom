# NOTE-009 viewer: btime-follows-mtime (OS invariant) — pins regenerable, CTM closed

## Beds (first-hand, stat + python os.stat)
- utime(ns) mtime->2020 past: btime FOLLOWED (b=m=1600000000.123 exactly). same for touch -t past (b=m=2021).
- touch -m future (2030): btime stays live-now, mtime 2030.
- invariant (OS-enforced, APFS): btime <= mtime ALWAYS. setting mtime into the past clamps btime down to it.

## Verdicts
- CTM=btime CLOSED (writer impl correct). my withdrawn min() is observably identical given b<=m — no bed can separate them. no further probes needed.
- writer pins REGENERABLE (re sweep NOTE-004 worry): test_rawenc.sh fixes mtimes to 2001-past via touch -d
  (own read of committed script) -> btime deterministically 2001 too -> CTM pinned. "live-btime" applies
  ONLY to live-mtime inputs, which pinned cells never use. sweep's fresh-run-sha-vs-pin check will CONFIRM.
- A-6 CTM struck-record stands (NOTE-006, which IS in quiz-encode as NOTE-006-viewer-corrections.md, filed
  ~17:00 — sweep's listing predates it).

## Tie (==) micro-gap (writer NOTE-6): OPEN, acknowledged
- exact 16*comp == 15*unc never observed by either side. <= assumed compress. hunting it needs tuned beds;
  queued behind alg coverage. writer proceeds with <=.
