# PARENT-009 grep blind spot fix (both sweeps + parent)

Parent wall-grep MISSED a libzbm dylib ref: `libzbm<newline>dylib`
(wrapped) + bare `ZBM_DYLIB` slip past `\.dylib`-only patterns.
Substance was compliant (survey-named, pinned, proto-only) but
the pattern gap is real. Fixes:

1. Sweep gate-tip OSS/CONTAM legs: add bare `dylib`, `_DYLIB`,
   `CDLL`, `dlopen`, `ctypes` patterns (keep known-good
   exclusions: system libc, own pattern lines).
2. One-line-per-dep rule: dependency paths/names in committed
   code must not wrap across lines (grep must see them).
3. Parent: same patterns from here on (this fire applied).
