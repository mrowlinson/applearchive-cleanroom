# VERIFY-15ef0e5: PASS (3 cells + 9 pins, additive, honest)

- scope first-hand: tests +2/-2 (zeros loop gains 524289/600000/1000000 multi-frame-compressed),
  pins +9 rows. purely additive (loop-list + pin rows).
- code: same CELL() path (CT + ravframe + CLOSED/f2/sha). sizes cover 1M-zero 2-frame case
  (NOTE-w2s4-14: closes under existing walker, no model change). honest battery growth.
- wall: 0 hits under PARENT-009 patterns (dylib/_DYLIB/CDLL/dlopen/ctypes included). no FLAG.
