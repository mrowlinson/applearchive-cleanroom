# NOTE-scout-r2-02: T1 fixture set LANDED (75726e7)

## Pins (lanes/encode-container@75726e7, LOCAL ONLY, 83 paths)
- Inputs: input/t1-{nested,flat50,symlinks,xattr,edges,twins}/ (content
  rows in SHA256SUMS). Archives: 6 -a raw + t1-twins-slc +
  twins-lzfse + twins-lzfse-convraw + t1-nested-APPEND-edges (11 .aar,
  all <8KB) + manifest/t1-nested.manifest + golden list-json.
  `shasum -c` ALL-ROWS-OK (L5 + T1). FIXTURES.md §8 documents all.

## Reproducibility law (NEW, measured — battery design hinges on it)
- CTM and MTM BOTH derive from file mtime: `touch -t 202001010000`
  moves both to 1577836800.0 (TZ=UTC). CTM is NOT btime here.
- Recipe `touch -h -t 202001010000` + documented xattr re-apply +
  empty-dir mkdirs => regen from a simulated git checkout (xattrs
  stripped, empty dirs deleted) is BYTE-IDENTICAL to pins, 6/6.
  (xattr -c cannot even remove com.apple.provenance — kernel ambient,
  identical everywhere — which strengthens the result.)
- Consequence: T1 regen legs CAN cmp bytes (unlike L5 hello, whose
  inputs carry un-normalized mtimes — L5 turf, untouched).

## Oracle behaviors pinned along the way
- SLC: archive-time `-include-field SLC` + identical content -> SLC=0
  on twins only (+10B); default archive never emits (any -a/size,
  incl APFS clones); convert preserves, never adds. (Also caught +
  fixed my own falsy-value census bug: test key presence, not value.)
- Convert lzfse->raw round-trips clean but DIFFERS from direct raw:
  battery compares census + extract, never cross-path bytes.
- Append without -subdir merges at root with EMPTY-PAT '' entry.
- Manifest = pbze archive, DAT absent, SH2+SIZ on files, no IDX/IDZ.
- Symlink farm incl dangling + dir-link round-trips via readlink
  comparison (diff -r unusable: dangling + loop warnings); battery
  ships a tree-compare helper, not diff -r, for that cell.
- xattr user.scout-tag value preserved through round-trip.

## Next
- T1 battery runner (t1-pinned.sh: shasum + regen-cmp + census +
  golden + round-trip + dedup legs) wired into test_container.sh.
- Then survey threads: TYP h-trigger hunt, Apple-404 re-verify,
  compression_tool framing probes.
