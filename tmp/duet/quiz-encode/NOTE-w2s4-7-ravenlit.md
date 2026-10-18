# NOTE-w2s4-7 writer2: raven frames closed, literals transformed

- FRAME model CLOSED 6/6 (parse consumes exactly to trailer):
  512K cap EXACT (524288 single max; 524289 splits 512K+1);
  1M = 2x512K; 1.1M = 3 frames. cont-hdr = 4B F3-style
  (75712*4096+1 EXACT). F2(200K)=0x1c REAL (3 seeds);
  24->28 transition in (196608,199999].
- PAYLOAD probes (128B zeros + 1x0xAA @P): 0xAA NEVER appears
  in ANY payload (literals transformed, not raw LZ4-style).
  pos127: LOCAL 4B diff (29,30,40,41), same len. pos63/64:
  +4B (match split). pos0-9: same len, global resync BUT
  neighbor-D (p7 vs p8) = 2 BYTES (26,38) -> POSITION field
  local; EXISTENCE = restructure. 7/8/9 NOT identical (trunc
  artifact corrected).
- zeros 64..768 payload CONSTANT 44B (length in-field:
  W1=2N-127 linear, W7 stepped-16, W8B2 mod-16); shape flips
  in (96,128]. payload word/bitstream structure TBD.
- next: VALUE sweep (pos8 x 00/01/02/7f/80/ff) -> value field;
  POS sweep 0..20 (position bytes); then offset/len titration.
  Q-17/18 open. claim HELD.
