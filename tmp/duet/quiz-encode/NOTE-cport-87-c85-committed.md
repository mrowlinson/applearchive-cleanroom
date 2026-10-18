# NOTE-cport-87: C85 COMMITTED 95e9d30 (band85 T10R73)

- b8b1278 partial-merge w2@93098c6 (R73 42517..42836,
  +2 tiers, +26 pins; UNGATED-at-merge, self-consistent band).
- band85: rgramc.c --upto 42836. regen IDENTICAL to
  predecessor dirty file (tables 1525/1529, clean, no ABORT).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2559/2559 GREEN +
  RGRAM-GREEN 5118/5118 py + RGRAM-GREEN 5118/5118 via
  RGRAM_BIN=C (0 FAIL) + SMOKE-GREEN + UNITS-GREEN.
- 602 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P75 007d272 + R74 1018e76).
