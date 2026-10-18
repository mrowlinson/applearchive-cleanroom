# NOTE-sweep-220 — GATE-eeb1ee5 band110 PASS-functional + seat end

- band110 eeb1ee5: py 6210/0, pins 6210/6210, C 6210/0,
  parity 3105/3105, own-loop 348/0 + pins 52/52, tables
  4/4 EQ, wall 0. Inherit legs OBSERVED (PARENT-032).
- 9/22 gated (b102-b110 all PASS-functional). 90min budget
  reached; seat stopping. b111-b115 batteries were in-flight
  at stop (seat-private NVME dirs; rerun if partial):
  b111 5dca1be, b112 917fac8, b113 93555bb, b114 c343ea0,
  b115 99355a0. Fast legs pre-done for b111-b123 (diff/
  wall/tables all clean, see NOTE-210).
- Next seat: verify/reap b111-b115 logs, then launch
  b116 6606cc1 (51281..51628), b117 e05869a (51629..51884),
  b118 31e41ed (51885..51976), b119 0aea685 (51977..52232),
  b120 779427a (52233..52324), b121 f7cf078 (52325..52580),
  b122 12b8957 (52581..52672), b123 9e30e0b (52673..52928)
  via sweep-band.sh <sha> <lo> <hi>.
