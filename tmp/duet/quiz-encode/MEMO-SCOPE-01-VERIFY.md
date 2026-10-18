# MEMO-SCOPE-01-VERIFY (parent first-hand, 2026-10-18): CONFIRMED

Method: own oracle beds, zeros-N -> compression_tool -encode
-a lzraven, pay=raw[12:-4], sig=pay[0:4]. 17 probes, NVME
tmp/parent-scope. No memo files used as input (predictions
read AFTER probing for all but control).

- Control N=120093: raw100 sig 66501000 (matches A-361). PASS.
- Formula stride: P_start(P)=83553+(P-192)*348.
  P500 -> N=190737: raw104 sig a6020000 structured. PASS.
  P1000 -> N=364737: raw108 sig 1b8e1e00 structured. PASS.
- Phase evolution: N=250000 raw108; N=450000 raw112
  sig 9f849c01 structured. In-phase with memo schedule. PASS.
- P1458 start N=524121: raw112 sig 0fa8cf20. EXACT. PASS.
- N=524212: raw116 sig 19040000 structured. PASS.
- Top N=524287: raw116 sig 03400000. EXACT. PASS.
- Transition N=524288: raw116 sig 07800000 (old size,
  new sig). EXACT. PASS.
- N=524289 raw121 / N=524300 raw132, sig 07800000
  (+1/cell 121..132). EXACT. PASS.
- Beyond: N=600000 raw184, N=1000000 raw196, both sig
  07800000. EXACT vs memo table. PASS.
- R189: N=83297 + N=83552 raw100 sig de652003. EXACT. PASS.
- R189/P192 boundary: N=83553 sig 20030000 (P192 PB0),
  N=83554 sig 47a20700 (PB1). EXACT. PASS.

Verdict: scope CONFIRMED on all 17 probes, 9 byte-exact.
LAST P = P1458 (524121..524287). LAST R = R189
(83297..83552). TOP N = 524287. Uniform sig-07800000
regime beyond (no P/R structure to 1M probed).
Remaining: ~1279 P-tiers (P180..P1458) + 18 R-tiers
(R172..R189). Plan steps 5/6/8/9 STAND as written.
