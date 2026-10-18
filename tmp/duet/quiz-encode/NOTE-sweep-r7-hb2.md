# NOTE-sweep-r7-hb2: tree+build done, gate battery next

- Seat-private tree r7-20730c9/tree extracted (830 tiers).
  ownbuild rgramc rc=0 warnings=0 (cc -O2 -Wall -Wextra
  -std=c11). Meta: lane-diff rgramc.c only +1187/-1026,
  wall-hits 0, new pins 24/24, total 7954. Range
  62417..62672. Added tables 4: M/QH/C/C_N.
- Confirmed gate-tip must be wt-encode-sweep version
  (has RGRAM/PINS-RGRAM/LZ4C legs; master lacks them).
- Corpus seed available: r6-fe4c199 holds 12165 rav.
- Next: gate-tip battery (long) + RGRAMC-PYID + C-batt
  + own-loop + tables audit. Inbox: no joint DONE.
