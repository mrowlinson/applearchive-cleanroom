# NOTE-16 writer1s2: RULE-EXT v2 (14/14), framing CLOSED, search-limit found

- RULE-EXT v2 (all fit): initial 4B + do-while 8B steps
  (match? p+=8 : byte-fixup-to-mismatch DONE); stop when
  p+8 > chunklen-121 (NO fixup at bound). >=1 step always
  attempted (tail-132 match@(0,12) overshoots 11!). closed
  form: mend = largest mstart+4+8K with (K=0 or step taken);
  bound-stop mend+8 > chunklen-121; mismatch-stop exact.
- framing CLOSED: chunks@64KB; chunk>=128 + 15/16-pass ->
  bv41+u32u+u32c+blk; chunk<128 (EXACT threshold, bisected
  127/128) or 15/16-fail -> bv4-+u32+raw (mid-stream OK,
  bodies byte-EQ raw); terminal bv4$ always; all-stored
  block -> outer-store (no frames). single-chunk 15/16
  proven on CHUNK comp (r4 razor kills payload-size alt).
- bv4- header CORRECTED (in-test): 8B (magic+u32 unc), NOT
  12B — the "c3=0" was raw zeros; terminal $ present.
- RULE-SEARCH-LIMIT (candidate): no match starts at pos >=
  chunklen-128 (TailS4 1099 allowed / TailS5 1123 refused;
  exact boundary in (1099,1123], bisect queued). tiny-chunk
  min-128 rule CONSISTENT (no starts possible -> store).
- gap: g-lz4hunt search-model OPEN (hash/skip/table/dict);
  queued: limit-bisect, F1b (200B random tail -> bv4-?),
  dict-init probes. lzma untouched.
- read: GATE-526b856 PASS (mine, 13/13 both, LIBCOMP leg
  live), NOTE-022b, NOTE-023. w1 clear, 4 straight PASS.
