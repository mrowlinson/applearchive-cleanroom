# NOTE-scout-r2-08: omanifest + IDX/IDZ + CMP closers

## -omanifest: ARCHIVE-time verb (convert-time stays silent)
- `aa archive -a lzfse -omanifest PATH ...` rc=0 and WRITES (1215B,
  raw AA01 even though main output is pbze). Convert-time -omanifest
  (NOTE-r2-04) writes nothing on raw OR lzfse output — trigger
  split: archive YES, convert NO (this build).
- Omanifest content (nested, 8 entries D4/F4): manifest alias shape
  (DAT absent, SH2+SIZ on files) PLUS IDX+IDZ on ALL 8. No M/YAF.

## IDX/IDZ DERIVED: (offset, length) into the uncompressed stream
- Values chain exactly: IDX = 0/114/230/348/468/612/753/891, IDZ =
  114/116/118/120/144/141/138/134; IDX[n+1]-IDX[n] == IDZ[n]
  throughout and 891+134 = 1025 = t1-nested-raw.aar size. Purpose
  fits `-imanifest` ("accelerate processing when only a subset of
  entries are selected"): random-access index into the AA01 stream.
- Cpio-convert IDX/IDZ (NOTE-r2-04: 250/599, IDZ 99) are the same
  fields on that path (offsets into the cpio-derived stream).

## CMP upgraded: binary-ACCEPTED, emission unknown
- `-include-field CMP` and `-exclude-field CMP` both rc=0, but 0
  CMP keys emitted on twins-raw. CMP graduates from "single-sourced
  name" to "binary-accepted field with unknown emission trigger"
  (same class SLC was in before its trigger was found). Emission
  hunt stays open for container lane (try compressed -a + flag).

## Still open (container lane)
- m/YAF source (no M in verb-manifests, convert pairs, omanifests,
  or cpio converts — every local manifest-family output checked);
  W/R/T parse-only acceptance; YAA1 (no local producer); v1/v2
  selector trivia; omanifest+convert trigger (if any).
