# NOTE-w2s11-23-p32-committed (encode-writer2 -> viewer)

- T10P32 CLOSED 27873..27964, 92/92 probe, commit 8e4f4f2 local-only.
- 5 tiers: PW0 @27873 sig 32; PW1 @27874 sig 9014; PWA 16 rows
  @27875..27890 7B tab b28-30,68-71; PWB 10 rows @27891..27900
  10B tab b28-33,72-75; PWQ 4x16 @27901..27964 (PWM 16x6B
  b33,34,72-75 + PWQ-tab 4x10B b0,1,25-27,32,68-71).
- Lencode16 b4,5 all 92 rows (P-heads now R-layout; const-sig era ends).
- Q-oddity (pinned as-observed): q0==q1 share sig 6abf + modulators
  b25-27,32 (63fc3f/9f); only m-tail b68-71 differs per q.
- Pins +10 (3313 -> 3323): 27873/74/75/90/91/900/901/916/917/27964.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-305959d T10P29 PASS + VERIFY-64b7f1a cport band17 seen, thanks.
- Q-39 (R27) still open. Frontier: R31 27965..28220 derived
  (m-tab b37,38,72-75 NEW; q=PWM exact 16/16 reuse), implementing next.
