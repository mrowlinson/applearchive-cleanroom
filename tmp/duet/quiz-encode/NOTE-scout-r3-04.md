# NOTE-scout-r3-04: m/YAF hunt — emit-negative (parse-acceptance open)

## Verdict: no local path emits TYP m or YAF (joins h as emit-negative)
- `aa -h` discloses: m = "metadata entry (not a filesystem
  object)", yaf = "list of archive fields (metadata entry)".
- Probed, all rc=0, zero m/YAF: archive -include-field yaf (11
  entries, no YAF keys — YAF unforceable, CMP-class);
  -include-type m (0 entries — negative confirmed); convert;
  verb-manifest; archive-time -omanifest; cpio-convert; verify
  (clean rc=0 / dirty rc=1); check-and-fix (in-place, emits
  nothing); patch (shape unprobed, "patch failed" w/o inputs).
- Parse-acceptance of TYP m / YAF stays OPEN (needs foreign or
  hand-crafted bytes — same boat as W/R/T+YAA1, queue item 3).

## Bycatch (forced-field mapping, own bytes, macOS 27.0.1)
- -include-field FORCES: yec (int, nonempty-F-only; 82 @<=~7K,
  184 @64K, 1986 @900K — size-scaling count), duz (int disk
  usage: D=4096, F=size-rounded), cks (int, F-only, POSIX CRC
  per -h), sh1 (40-hex string). SILENT-accepted: btm (no backup
  time source), yaf (above), cmp (r2).
- check-and-fix puzzle (NOT scout turf, recorded): 11-common-OK
  verdict on a dir with corrupted+retouched text.txt, content
  NOT restored — fix scope unclear (attrs only?). Verify lane
  owns; container battery does not assert fix semantics.

## Leads filed, not chased
- AEA auth-data entries (-sign-pub-auth-key "auth data entry"):
  possible m/YAF habitat — AEA seat turf, zero scout reads.
- Hand-crafted m-bearing stream: needs decode-lane coordination
  at container kickoff (same session as W/R/T+YAA1 probes).
