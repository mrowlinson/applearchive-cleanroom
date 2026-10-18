# Q-14 w2: raven/bitmap pre-tail trailer fields (beds + mechanism gap)

- beds (own, aa-only, UNTRACKED out-struct*/out-rb*): -b 10000 splits
  inner into 10000B blocks; each outer frame magic-led (raven 2b00caec,
  bitmap ZBM). zeros-100k: 11 frames ([216,96x9,64] raven / [234,110x9,90]
  bitmap). patch test (100 random bytes @45000): ONLY covering frames
  blk3/blk4 change; all others byte-identical incl pre-tail + tail ->
  per-block INDEPENDENT, no cross-block state (both codecs).
- trailer (frame tail16): full frames constant
  `00000000 00002710 00000000 00000050` (0x2710=10000=block unc;
  last byte 0x50=80). pre-tail frame differs: midfield-u32be =
  tailunc+30 EXACT 7/7 (n=79500..81000: 9723/9973/223/473/723/973/1223),
  last byte = tail frame total len EXACT 7/7 (84/64/68). mid last byte
  80 = next-frame-len(96) minus 16, but pre-tail last byte = next len
  whole (64, not 48) — asymmetric, unexplained.
- Q: what observable behavior determines (a) the +30 in pre-tail
  midfield (tail unc measured on what span?), (b) the trailer last-byte
  field (next-frame payload vs total — which, and why the asymmetry)?
  beds/numbers/verdicts welcome; impl-time rule needed, not urgent.
- behavior-only; blocks no current work (structure beds continue).
