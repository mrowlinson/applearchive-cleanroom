# NOTE-viewer2-HANDOFF-r13 (4-cap reached, EXIT per PARENT-074)

## Filed (all PASS, full first-hand r13 batteries, seat-private WS)
- VERIFY-02c66ac (b203 T10R141): build 0w 2015048B;
  PYID 4286/4286; CBAT/PYBAT 8572/0; set-eq 8572;
  own 66593..66848 256/0 p24; tables 3/3 (M/Q 16,
  C 68); wall 0. Concurs GATE (sweep-r16d).
  Claim consumed. Unblocked b203 merge.
- REAUDIT-94a0e0b (b191 T10R135, independent 2nd
  coverage): build 0w 1946744B (== VERIFY build);
  PYID 4127/4127; CBAT/PYBAT 8254/0; set-eq 8254;
  own 64505..64760 256/0 p24; tables 3/3 (C _N 67);
  wall 0. Concurs GATE+VERIFY. Claim consumed.
- VERIFY-8b26a1f (b205 T10R142): build 0w 2031896B;
  PYID 4314/4314; CBAT/PYBAT 8628/0; set-eq 8628;
  own 66941..67196 256/0 p24; tables 3/3 (C _N 67);
  wall 0. Concurs GATE (sweep-r16e). Claim consumed.
  Unblocked b205 merge.
- VERIFY-d01a797 (b207 T10R143): build 0w 2048792B;
  PYID 4342/4342; CBAT/PYBAT 8684/0; set-eq 8684;
  own 67289..67544 256/0 p24; tables 3/3 (C _N 69);
  wall 0. Concurs GATE (sweep-r16e). Claim consumed.
  Unblocked b207 merge.

## Method notes (r14 reuse)
- Corpus chaining own-seat works: b205 seeded 4352
  ex own b203 r13, b207 seeded 4408 ex own b205 r13
  (cp -al, missing-only fresh-oracle regen, fresh
  py+C exec per pin). Tables scripts sed-cloned per
  band (fix _N assert + chain comment each time).
- Predecessor r12 lesson honored: never file on
  staged numbers — every leg re-ran first-hand r13.

## R14 NEXT (Step-1 re-scan first)
- At exit: b203-b208 + b210 all GATE+VERIFY; b209
  f8e426b gating (sweep-r16f claim, no GATE yet);
  b211/b212 gating (sweep2-r26 on b212 a50a414);
  lane tip b221. Q max 361, qmiss=0, diff 0.
- Likely: b209 VERIFY when GATE lands, else
  oldest-gated-first per 068/069/070 + claim-check 071.

## Seat state
- WS tmp/encode-viewer2/{02c66ac,94a0e0b,8b26a1f,
  d01a797}/ retained (trees + builds + corpora + logs
  + scripts) + r13/ TMPDIR. No commits, no push.
  Heartbeats hb-r13-01..26 on file.
- EXIT per PARENT-074 (cap+handoff, no hold-polling).
  Seat HELD, no joint DONE. Refill as r14 same lane/tree.
