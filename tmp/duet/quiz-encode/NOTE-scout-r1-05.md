# NOTE-scout-r1-05: harness skeleton landed (b53969c) + `aa -h` findings

## A. Commit (LOCAL ONLY, lanes/encode-container@b53969c, worktree clean)
- harness/container-adapter.sh (probe + frame-list/-xmanifest/-append/
  -convert, oracle-backed) + tests/container/{README.md,t0-smoke.sh}
  + tests/test_container.sh. T0-CONTAINER GREEN 5/5 first-hand vs
  oracle (macOS 27.0, -t 1, NVME workdir). No map-lane reads; nothing
  pushed; master untouched.

## B. `aa -h` full-read findings (binary-truth, wall-clean black-box)
- -a list CONFIRMS lzbitmap (man page stale — man-vs-binary drift
  filed NOTE-02 stands; trust binary).
- Field vocabulary (lowercase CLI names): typ pat lnk dev uid gid mod
  flg mtm btm ctm dat siz cks sh1 sh2 sh3 sh5 xat acl duz idx idz yec
  yaf + attr/ALL aliases. vs theapplewiki uppercase keys (TYP/PAT/..):
  case differs (CLI alias vs wire key — probe decides mapping).
- TYP DISCREPANCY (new, container-lane probe owns): `aa -h` types =
  9 lowercase (b c d f h l m p s); theapplewiki table = 11 uppercase
  (F D L P C B S W R T M). Delta: wiki has whiteout/door/port, lacks
  hardlink; binary vice versa. Oracle header bytes decide; NEITHER
  adopted until probed.
- SLC: man EXAMPLE uses -include-field SLC but -h field list OMITS
  it — acceptance probe open (round 8). HLC named only in
  -ignore-cpio-hlc help (cpio hardlink-cluster synthesis).
- -manifest alias confirmed (= exclude dat + include sh2,siz,idx,idz
  + lzfse/1m); -omanifest = convert-time manifest (later verb);
  manifest is a real VERB (frame-xmanifest maps it 1:1).
- Adjacent surface noted (not stubbed): -afsc fst-compression,
  aa-native encryption flags (profile auto-select; full range = pipe
  to aea), entry-selection (-include-path/-rename/...), cpio parsing.

## C. Rounds 6-10 plan (stay-alive)
- Black-box framing probes on selfgen bytes (own oracle outputs):
  header-chain walk (magic/size stepping), pbz* magic census, slc
  acceptance, list-json field census. Findings -> NOTE-06..08.
- Then sleep-60/poll loop; never exit pre-DONE.
