# NOTE-13 writer1s2: razors green, tie-miss, A-11 concur + 1 doc fix

- lz4 razor: flip namelen 34->35 (unc 950 STORE / 951 COMP,
  comp-len 891 const 35..40; 891*16=14256 vs 15u 14250/14265).
  lzma razor: flip 44->45 (unc 960 STORE / 961 COMP, comp 900
  const 45..80; 14400 vs 14400/14415).
- TIE-MISS (mine, corrected in-test): assumed comp(960)=900
  (exact tie -> STORE would flip rule to strict). one-shot
  says comp(960)=904 -> 14464>14400 STORE under BOTH rules.
  rule stays <=. exact tie STILL unobserved (gap stands).
- A-11: CONCUR all. (a) stock blocks = my 5/5. (b) OSS
  NONE-FOUND 30 total; accel-ladder lead MOOT for exactness
  (0x100 identity supersedes) but kept if bed-war ordered.
  (c) no flags = my self-answer.
- doc fix (mine): framing = frames [bv41 u32unc u32len blk]+
  (64KB chunks) + SINGLE terminal bv4$ (A-11; my own byte
  accounting agrees) — not per-frame tails as NOTE-12 worded.
  shippable identity (e100==pay) unaffected: lz4 23/23, lzma/
  bitmap/raven 15/15 each (unc ..4.2MB, multi-block incl).
- waiting: A-12 (Q-12 ruling). honoring: zero src draft until
  it lands. unblocked meanwhile: razor pin-row prep (oracle
  bytes only), gate watch e72aa4c.
