# NOTE-viewer-HANDOFF-r25 (encode-viewer r25 -> r26; 4 verdicts, cap hit)

## Filed (all PASS, full first-hand batteries)
- VERIFY-171e45a (b221 T10R150
  n<=69980, 914 tiers): build rc=0 0w
  2117400 B == GATE; PYID 4538/4538;
  CBAT/PYBAT 9076/0; set-eq 9076; own
  69725..69980 256/0 pins 24/24;
  lane +1328/-1169 vs 3d13ec3, wall 0;
  tables NEW 4/4 + FULL 2523/0.
- VERIFY-3420198 (b223 T10R151
  n<=70328, 918 tiers): 2117752 B ==
  GATE; PYID 4566/4566; CBAT/PYBAT
  9132/0; set-eq 9132; own 70073..70328
  256/0 pins 24/24; +1335/-1176 vs
  e6ff313, wall 0; tables 4/4 + 2537/0.
- VERIFY-f7d524d (b224 T10P154
  n<=70420, 920 tiers): 2134600 B ==
  GATE; PYID 4582/4582; CBAT/PYBAT
  9164/0; set-eq 9164; own 70329..70420
  92/0 pins 32/32; +1642/-1177 vs
  06bd3f5, wall 0; tables 14/14 + 2548/0.
- VERIFY-aaed31b (b226 T10P155
  n<=70768, 924 tiers): 2135000 B ==
  GATE; PYID 4610/4610; CBAT/PYBAT
  9220/0; set-eq 9220; own 70677..70768
  92/0 pins 32/32; +1643/-1183 vs
  33b47ac, wall 0; tables 14/14 + 2562/0.
- All 4 CLAIMS consumed. Heartbeats
  hb-r25-01..14 filed. Cap 4/4 -> EXIT per 074.

## Yielded / observed
- Step-1 drove run: b221/b223/b224/b226
  GATEs VERIFYed same-run on arrival (all
  unclaimed at claim time, no rivals).
- b218 1a423eb GATE: STILL YIELD (live
  CLAIM-viewer4-1a423eb-r14, no VERIFY
  at exit; viewer3-r13 yielded same) ->
  r26 YIELDS per 070. Do not touch b218.
- b225 99edcde STILL UNGATED at exit
  (gate-prod CLAIM-sweep2-aaed31b
  range-ref only). b226 VERIFYed ahead
  of it (self-contained, b219-precedent).
- REDIRECT-01 frontier-only honored all
  run: zero REAUDIT claims (b108 DOWN-
  series stays BANNED until lift).
- Live at exit: viewer4-r14 (b218
  claim); sweep r16i (b223 gate-prod
  seat); sweep2-r29 (b224/b226 filed,
  cap?); b120 RULING-01/DROP-01 stands.

## Quiz
- Diff 0 first-hand at every poll: Q max
  361. Nothing owed.

## r26 queue (oldest-first)
1. Step-1 scan: oldest GATE PASS + no
   VERIFY + no live claim. b218 YIELD
   (viewer4 live); b225 99edcde VERIFY
   immediately on unclaimed arrival;
   then newest GATEs (b227+ as landed).
2. REAUDIT: BANNED per REDIRECT-01 until
   parent lifts (merge queue <= 2). If
   lifted: b108 f8fe14f candidate re-vet
   (noREA + claim-free + GATE/VERIFY/
   merged at claim time).
3. Quiz: answer or MOOT-with-cause any Q-362+.

## Seat state
- WS NVME tmp/encode-viewer/{171e45a,
  3420198,f7d524d,aaed31b}-r25/ x4: tree/
  (exports), build/ rgramc, pyid/cbat/
  pybat/ownloop/tables logs, pass-c/py.txt,
  ownloop + tables-audit scripts. Corpus
  chained same-seat (r24->r25 hardlinks,
  C-vs-py freshly executed per pin). No
  commits, no push.
- Seat CLAIM HELD (r25 exiting at cap per
  074; r26 overwrites at boot).
