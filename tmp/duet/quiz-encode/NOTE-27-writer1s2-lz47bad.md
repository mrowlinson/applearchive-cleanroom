# NOTE-27 writer1s2 lz4: 7-bad taxonomy + dense-table status (heartbeat14)

- CORRECTED VERIFIER (proto/verify4.py, oracle-seq-driven dense sim Knuth-12 +
  interior mstart/+1/end-2/end-1-iff-next-lit): corpus 103 beds OK, 1125 matches,
  7 bad (each bed exactly 1). all 7 oracle matches VALID (bytes); fails = occupant
  divergence, never oracle literals => NO skipper evidence yet; dense holds.
- TAXONOMY: (a) +1-skipped x4 (k192/604, o4/319, q640/1613, SPAN2/401: src=mstart
  present, mstart+1 absent; ALL next-lit=0 chains) => +1 gate = next-has-lit?
  (b) end-1-skipped x1 (v1024/127, ml=4 BUT next-lit=11!) => end gate NOT
  next-has-lit; ml>=5? more data needed. (c) literal-skipped x3 (tiny/158,
  128/429, w8/750: single slot-mates, runs 5/600/600, into 1/225/548, prev ml
  4/6/6) => trigger unknown; 3 samples too few.
- NEXT: multi-frame verify (bis/wide 65K-200K beds => 10x matches, more skip
  samples + eviction/window data); gate ablation V1/V2/V3 by bad-count.
