# NOTE-119b viewer: c-seat N∧S tension RESOLVED (5 guilty grams in 6 chunks)

- reproduced c-seat set0 bed first-hand (PRE seed-51, NEU filler,
  6 chunks @819/898/1009/1010/1350/1423): base=MISS ✓ (their
  bed verified). apparatus v4q30d.py (scratch-viewer6).
- per-byte mutant scan (mates + 4B junctions, xor-01): exactly
  FIVE guilty width-4 runs, all ->FIRES: b074e265@6664,
  e389383d@7294, 7e011894@8187, f5ec9105@10908, 8e75a59d@11495.
  all distinct + !=T4 (94dd1fa9) + occ_before=-1. 10/10 NEU
  sample flips stay MISS.
- resolution: their N=6 counts 8B CHUNKS; guilty units are 4B
  GRAMS. chunks 1009+1010 (adjacent) share ONE junctional
  guilty gram (7e011894 = mate1009[7]+mate1010[0:3]). 6 chunks
  carry exactly 5 guilty grams => S=5 overflow EXACT. no need
  for S-up-to-9 / multi-bucket / refresh-kill (their a/b/c).
- refinement to their mutant read: guilty window position VARIES
  (chunk bytes 4-7 / 2-5 / junction / 0-3 / 3-6). "bytes 0-3
  inert" is mate0-specific (mate@1350 guilty = bytes 0-3).
  general rule: killing insert = the guilty 4-gram wherever it
  sits (sliding width-4 inserts, content-keyed).
- net: both A-37s stand and AGREE (5-set atom, width-4, cover
  criterion). w1 fit: 25 co-bucketing 4-grams total (my 20 +
  these 5) across 5 independent T's.
