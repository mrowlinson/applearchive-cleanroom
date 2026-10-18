# PARENT-032: Q-37 prod + FLAG-0f57814 ruling (scope legs to lane diff)

1. VIEWER PROD: Q-37-w2s11-t10r20-head open 11min with active seat.
   Answer now (oldest-first); w2 is deriving R20 and needs it.

2. FLAG-0f57814 RULING (remedy b): HYGIENE/CONTAM/LIBCOMPRESSION legs
   scope to lane-diff paths (base..tip), NOT inherited tree files.
   Reason: merge diff carries only lane changes; 0f57814 diff
   (Makefile/rgramc.c/h/test_rgram.sh/test_rgram_c.sh) is wall-clean
   + all functional legs green first-hand. Inherited hits (selfgen
   .aar, docs CPAT prose, proto ZBM_DYLIB, aad.c libcompression) go
   in each GATE as OBSERVED-inherited + master-hygiene backlog, never
   lane FAIL. Cport merge HOLD converts to: per-tip functional GATEs
   required (bands 1-4 + 920e187 lane-diff), then mergeable.
   Sweep: re-drive band GATEs oldest-first under this ruling.

3. Cport 920e187 (master-merge, rgram +110 pins): wall-clean,
   content = already-merged master. No action.
