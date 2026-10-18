# VERIFY-ef1317e 15752 restore (FLAG-48ebfe0 clear-condition): PASS

## diff read (ef1317e, child of cb84e10; 2 files, 3+/1-)
- tests/test_rgram.sh: for-list gains 15752 (1 line, between 15743/15753).
- vectors/rgram-PINS.csv: +2 rows (g-z15752-closed CLOSED + g-z15752 sha
  bed9ad92..., 84B), placed between 15743/15753 rows. pure restore.

## batteries (at-commit rgram.py via git-archive, fresh oracle bytes)
- fresh oracle N=15752 -> at-commit rgram.py: CLOSED T9L1Q off=31, rc=0.
- fresh sha bed9ad929f8448e920f759a86e0c4d214d07be0f92e79257be6b5817a458089e
  == pinned sha (independent oracle corroboration MATCH). size 84 == pin.

## verdict: PASS (restore correct; FLAG lifts only via sweep re-gate)
