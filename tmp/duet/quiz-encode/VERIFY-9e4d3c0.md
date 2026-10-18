# VERIFY-9e4d3c0: PASS (UNC cells; verdict correct, prose corrected by A-14)

- scope first-hand: tests +25 (UNC helper + 4 calls), pins +8. additive.
- code: UNC walks header chain on fresh oracle bytes (BE unpack, zero-asserts, chain-end exact) —
  honest. NOTE: helper encodes `inner=len(raw)-28` + `su-28==inner`, which A-14 corrects in prose
  (no +28 in format; check ⟺ su==len(raw), verdict TRUE). pins/verdict stable, no code change needed.
- wall: 0 hits (own grep). concur GATE-9e4d3c0 PASS (115/115).
