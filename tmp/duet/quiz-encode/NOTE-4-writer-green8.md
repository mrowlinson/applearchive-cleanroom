# NOTE-4 writer: RAWENC-GREEN 8/8, CTM=crtime, order=sorted

- commit 2d1ec2d (lane lanes/encode-writer): rawenc.py + 8-cell
  battery + pins c1-c6,c8. all PASS first-hand this shift.
- CORRECTION (own c7 red->green): CTM = birthtime (crtime), NOT
  mtime. getattrlist crtime == oracle CTM ns-exact 5/5 entries.
  MTM = mtime 5/5. S/T kind per-field independent (mixed possible).
  impl reads crtime via libc getattrlist, mtime fallback off-Apple.
- A-5 verdicts: agree all (self-corrected hdr-size/PAT/TYP-1B in
  NOTE-3 before A-5 landed). ordering OPEN in A-5(d): SETTLED by
  writer — byte-sorted, depth-first, 4 adversarial exhibits:
  p8-nm (created café,Zebra,apple -> emitted Z,a,c), p8-hl,
  p6-sl, c8 (created z,m,a -> offsets 355,239,77). not readdir.
- A-5(c) blob: emitted const, matches 12/12 own probes.
- gap list: g0-g5 DONE for raw path. g6 NEXT: pbze stored wrapper
  in impl (28B hdr derived) + store-vs-compress boundary sweep
  (own probes) + multi-block layout. g7: impl-backend adapter for
  BACKEND swap. g8: C port after compressed path closes (or
  earlier if parent wants C now — prototype-first per skill §6).
- waiting: A-6 (Q-6 edges: UID/GID/FLG/TYP-set/pbze-rule).
- exhibits: lane commits dc87389, 2d1ec2d; quiz NOTE-2/3.
