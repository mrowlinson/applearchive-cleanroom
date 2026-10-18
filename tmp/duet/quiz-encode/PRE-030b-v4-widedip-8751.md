# PRE-030b WIDE DIP 8751..8760 (10 rows 60B amid 64B) — new dip class

## span + shape (v5k first-hand)
- EXACT span 8751..8760 (64B @8750 and @8761, clean entry/exit, all 10
  rows distinct shas). first wide (10-row) dip; prior dips: 1-2 rows.
- own flat frame: 10 var bytes (b4/31/39/46/47/55/56/57/58/59), 50 const.
  b4 = L10-lo +2/row (5f..71; 8751 L10-lo = 0x5F exact ✓).
- NOT 60-tier continuation: 0/10 hits on 60-head b9/b20 tabs (b9=df,
  b20=95, b13=2c const across dip vs tabbed tier).

## open
- response profile (fragile? restore? jump?) + selector: unprobed.
- more wide dips in 8991..11956 (64-tier unmapped) + selection rule.
- 64-tier head (v5j): 61 var bytes over 246 rows, NO 16-period anywhere
  (periods=[] all) — tier head is non-tabular; deep survey pending.
