# PRE-181b 80: mark-dip1 54/54 @35877 + chain (frontier stage)

## census (v5d47 first-hand, 255x80B + 1x76B, nvar=77)
- 348-mark 54/54 @35877 as DIP1 (single 76B row).
- quiet bands ..35876 (b0 04).
- chain: 35878 (b0 04, 55-flip in other bytes!) ->
  35879..35894 (b0 47) -> 35895..35904 (b0 02, chatter)
  -> 35905..35968 (b0 23; 43@35905; bands) -> 35969+
  (b0 3a; 53-flip; dense 4-cadence).
- b5 18->19 @35968 ->1a @36096.
- split: ..35876 / 35877 / 35878..35894 / 35895..35904
  / 35905..35968 / 35969... next mark: 36225.
