# NOTE-w2s5-6 writer2: LENGTH CODE closed (byte4 exact) + tail-echo puzzle

- R1 TIERS (zeros-N, exact): N<=63 STORED-verbatim (paylen=N, F3=(N<<12)|1);
  N>=64 COMPRESSED flat-44B to N=513+. tierbounds 63/64, 127/128, 255/256
  (+512 shape-change noted, open). tier[k] base 2^(k+6), width doubling.
- R2 BYTE4 = (offset<<1)|1 EXACT (128/128 tier1 sweep, bits 33-39 = O0-O6
  linear, bit32 const-1; only head bits varying with N).
- R3 TAIL ECHO (lossy, deterministic): bits 307-310 = (off+3)&15 (16/16
  incl wrap 63->15/64->0); bits 272-273 = (off+3)>>6 (transitions exact
  @off+3=64,128). MIDDLE bits 4-5 NOWHERE in 352-bit scan — tail has 48
  states for 128 offsets (byte4 carries full length; echo purpose open —
  2nd-run token? checksum?).
- grammar so far for A-23 ask: tiers + byte4 + split-nibble value fields
  (NOTE-5) + lossy tail echo. next: tier2/3 sweep (does byte4 rule hold?
  b8 tier-code map) + TAG-width ID at nibbles. claim HELD.
