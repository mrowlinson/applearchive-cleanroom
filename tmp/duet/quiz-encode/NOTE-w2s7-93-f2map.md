# NOTE-w2s7-93-f2map (encode-writer2, own-side heartbeat)

- 9 own calls this segment. 68-tier map extends:
- F2 storm 14286..14329: A 15-row (b40-43,47,52,53m) + s14301/02/03 + B 15-row (b49,50,b52-55) + s14319 + C 9-row (b48-51,b56-59) + s14329.
- FQ 52-row 14330..14381, 6B-ish tab b6,b60-63 (+b5 per-block, words b48-51,b56-59).
- G1 11-row 14382..14392 (b5,6,b60-63 walk); G2 quiet-16 14393.. (6B tab b10,11,b64-67; 6+ blocks, dump extends past 14500).
- Flips confirm boundaries: 14301/02/03, 14319, 14329, 14393, then per-16 heads.
- Next: T9F2 + T9F2Q chips, then G1/G2.
