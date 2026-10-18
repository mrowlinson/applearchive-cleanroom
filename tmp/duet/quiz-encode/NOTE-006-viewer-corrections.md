# NOTE-006 viewer: CTM agree + store-rule CORRECT + outer-parse note (re NOTE-4/5)

## CTM: AGREE CTM=btime. my A-6 min() WITHDRAWN.
- root cause of my error: `touch -m -t 2021` RETRODATES btime on APFS (bedded: btime=mtime=1614852367).
  my "discriminating" bed had btime==mtime — undiscriminated. all beds now fit CTM=btime:
  fresh (CTM==btime, ns-exact), touch-past (btime follows), touch-future (CTM==btime=now).
- writer getattrlist crtime approach CORRECT. OPEN edge (no bed distinguishes): a file with mtime<btime
  with CTM read — unreachable via touch/utime if OS clamps btime; revisit only if such a bed appears.
- A-6 "CTM=min(btime,mtime)" struck; do not implement the min.

## Store rule: CORRECT writer NOTE-5 "comp<unc else raw". 15/16 rule STANDS.
- fresh re-verify (NEW random bytes): unc=850, aa comp=796 -> COMPRESS. floor(15*850/16)=796: 796<=796 edge-INCLUSIVE.
- prior bed same unc=850, comp 797 -> STORE. verdict flips on ONE comp byte at the predicted boundary.
- writer's rule mispredicts the stored case (797<850 yet stored). their sweep never landed comp in
  (15unc/16, unc) — that window is ~1/16th wide and only visible near codec-crossover sizes.
- rule (unchanged): per block, compress iff 16*comp <= 15*unc. writer impl MUST use this, not comp<unc.
- OSS-lzfse byte-exact finding (NOTE-5): trusted-from-writer (not re-run by viewer; lzfse path is writer turf).

## Outer parse: same bytes, two framings. NO conflict.
- writer NOTE-5 "28B first-block hdr + 16B chained next-headers" == my "12B prefix + uniform 16B/block chain"
  byte-for-byte (3-block 10MB: both sum 10000301 EXACT). either framing implements identically.
- prefer uniform chain (simpler): prefix(magic,u32 0,u32 BE blocksize) + repeat(u32 0,u32 BE unc,u32 0,u32 BE comp,comp bytes).
