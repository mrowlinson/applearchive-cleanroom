# A-30 bucket mates: 4 sets x 5 same-bucket 4-grams (Q-30 CLOSED)

## sets (each: 5 distinct grams share T's bucket; jointly evict at LOW N)
- T501 T8=9b23b85ea9b4b536 T4=9b23b85e N=56: 9d345fdb@115
  ff943e52@128 6def5bf3@136 9f0ddba9@147 68bb4e34@158
- T502 T8=3973713227fb21a5 T4=39737132 N=40: 20aee3e0@111
  c00cacd5@118 9cd5c3b8@128 e1cd9512@133 823b3476@143
- T503 T8=edfed5f66ab55eba T4=edfed5f6 N=48: f430961a@112
  12da3bc1@120 23512b8a@131 31a13e60@144 6bf9edfe@154
- T504 T8=2271fcafac226608 T4=2271fcaf N=56: 07910a99@113
  0f8f6fca@124 b4ee3229@137 182d6c42@150 4d086f37@160

## why these are mates (not artifacts)
- each set 1-minimal: flipping ANY guilty byte restores T firing
  (full-filler mutant scan: exactly 5 guilty 4-runs per set, all
  other bytes innocent). 5 mates + T = 6 keys > 5 slots => T out.
- no consumption: covering_p empty all 4 (near match only TAIL
  zeros at p+9). all 20 grams hist_occ=[] (never seen before).
- all 20 distinct from each other + from T4 (distinct keys ✓).
- guilty runs are width-4 => hash width 4 STRONG (T502 pattern
  provably excludes width>=5: guilty 111-114 excl 110+115).
- S=5 CONFIRMED mechanistically (A-33 fit now has ground truth).

## 1-byte mutant (asked: in-bucket or not)
- guilty-byte flip => that gram LEAVES bucket => 4 mates + T = 5
  keys fit => T FIRES. e.g. T502 mate@111 20aee3e0 flip b0
  (20->df): fires. all 80 guilty bytes behave so; all 120
  non-guilty bytes keep evicting when flipped.

## repro shape (v4q28b apparatus + PRE seed)
- PRE=Random(pseed).randbytes(108) pseed=501..504, T=PRE[100:108],
  filler=concat of mate chunks (8B each, hex below), TAIL=2000
  zeros; query m.get(108+len(filler)).
- F501=e315f3f2bbf3ff9d345fdb77b2762460b256f0e8ff943e52
  0f8a666a6def5bf3dc58a566940ce99f0ddba94ce1d48605
  f66968bb4e34ebfc
- F502=fc426620aee3e0e4ebbac00cacd5e39724afc3c69cd5c3b8
  0ee1cd95127fe225716029823b3476ba
- F503=4c2a7cdaf430961a54ac963a12da3bc122272d599c9e2123
  512b8abbed93c978b366046b31a13e60e830203b31e66bf9
- F504=244818afc407910a991f934254f351970f8f6fcad19a6797
  50d82c0b49b4ee32679283df53146832d61182d6c428047
  6ce975654d086f37
- method note: 5th candidate (T505) DISCARDED — junction gram
  matched history@99 (len-9 off-16 covering p): consumption,
  not eviction. ddmin can select consumption; all delivered
  sets pass covering_p + occ checks.
- apparatus: v4q30.py (ddmin-lite 12K->40..56B, 778 encodes) +
  v4q30b.py (dump+scan) + v4q30c.py, oracle compression_tool
  -a lz4. Q-30 CLOSED.
