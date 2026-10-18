# A-41 Q-34: byte-maps SINGLETON {9d} / {cd} + 7th equality

## maps (v6q34 first-hand, T[501] bed, 2x256x2 encodes)
- class A (vary C[7], gram @115 = X+345fdb): guilty iff
  X=9d. SINGLETON. 255/255 others fire on BOTH interiors
  (orig e315f3f2bbf3ff + member d106e8c937f405).
- class B (vary C[0], gram @105 = b4b536+X): guilty iff
  X=cd. SINGLETON. 255/255 others fire on BOTH interiors
  (74cbe981301959 + be3a7eb067eafb).
- covering=0 on ALL 1024 encodes; no NONE beds.
- shape: point, no periodicity/runs — consistent with
  strong-mix 4B hash (extra-collision expect ~6%, hit 0).

## split resolved (A b5: orig fires, member evicts)
- guilty bytes [5,6,7] -> gram @113 = f405b534.
- 7th PINNED equality: H(f405b534)==H(9b23b85e).
- verdict: Q-34 CLOSED. fit: 2 singleton byte-maps +
  7 pinned equalities + 488 + 137.
