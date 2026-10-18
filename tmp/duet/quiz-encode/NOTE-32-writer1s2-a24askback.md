# NOTE-32 writer1s2 A-24 ask-back: slotmate distances for the 5 (0/5 skipper-signal)

- tiny/158 (probe/tiny.lz4.aar P=158): hashmates<P 1 (S=146, sole), VALIDATED 0 (collision, bytes differ). P-S=12, distinct(S,P]=12.
- 128/429 (win/128.aar P=429): hashmates 1 (S=404, sole), VALIDATED 0. P-S=25, distinct=25.
- w8/750 (win/w8.aar P=750): hashmates 1 (S=402, sole), VALIDATED 0. P-S=348, distinct=348.
- t8192/73725 (ttail/t8192.aar P=73725): hashmates 14, VALIDATED 1 (S=65533). most-recent hashmate 71153 is a COLLISION (bytes differ) and OVERWRITES 65533 before P. P-S=8192, distinct=8192 (borderline) but overwrite explains deterministically (eviction moot).
- t32768/96310 (ttail/t32768.aar P=96310): hashmates 11, VALIDATED 0. most-recent S=89273, P-S=7037, distinct=7037.
- VERDICT: 0/5 skipper-signal. 4/5 are validation-misses (sole/collision mates, bytes differ — my model already misses via 4B-validate). 1/5 (t8192) is overwrite-miss (validated older evicted by later collision-insert, deterministic last-write). Q-15 premise WITHDRAWN (attempt#1 confusion, not oracle behavior). No run-interior hunt needed from these.
