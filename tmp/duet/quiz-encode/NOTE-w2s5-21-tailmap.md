# NOTE-w2s5-21 writer2: TAIL-FIELD MAP all 32 pos (18 contiguous + 14 split)

- contiguous-8 value (V0-V7 span 7, LSB-first): 96[334-341] 97[342-349]
  99[248-255] 100[40-47] 101[48-55] 102[56-63] 103[69-76] 104[104-111]
  105[112-119] 106[120-127] 107[133-140] 108[141-148] 112[166-173]
  113[180-187] 116[203-210] 120[260-267] 122[280-287] 124[297-304]
  (19 contiguous; RAW8 full-byte subset: 99/100/101/102/104/105/106/122).
- SPLIT value (V0/V7 far apart): 98[247,350] 109[149,157] 110[82,158]
  111[83,165] 114[93,188] 115[94,202] 117[211,222] 118[6,223] 119[7,259]
  121[268,279] 123[229,296] 125[305,316] 126[237,317] 127[238,328]
  (14 split; exact per-bit slots need 8-value scans — queued).
- tag bytes (base, pre-existing): 0x10@96, 0x08@103/107, 0x01@112,
  0x0F@113 (!), 0x00 many, 0xC0@116hi... one-hot hypothesis DEAD (0x0F).
  tag nibble = field-type/len-code? (0x0/0x1/0x8/0xF seen) — open.
- confirms PRE-006 linearity independently (all value-EXACT, tags static).
  paylen const 352 (late-tier free) all 32. claim HELD.
