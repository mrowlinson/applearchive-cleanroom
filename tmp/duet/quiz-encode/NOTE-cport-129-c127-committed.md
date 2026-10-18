# NOTE-cport-129: C127 COMMITTED 3621528 (band127 T10R103)

- c482a73 partial-merge w2@26a5a51 (rgram.py +56, PINS +24,
  test N-list 1/1; 1 w2 commit R103, self-consistent band;
  RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6674/6674 py + SMOKE-GREEN.
- band127: rgramc.c --upto 53624. transpiler needed FH extension
  (new w2 construct bytes.fromhex(_T10P105M[q]) + tuple compare;
  qexp[i] emits hexval(qexp+2*i, 2); emission inspected + PYID-verified).
  tables 1899/1903, pre-gen identical to installed.
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3337/3337 GREEN +
  RGRAM-GREEN 6674/6674 py (merge tree, same-tree) +
  RGRAM-GREEN 6674/6674 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- mid-band incident: PYID + py batteries SIGTERM'd externally ~04:31Z
  (py was 2993 lines 0 FAIL); both reran fresh to GREEN. C battery stood.
- 726 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P106 next; w2 tip R105 aaf6e48).
