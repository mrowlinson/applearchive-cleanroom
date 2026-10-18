# PRE-178b 80: mark-dip1 52/52 @35181 + dip10 (frontier stage)

## census (v5d44 first-hand, 245x80B + 11x76B, nvar=73)
- 348-mark 52/52 @35181 as DIP1 (single 76B row).
- bands 16-step ..35180 (b0 98).
- bridge 35182..35198 (b0 01->13; 48-flip @35182).
- DIP10 35199..35208 (39-flip @35209 exit).
- body 35209..35272 (b0 08; bands) -> frameswap @35273
  (b0 85; 48-flip).
- b5 12->13 @35209 ->14 @35328.
- split: ..35180 / 35181 / 35182..35198 / 35199..35208
  / 35209..35272 / 35273... next mark: 35529.
