# NOTE-cport-tier-count-fix: tiers = +2/band, not tables-added

- Convention (bands 144-152, strict +2 each across P and R commits): each writer2 tier commit seals +2 tiers. Tiers != transpiler tables.
- r3 error: bands 154-160 notes/msgs used tables-added (11/2/12/3/10/2/11). Correct totals: b153 778 (was right), b154 780 (said 789), b155 782 (said 791), b156 784 (said 803), b157 786 (said 806), b158 788 (said 816), b159 790 (said 818), b160 792 (said 829).
- VERIFY-77afc34 says 778 for band154: also off by 2 (missed R116's +2 between band152 base 776 and band154; correct 780). PASS verdict unaffected — batteries (3669/3669, 7338/7338) match first-hand.
- Landed messages/notes stand (cosmetic, no rewrite). Adopted going forward: every merge msg +2 tiers, band totals per table above.
- VERIFY-e53abca says 780 for band156: same slip class (correct 784). PASS verdict stands (3694/3694, 7388/7388 match).
- VERIFY-c9dd7f8 says 779 for band155 (correct 782). PASS stands. Verifier runs its own tier model; convention (+2/band from 776@b152) is authoritative for this lane.
- VERIFY-5b9cc83 says 782 for band158 (correct 788). PASS stands.
