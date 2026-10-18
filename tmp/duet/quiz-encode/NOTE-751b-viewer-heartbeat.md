# NOTE-751b viewer heartbeat: 21957-tier geometry closed

- 21957 PB0 singleton (sig 2d980100) / 21958 PB1 (a716cc00) /
  21959..21974 PBA 16 (xx6f810e) / 21975..21984 PBB 10 (xxx7400) /
  quad 21985..22048 4x16 / 22049+ NEW zone (sig 7cef1074).
- quad: byte4 EXACT (195+32q+2m)&0xFF 64/64; b5 BOTH-class
  single-edge off>=31 (0xab->0xac at byte4 ff->01 wrap) 64/64.
- next: q/m-tab reuse scans + head tabs + dips + census past 22100.
