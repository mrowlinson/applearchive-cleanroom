# A-18 raven tiny-input I/O: magic + framed-store (+16) + zeros flip at 64 (MEASURED)

## 1. tiny outputs (own beds, ct-oracle, rc=0 ALL incl empty)
- empty: out=12B `2b 00 ca ec 00 00 00 00 00 00 00 00` (magic + 8 zeros).
- 1B {00,ff,41}: out=17B; byte@12 = input byte verbatim (00/ff/41); rest fixed framing.
- 8B zeros: 24B. 8B distinct (00..07): 24B with input verbatim @12..20.
- 64B zeros: 60B (COMPRESSED). 64B pattern(00..3f): 80B = 64+16 (STORED).
- 1K zeros: 64B. 1K rand-s7: 1040B = 1024+16 (STORED). 1M zeros: 196B.
- store sweep (random s77): out = n+16 EXACT for n = 8/16/32/64/128/256/512/1024/2048.

## 2. STORE fallback: YES — framed-store, never bare; boundary content-dependent
- stored outputs embed input VERBATIM (proven: 1B variants, 8B-distinct, rand heads).
- overhead exactly +16B (12B head incl magic + 4B zero tail — see 3).
- zeros flip EXACT: 63 -> 79B STORE; 64 -> 60B COMPRESS (bisected 56..64, clean 2^6 edge).
- distinct-pattern (00-FF repeat): STORE at least to 80B (no flip — content rules, not size alone).
- no bare-output mode observed: every output carries magic + trailer (min 12B for empty).

## 3. magic + fixed structure
- magic `2b 00 ca ec` @0..4 EVERY output (matches w2 pbzm frame magic ✓).
- trailer `00 00 00 00` last 4B EVERY output (11/11 cases + 9 sweep pts).
- @4..8: zeros in tiny cases; 1M-zeros shows `00 00 00 40` (size-ish field, w2 hunt territory).
- @8..12 varies by case (01 10.. / 01 80.. / 00 c0 02.. / 01 00 40..) — header bits, not decoded here.
- hunt seeds: 1B/8B cases give minimal framed pairs (1 unknown input byte <-> fixed skeleton);
  zeros-63/64 pair brackets the store decision; 1M-zeros 196B shows multi-block scaling.
