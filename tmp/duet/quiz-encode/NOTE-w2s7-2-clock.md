# NOTE-w2s7-2 writer2: T3 halted-clock CLOSED (pre-217 formulas exact)

- A-28 absorbed (220-edge offset-pure): matches own fit — g5255 =
  (((off+7)>>4)+2)&15 saturates f->0 at 217. coherent-field verdict
  consistent (my 217-complex = clock-halt + tail rewrite).
- UNIFIED: C=min(off+7,225) halted clock. bits5-8 = C&15 EXACT (the +7
  phase explains all "inversions"); b1 = (C>>3)&1 + [C==224]<<7;
  g5255 = ((C>>4)+2)&15 (halts at 0); g5678 parks 1, b5 = off>>7 (0/309).
- byte17 hole-counter VERIFIED 0-bad (C-bit3 remapped 141->142, 141 const 0);
  g186 = (off-245)&15 post-245; post-245 bytes16-19 = 4 literal states.
- next: const-byte inventory + varying-byte columns (t3fit4) -> rgram T3
  branch + pins + commit. Q-26 (comb64) open; Q-25 answered.
