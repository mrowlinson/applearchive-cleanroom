# PRE-002 hardlink + DAT-C beds (no Q yet; writer1 impl will need both)

## Hardlinks: trailing HLC'1' 00 per member, content DUPLICATED (no dedup)
- bed: 2-link pair (same inode 93769988) + 3-link triple + solo control.
- every nlink>1 REGULAR file ends fields with `48 4C 43 31 00` (HLC'1' 00), AFTER XAT. value constant 00 (not index/count). 5/5 members.
- solo file: NO HLC. dirs: NO HLC despite nlink>=2 (root + sub beds) — files-only rule: HLC iff S_ISREG && st_nlink>1.
- each member carries FULL DAT payload (18B x2, 6B x3) — encode does NOT dedup; link restoration is decode-side.
- writer rule: emit HLC'1' 00 as last field when st_nlink>1 on regular files.

## DAT'C': u64le length for >=4GB payloads (minimal-width A/B/C)
- bed: 4.5GB sparse file -> DAT kind 'C' + u64le 0x120000000 = 4831838208 EXACT. total 4831838451.
- widths: A(u16, n<=65535) -> B(u32) -> C(u64), minimal fit. same rule as int fields.
- pbze same input: 1153 blocks (1152x4MB + tail) chain EXACT; unc/comp u32 never stressed.
- XAT widening past 'A' (giant xattrs): still OPEN micro (likely moot, xattr caps).
