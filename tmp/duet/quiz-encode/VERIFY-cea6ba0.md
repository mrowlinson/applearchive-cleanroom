# VERIFY cea6ba0 (encode-writer): PASS, pristine-archive batteries green

- method: git-archive @cea6ba0 to WS (pristine; live worktree dirty with WIP), pycache stripped, both batteries run first-hand.
- PBZE-GREEN 4/4 (z1 332B, r1 3245B, mb 3958B, mix 1049382B). RAWENC-GREEN 8/8 (c1-c8). CONFIRMED.
- code read (pbze.py 60 lines + rawenc.py refactor): 15/16 rule correct in code; framing byte-identical to uniform chain;
  build_inner refactor clean; OSS dylib ctypes path venue-pinned (prototype-OK).
- FLAGS (minor, non-blocking):
  1. pbze.py docstring says "comp<unc else raw" but code does 15/16 — doc/code mismatch, fix doc.
  2. src/__pycache__/*.pyc COMMITTED (2 files) — binaries in repo; remove + gitignore. (transient RED seen mid-run
     was live-WIP edit collision, not a code fault; pristine run green.)
  3. c7 cell sha varies run-to-run (live times, unpinned) — pin it or fix mtimes; pins file still lacks c7.
- carried gaps: UID/GID trunc, FLG=0, LNK bytes, xattr order, B/C/S (unchanged from VERIFY-2d1ec2d).
- verdict: PASS. no merge-blocking FLAG.
