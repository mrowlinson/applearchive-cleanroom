# GATE-94c8d61 sweep: PASS (test-only tip; C-parity 5/5 first-hand)

- tip: lanes/encode-writer @94c8d61 (parent 34df169 gated PASS). +25/-0:
  tests/test_lz4_c.sh ONLY. src identical to 34df169.
- code read (ALL 25 lines): bed-loop py(lz4enc.py direct) vs C(AAE_C, WS
  default + env override) with honest cmp + exit codes + LZ4C-GREEN/RED.
  TMPD=${TMPDIR:-/tmp}: /tmp-default noted, precedent-consistent with
  test_lz4.sh (same pattern, gated PASS before); sweep ran TMPDIR=NVME.
  no FAIL (runtime temp, rm -rf cleaned, nothing committed).
- battery: GATE-PASS (outdir gate-w1-94c8d61-s4). all legs same-green as
  34df169 (C-BUILD w=0, RAWENC/PBZE/LZMA/SMOKE/UNITS py+C, pins 11/11+10/10
  both backends, HYGIENE/CONTAM/OSS-nominated/LIBCOMP/ADOPT).
- C-parity manual (NEW test, first-hand): 5/5 py==C (empty1/r1/rzc/rzs/z1),
  LZ4C-GREEN, AAE_C=gate-build aae, bed=prior lz4 inputs incl parked-rzc
  input dir. writer's 6/6 (mb/mix bed) not re-runnable (own bed); 5/5 on
  committed-shape inputs decisive for parity claim.
- test_lz4.sh NOT re-run: script+src+oracle identical to 34df169 legs
  (4/4 both backends); re-run adds zero signal. stated, not skipped-blind.
- coverage: 85/86 with 7e25544 (this file 85th; ZERO holds).
- viewer: VERIFY-94c8d61 PASS concur (LZ4C-GREEN 6/6 own bed, no regress).
