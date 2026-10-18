# NOTE-memo-hb-r1-01 (heartbeat)

- Seat memo-r1 booted: scratch /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-memo/r1, TMPDIR there.
- Oracle repro first-hand: zeros-N -> compression_tool -encode -a lzraven -i IN -o OUT, pay=raw[12:-4], sig=pay[0:4]. P297 edge EXACT (n120093 66501000 ... n120443 03000000, 10/10 vs A-361 window).
- TASK1 scoping: 348-stride P_start(P)=83553+(P-192)*348 holds P298..P398 (PB0 raw100 verified); BREAKS at P399 @155589 (raw104, all-88B phase). Zero raw100 in 155589..157000. No raw100 157k..215k (step-1000 sweep, all raw104; 216000 raw108).
- P399 head 155589..: 1+1+6+10+10+64+... (P-head-like, all-88B). 348-stride likely continues with evolved sizes. Next: sparse tier-start sweep to bound P-tier end + R189 boundary verify.
- Quiz poll: Qmax 361, all Q-28..Q-361 A-mapped (diff 0). Nothing owed. Q-362+ watch on.
