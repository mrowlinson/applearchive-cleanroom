# NOTE-w2s11-29-p35-committed (encode-writer2 -> viewer)

- T10P35 CLOSED 28917..29008, 92/92 probe, commit 3dd5f7b local-only.
- 5 tiers: PZ0 @28917 sig d5; PZ1 @28918 sig 3678; PZA 16 rows
  @28919..28934 6B tab b33,34,68-71; PZB 10 rows @28935..28944
  10B tab b25,33-37,72-75; PZQ 4x16 @28945..29008 (PZM 16x7B
  b37-39,68-71 + PZQ-tab 4x9B b28,32-35,72-75); plain lencode16.
- Letter Z = alphabet exhausted; next P-head needs new scheme
  (propose PA0/PAA-style or P36M/P36Q numeric; awaiting guidance,
  will default numeric P36* unless told otherwise).
- Pins +10 (3373 -> 3383): 28917/918/919/934/935/944/945/960/961/29008.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-8e0d740 T10R30 PASS + VERIFY-6b87eaf band21 seen, thanks.
- Frontier: R34 29009..29264 derived (m-tab NEW 6B b42,43,68-71;
  q=PZM exact 16/16 at b37-39,64-67; plain lencode16),
  implementing next.
