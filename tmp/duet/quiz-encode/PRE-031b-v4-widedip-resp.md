# PRE-031b wide-dip response = fragile class (restore/jump/transparent)

- N=8755 (mid-dip): pos0 -> 60->64 RESTORE; mid -> 60->68 JUMP;
  tail d=3/2/1 samelen 19/23/49 diffs.
- neighbor 8761 (64-tier): pos0 samelen 212 (no jump); mid 64->68;
  tail 19/23/45 — d=3/d=2 counts IDENTICAL to dip, d=1 49 vs 45.
- verdict: wide dip joins the fragile-dip response class (4209-shape:
  pos0-restores-tier signature ✓). width (10) is the only novelty.
