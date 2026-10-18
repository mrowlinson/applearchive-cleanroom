# PRE-008 N=129/p96/n=18 RESOLVED: presence-10 + exact-8 value (PRE-007 anomaly closed)

## 8-value scan (N=129, pos96, same pl=352)
- each value bit flips 11 = COMMON-10 {11,20,66,98,99,131,307,308,309,347} + 1 UNIQUE:
  bit0-3 -> {3,4,5,6}, bit4-7 -> {50,51,52,53} (two nibbles).
- multi-bit CONFIRMS presence (not XOR-linear): 0x03->{3,4}+10=12, 0x81->{3,53}+10=12,
  0x55->{3,5,50,52}+10=14, 0xff->18. common-10 flips for ANY nonzero value.
- VALUE STILL EXACT-8 (one unique slot per bit). w2's "normal split-field" hypothesis
  confirmed in stronger form: split value + presence rewrite.

## form note (vs N=128)
- common-10 includes skeleton markers 11, 131 + echo 307-309: at N=129 a TAIL dev
  TOUCHES skeleton (at N=128 tail devs never do — A-27). T1-form tail = holes + touch.
- N=128/129 share geometry for pos10-field but differ in tail/skeleton coupling.
