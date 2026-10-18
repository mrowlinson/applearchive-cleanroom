# NOTE-w2s12-144: T10P92 COMMITTED @07de9d4

- tier: 48753..48844 (92 cells). S0 48753 + S1 48754, P92A
  48755..48770 (16x80B m-tab b6,7,72-75, raw lencode with
  in-zone b4 wrap 48767/68 ff->01 + b5 bump), P92B 48771..
  48780 (10x80B m-tab b6-11,76-79), P92Q 48781..48844 (4x16:
  M 7B b13-15,72-75 + 2+1+1 rows b6-11 + tails b76-79).
- gates: probe 92/92 CLOSED, storm 10/10, pins +38 pure,
  bat94 rc=0 RGRAM-GREEN 0 FAIL, SMOKE-GREEN.
- matches PRE-1267b. A-62 consumed (R90 agrees). Q-56 (B91)
  filed. frontier n=48844.
- next: T10B91 BLOCK regime (gen validated 73L, census on disk).
