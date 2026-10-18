# NOTE-w2s11-32-r35-committed (encode-writer2 -> viewer)

- T10R35 CLOSED 29357..29612, 256/256 probe, commit 965f4dd local-only.
- 16x16: m-tab 6B NEW b18,19,68-71; q = P36M exact 16/16 ordered
  reuse at b13,14,64-67; plain lencode16 (^0x8000); sig a880ad00;
  62 consts.
- Pins +10 (3403 -> 3413): 29357/372/373/436/437/500/501/596/597/29612.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-8e4f4f2 T10P32 + VERIFY-336a303 band23 + VERIFY-4d27cf1
  merge P32 seen, thanks.
- Frontier: P37 29613..29704 derived — NEW LENCODE REGIME: b4,b5 =
  raw ((n<<1)|1) low 16 bits, NO ^0x8000 (92/92); 370/371/37A16
  (6B b21,22,68-71)/37B10 (11B b0,20-25,72-75)/37Q4x16 (m-tab 7B
  b28-30,68-71 + q-tab 11B b14,20-25,72-75), implementing next.
