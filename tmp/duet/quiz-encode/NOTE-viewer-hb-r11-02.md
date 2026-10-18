# NOTE-viewer-hb-r11-02 (first-hand legs)

- Build r11 seat-private: cc -O2 -Wall
  -Wextra -std=c11 rc=0 0 warnings
  1895688B (= r10 byte-size).
- Wall-grep PARENT-032 scope first-hand:
  4f8b304..d1a3c2d (rgramc.c only
  +1484/-1034, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
- Tables-EQ re-run first-hand: NEW 8/8
  (_N 75/71/62) + audit 1238/0.
  Matches r10 on-disk.
- PYID running (corpus cached, silent
  when green). Waiting; CBAT/PYBAT/
  PINS/own-loop-re-run after.
- No commits, no push.
