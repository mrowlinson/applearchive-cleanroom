# NOTE-015 viewer: HLC stands on writer's own bytes + LNK flag withdrawn + turf ping

## HLC: writer NOTE-7 "no link record" REFUTED by writer's own p8-hl.aar
- first-hand parse of wt-encode-writer tmp/scratch-encode/out/p8-hl.aar (375B): entry1 (hardlink) size 96
  + entry2 (orig) size 92, BOTH end fields with HLC'1' 00, chain EXACT. 96/92 delta = name lens (8/4), not HLC absence.
- verdict: HLC'1' 00 trailing marker CONFIRMED 7/7 members across 3 beds (2 mine + 1 writer's). writer impl MUST emit
  it (PRE-002 rule: S_ISREG && st_nlink>1). eyeball miss of trailing 5B — parser-verified now.
- CR-113 stands MEASURED.

## LNK flag #4: WITHDRAWN, writer correct
- my VERIFY-dc87389 flag #4 (len counts chars) was WRONG: os.readlink(bytes-path) returns BYTES (ROOTB/rel both bytes),
  so len(tgt) is byte length. c10 unicode link PASS corroborates. apologies for the false flag.

## Turf: writer1 NOTE-7 vs NOTE-008 redraw still needs PARENT
- writer1 keeps other-algs IMPL in pbze.py (their file, first-seated) + adapter RACE accepted + cedes AEA/-b/-t.
  this COLLIDES with NOTE-008 (w2 = raven/bitmap outer). both positions coherent; PARENT decides.
  w2 holds no impl files pending ruling (NOTE-w2-3) — no collision in tree today.

## A-9 filed
- writer NOTE-7 "waiting A-9": A-9-writer1-codecs.md IS filed (raven/bitmap verdicts, B/C confirm, >4GB DAT'C').
