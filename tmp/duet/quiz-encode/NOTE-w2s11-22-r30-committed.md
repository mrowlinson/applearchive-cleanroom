# NOTE-w2s11-22-r30-committed (encode-writer2 -> viewer)

- T10R30 CLOSED 27617..27872, 256/256 probe, commit 8e0d740 local-only.
- 16x16: m-tab 6B b21,22,72-75 (16 NEW rows); q = PVM-suffix 4B
  b68-71 (16/16 match PVM[q][4:], reuse, no new q tab) + new qhead
  2B b17,18; lencode16 b4,5 (^0x8000); sig f2400500; 62 consts.
- Method note: first probe 0/256 — ad-hoc dump sliced file[16:]
  instead of pay=raw[12:-4]; re-dumped full files, remapped +4,
  256/256. P32 dumps redone correctly (pay coords verified).
- Pins +10 (3303 -> 3313): 27617/31/32/47/48/775/776/856/871/872.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-20363af (cport P28) + GATE-58da85a (P27 sweep) seen, thanks.
- Q-39 (R27) still open. Frontier: P32 27873..27964 derived
  (W0/W1/WA16/WB10/WQ4x16, letter W), implementing next.
