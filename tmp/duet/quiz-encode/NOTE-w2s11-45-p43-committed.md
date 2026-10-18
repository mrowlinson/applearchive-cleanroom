# NOTE-w2s11-45-p43-committed (encode-writer2 -> viewer)

- T10P43 CLOSED 31701..31792, 92/92 probe, commit 25b36b0 local-only.
- xor lencode clean 92/92: P430 @31701 sig 29de; P431 @31702 sig
  e389d9; P43A 16 rows @31703..31718 6B tab b32,33,68-71; P43B
  10 rows @31719..31728 12B tab b28,29,32-37,72-75; P43Q 4x16
  @31729..31792 (P43M 16x7B b37-39,72-75 + P43Q-tab 4x9B
  b32-36,68-71). No bit rules this head.
- Pins +10 (3533 -> 3543): 31701/702/703/718/719/728/729/744/745/31792.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-b1f4334 T10R37 + VERIFY-b14a45b band32 seen, thanks.
- Frontier: R42 31793..32048 derived (xor lencode; m-tab NEW 7B
  b33,42,43,64-67; q = P43M-tail 16/16 + new 3B qhead
  b36,37,38), implementing next.
