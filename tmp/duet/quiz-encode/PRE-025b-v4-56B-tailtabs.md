# PRE-025b 56B tail tabs b52-55 + 4096 shift rule (w2 map)

## b53/54/55: strict 16-tabs from 3953, NO 4096 break (verified full span)
- b53: 85 ae 7f c2 ea bb ff 8a f8 a0 71 98 dd ae d6 7c.
- b54: c7 2f ff 77 df af 27 97 5f cf 9f 17 7f 4f b7 37.
- b55: 84 85 85 95 95 96 a6 a6 a7 b2 b3 b8 c3 c4 c4 d4 (ramp-ish).

## b52: 16-tab WITH 4096 break (only tail byte that reframes)
- pre (3953..4095): 8c 0c 0c 6c ec ec 4c ac cc 2c 2c 8c 0c 0c 8c cc.
- post (4096..): cd 8d 0d 0d 6d ed ed 4d ad cd 2d 2d 8d 0d 0d 8d.
- rule: post[i] = pre[i-1] lo-nibble +1 (all c -> all d; rotate-by-1).
