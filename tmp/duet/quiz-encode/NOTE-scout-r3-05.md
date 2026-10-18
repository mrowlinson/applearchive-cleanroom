# NOTE-scout-r3-05: W/R/T + YAA1 spelling verdicts (CLI vocabulary mapped)

## W/R/T: NOT in this build's CLI type vocabulary (either case)
- `-include-type`: per-char membership in {bcdfhlmps},
  case-insensitive (MH/fm/bcdfhlmps rc=0; any bad char kills:
  bcX/Xbc rc=1 `ERROR: invalid <types> specification`; empty
  spec rc=0 matching 0 entries).
- W/w/R/r/T/t (+Y/y/A/Z/1 controls) ALL rc=1. The wiki 11-type
  table does not match this binary's CLI. Stream-parse of
  foreign TYP W/R/T stays formally open (no sample bytes), but
  CLI-evidence says this build doesn't know them — container
  decode MUST still accept-or-reject deliberately at kickoff
  (foreign-bytes probe, decode coordination).

## YAA1: NOT an aa field key (format rule, not membership)
- `-include/−exclude-field` validates FORMAT ONLY: exactly 3
  alnum chars, case-insensitive, membership unchecked (QQQ rc=0,
  A1B rc=0, ZZZ rc=0; ZZ/ABCD/yaa1x rc=1 `ERROR: invalid
  <fields> specification`).
- YAA1 (4 chars) fails the format rule both cases, both verbs.
  Its 3-char form YAA is well-formed but emits 0 keys (QQQ
  control identical) — also not a real key. Whatever YAA1 names
  (codec-internal? AEA-side?) lives OUTSIDE aa's field
  vocabulary; container encode never emits it, decode never
  parses it as a field. Cross-lane note: if a lane sees YAA1
  bytes, source them there, not in aa fields.

## Solo scope closed
- Queue (3) solo-probeable half DONE; foreign-bytes
  parse-acceptance (W/R/T/m/h stream bytes) is kickoff work
  with decode-lane coordination, filed as such.
