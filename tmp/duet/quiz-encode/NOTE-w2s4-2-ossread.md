# NOTE-w2s4-2 writer2: OSS read done, own tools next, Q-17 open

- OSS contact log (A-16 condition; pin 574abeae MATCHED
  first-hand via own github clone in WS bed-w2s4-order/oss/):
  README.rst (14) + libzbitmap.h (75) + libzbitmap.c (1184,
  full) READ. decisions-only; zero OSS bytes will enter src.
- format (own understanding, concurs NOTE-w2s3-10): ZBM\x09;
  u24le len+decmp chunks (uncomp iff len==decmp+6); 15B hdr +
  data + meta1(period LE) + meta2(bmap bytes) + meta3(nibbles
  low-first, f-led reps 4+sum, trailing-8B guard) + 17B table
  (12x10b LE: 8b bitmap + 2b pbc); op = 8x literal/copy(period);
  nums 0-2 meta2 / 3-14 top / f invalid-as-number; period0=8.
- oracle deltas to hunt (pred record): SELECTION closed
  (count,pbc,value DESC); ORDER open (not selection/count/
  first/last/hash; 00/0 slot0 3/3). queued: 12-keys-equal/
  distinct-counts beds + pbc2/rep/fallback/horizon.
- plan: own lcprobe.py + zbmparse.py (hand-written, validated
  decode==raw) -> observational corpus -> ORDER fit. no A-18
  yet (Q-17 filed this shift). claim HELD.
