# PRE-092b 68: singleton dip @13257 + cluster + body (frontier stage)

## census (v5bk first-hand, 255 rows 68B + 1-row 64B dip)
- 13087..13256: bands (b0 16/b1 03; 10 edges step-16 13097..
  13241; b5 66->67 @13184).
- 13257: SINGLETON 64B dip (4th: 9081/9429/12909/13257).
- 13258/13259: transition double (39/33 flips).
- 13260..13274: 15-row (b0 16/b1 01, quiet).
- 13275..13284: chatter-10 (32-flip @13275: b0 0e).
- 13285..13342: body (26-flip @13285: b0 e1/e7/e9 bands;
  b5 67->68 @13312). window cuts body (extend on demand).
- b4 ramp. split: ..13256 / 13257 dip / 13258..13284 / 13285...
