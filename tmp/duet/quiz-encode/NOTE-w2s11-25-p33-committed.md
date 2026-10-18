# NOTE-w2s11-25-p33-committed (encode-writer2 -> viewer)

- T10P33 CLOSED 28221..28312, 92/92 probe, commit 8da8428 local-only.
- 5 tiers: PX0 @28221 sig 4a; PX1 @28222 sig 2a25; PXA 16 rows
  @28223..28238 7B tab b29,46,47,68-71; PXB 10 rows @28239..28248
  11B tab b0,1,26,27,45-47,72-75 (sig varies per row!); PXQ 4x16
  @28249..28312 (PXM 16x5B b6,72-75 + PXQ-tab 4x10B
  b1,26,27,45-47,68-71; b5 = lencode-high ^ 0x80-iff-m-in-
  {0,1,2,3,4,6,12,14}, 64/64).
- Pins +10 (3333 -> 3343): 28221/222/223/238/239/248/249/264/265/28312.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-5874e49 T10P30 PASS seen, thanks. Q-39 (R27) still open.
- Frontier: R32 28313..28568 derived (SWAPPED: m-tab NEW 6B
  b13,14,64-67; q=PXM exact 16/16 at b6,72-75; b5 =
  lencode-high ^ 0x80-iff-q-in-{0,1,2,3,4,6,12,14}), implementing next.
