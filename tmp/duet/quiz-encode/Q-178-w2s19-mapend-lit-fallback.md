# Q-178 (w2s19): map end @70328? literal fallback N>=70329

Own beds first-hand (NVME seat, compression_tool
-oracle bytes only):

1. boundary exact? 70328 = last 100B grammar cell
   (R151 off255, sig 783c0300, b4=0x71 b5=0x25);
   70329 = first 53B literal (sig 01500200).
   70329..70484 contiguous 156/156 literal, zero
   100B stragglers. confirm last-grammar=70328?
2. literal rule unbounded? 53B frame sig
   01500200, 37B pay == raw input bytes EXACT
   (162/162 incl sparse 71000 72000 80000
   100000 16777216 33554432; high input bytes
   tracked: pay[3]=0x01/0x02 at 16M/33M).
   varpos whole-regime = input support only.
   confirm pay==input, no exceptions anywhere?
3. scope: is the literal fallback IN the rgram
   map (staged T10LIT handler: n>=70329,
   paylen 37, sig check, echo check, GREEN
   162/162 on scratch) or is the map COMPLETE
   at 70328 with literal out-of-scope? need
   ruling before WT commit.
