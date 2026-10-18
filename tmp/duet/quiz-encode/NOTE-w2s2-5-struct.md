# NOTE-w2s2-5 writer2: raven/bitmap framing walked + Q-14 filed

- frames (b10k, zeros-100k): raven 11 frames [216,96x9,64] magic
  2b00caec; bitmap 11 frames [234,110x9,90] magic ZBM. default block =
  single frame each. first frame = metadata+zeros; tail = short.
- INDEPENDENCE proven (patch bed): 100B random patch flips only its 2
  covering frames; other 9 byte-identical both codecs. no dict/state
  across outer blocks. impl consequence: blocks encodable isolated.
- trailer mapped (raven 7-pt size sweep): mid trailer constant
  (unc=10000, last=0x50); pre-tail midfield=tailunc+30 exact,
  lastbyte=tail-frame-len exact. asymmetry (mid last=nextlen-16 vs
  pre-tail last=nextlen) filed as Q-14 (mechanism gap, non-blocking).
- Q-13 (raven/bitmap iteration oracle) still open; Q-14 open. no A-13/
  A-14, no new PARENT, no DONE. claim HELD. next: bitmap trailer
  confirm (2 pts) + battery green-keeping.
