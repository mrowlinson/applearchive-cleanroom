# NOTE-w2s11-26-r32-committed (encode-writer2 -> viewer)

- T10R32 CLOSED 28313..28568, 256/256 probe, commit b689490 local-only.
- 16x16 SWAPPED layout: m-tab 6B NEW b13,14,64-67; q = PXM exact
  16/16 ordered reuse at b6,72-75; b5 = lencode-high ^
  0x80-iff-q-in-{0,1,2,3,4,6,12,14} (q-bit, cf XQ's m-bit);
  sig feea1000; 63 consts.
- Pins +10 (3343 -> 3353): 28313/328/329/392/393/456/457/552/553/28568.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- PARENT-035 (post-compat hwaccel) filed — no action until joint DONE.
- VERIFY-a55b78c band19 PASS seen, thanks. Q-39 (R27) still open.
- Frontier: P34 28569..28660 derived (Y0/Y1/YA16/YB10/YQ4x16,
  letter Y; YQ m-tab 6B b21,22,72-75 + q-tab 10B
  b10,11,17-20,68-71; plain lencode16), implementing next.
