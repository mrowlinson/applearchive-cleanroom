# NOTE-scout-r4-03: foreign-bytes kickoff session plan (queue 1a)

## What is already closed (no re-probe)
- Oracle-decode (extract) over ALL 256 TYP values: census-closed
  by lane-committed DPROBE-04 (256/256 crafted flips): 248 =
  silent skip exit 0; 8 special classes (B/C device-no-DEV abort,
  D-on-file creates dir, F normal, H hardlink-by-path, L-no-LNK
  abort, P-with-DAT hang, S loud-skip exit 1). m(109)/W(87)/R(82)/
  T(84)/lowercase-h(104) sit in the 248 by elimination.
- CLI vocabulary (r3-04/05, oracle-side): -include-type membership
  = exactly {bcdfhlmps} case-insensitive (W/R/T rejected);
  -include/-exclude-field = exactly-3-alnum format-only (YAA1
  fails format; YAA well-formed but emits nothing). YAA1 lives at
  the stream-magic layer (legacy magic 59 41 41 31 per lane
  notes), NOT in aa fields — if seen, source it there.
- H uppercase (72): decode-closed (H+LNK hardlink-by-path,
  post-pass, reg-only rule). Encoder emits HLC groups, never H —
  no container-encode action.

## Residual matrix for the kickoff session (decode lane owns method)
- Cells: TYP {m, W, R, T, lowercase-h} + controls {F accept, Z
  known-skip} x verbs {list, verify} (+ extract re-confirm of the
  4 values only, 4 cells, to pin census-by-elimination to
  census-by-measurement).
- Total: 7x2 + 4 = 18 cells, all through decode lane's craft
  harness + battery cells (their method, their verdicts).
- Open question for decode lane: YAA1-magic stream acceptance —
  no local producer exists (r3-05); does oracle parse a YAA1-magic
  stream at all? If their recon already answers it, a pointer
  closes it with zero cells.

## Scout provides (oracle-side, already filed)
- r3-04 (m/YAF emit-negative + forced-field map), r3-05 (W/R/T +
  YAA1 spelling verdicts), r4-02 (libzbitmap wall brief).
- Probe-kit offer: unpatched oracle archives + patch offsets on
  request — decode lane decides whether to use them or their own
  craft path. No scout-crafted verdicts: crafted-input behavior is
  decode turf, and the census already covers the extract column.

## Close criteria
- Session closes queue-1a when: list/verify columns measured (or
  ruled out-of-scope) + 4-value extract re-confirm + YAA1-magic
  answer-or-pointer. Container-encode consequence either way: the
  emitted-TYP vocabulary is already pinned (D/F/L/P/S + HLC
  groups); foreign-TYP handling is a decode-side accept/skip rule.
