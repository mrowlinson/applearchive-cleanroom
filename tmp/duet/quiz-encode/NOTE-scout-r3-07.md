# NOTE-scout-r3-07: CMP emission — all-codec negative, AFSC lead parked

## -include-field CMP emits nothing on any codec (measured)
- basic dir (11 entries) x all 7 -a + -include-field CMP: rc=0
  every time, CMP-keys=0 every time. Extends r2-08 (raw twins)
  to the full codec matrix. CMP stays "binary-accepted, unknown
  trigger" (same class YAF was in before its verdict — but CMP
  IS well-formed 3-alnum, unlike YAA1).

## AFSC hypothesis: UNTESTABLE here, parked (not refuted)
- Idea: CMP rides on files carrying the APFS compression flag
  (`aa -h` documents -afsc for "files archived with the
  compression flag set").
- ditto --hfsCompression creates NO decmpfs xattr on this OS
  (NVME + internal both: output = plain copy, same du, only
  com.apple.provenance). System-file scan (ls/aa/man/plist/
  dylib): zero decmpfs sightings. No way to mint a
  compression-flagged file with available tools -> hypothesis
  parked for kickoff (needs an OS that still mints decmpfs, or
  a donor file from one). If CMP ever emits, re-test there.
