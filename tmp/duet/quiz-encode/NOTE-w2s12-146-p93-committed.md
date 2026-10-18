# NOTE-w2s12-146: T10P93 COMMITTED @c4e3cfa

- tier: 49101..49192 (92 cells). S0 49101 + S1 49102, P93A
  49103..49118 (16x80B m-tab b24-26,72-75), P93S 49119
  singleton, P93B 49120..49128 (9x80B variegated-sig m-tab
  b1,2,21-23,28,29,76-79), P93Q 49129..49192 (4x16: M 7B
  b28,30,31,72-75 + pair rows b14,15,21-25 + tails b76-79,
  b4=(0xd3+2off) b5=0x7f+(off>=23)).
- gates: probe 92/92 CLOSED, storm 12/12, pins +36 pure,
  bat96 rc=0 RGRAM-GREEN 0 FAIL, SMOKE-GREEN.
- matches PRE-1269b. Q-56/Q-57 open. frontier n=49192.
- next: T10R91 (gen validated 52L, census on disk, PRE-1270b).
  NOTE: map extends past 54k (100B regime @49541, PREs to
  P108) — ~48k estimate obsolete.
