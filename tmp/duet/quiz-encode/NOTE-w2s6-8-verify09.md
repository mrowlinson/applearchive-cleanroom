# NOTE-w2s6-8 writer2: PRE-008/009 VERIFIED + bug owned + m11=T1-flag

## segbed7 bug OWNED (my bad, fixed in tool)
- 8-value loop used leaked `pos` (=127) not 96 — scanned tail holes,
  reported common-0. PRE-009's correction stands; tool fixed + noted.

## PRE-008/009 confirmed first-hand, to the bit
- N=129: common-10 EXACT {11,20,66,98,99,131,307,308,309,347}; uniques
  bit0-3->{3,4,5,6}, bit4-7->{50,51,52,53} (two nibbles) ✓.
- N=131: common-39 ✓ same value slots ✓. N=130: common-24 — viewer's
  PREDICTION confirmed exactly ✓. value slots stable all three ✓.
- rewrite MORPHS not just grows (129->130: 20->29 swap, 307-drop;
  130->131: 308/309-drop). spread = stable split-holes + morphing
  presence rewrite.

## m11 = T1-flag (band resolved, absolute)
- bit11 = 1 @N=128..255 (every 4th + T1-full const-1 earlier), 0 @N<=127
  and @N>=256 (every 4th to 316). edge EXACTLY at tier bounds.
- so m11 = pristine-T1-skeleton (T1 AND no early/late dev per A-27
  knobs). T2 bit11 is LIVE (in T2 VARY set) — markers are per-tier.
- T2-head decode (bits 4-7,11,12,15,19,23 vary) queued.

## Lane: 89c57df (rgram 34-pin) committed, all batteries GREEN, for gate.
