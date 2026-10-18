# NOTE-sweep-r5-parked: 1/2 gates filed, parking for refill (r5)

- Seat encode-sweep r5 parking after ~90min with no second
  odd cut (brief step 3). Fresh refill takes the seat.
- GATED: b173 2205fa1 PASS-functional (GATE-2205fa1.md;
  seat logs r5-2205fa1* under NVME encode-sweep). Claim
  CLAIM-sweep-2205fa1.md stays (battery record, not live).
- Interim: odd-band fresh-oracle re-audits b145-b171 filed
  (NOTE-sweep-r5-audit-bNNN, 14/14 GREEN 256/0 + pins N/N;
  logs NVME encode-sweep/r5-audit-bNNN/). Generic rerun:
  NVME encode-sweep/r5-audit-band.sh <sha> <prev> <lo> <hi>.
- Next odd for refill: b175 T10R127 (w2-merge 394b22e staged
  n<=61976 +22 pins; C-port cut verifying at cport per hb77,
  imminent at park time). Claim oldest-ungated-odd on wake.
- Evens (sweep2 turf) still ungated: b166/168/170/172/174.
  No sweep inbox traffic at park; PARENT-066 read (no turf
  change). No commits, no pushes (quiz records only).
