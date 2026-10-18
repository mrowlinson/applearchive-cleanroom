# VERIFY-9d89fac w2 T10P49 (n=33789..33816, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-9d89fac)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 33789..33816: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=33788 CLOSED T10R47B off=255; next N=33817
 rc=2 (out of scope).
- labels: T10P490 at 33789; T10P49A at 33802 (off=11);
 T10P49B at 33816 (off=9). No Q tier.
- consts: P490C P491C P49A P49AC P49B P49BC only — no
 P49M/P49Q tables (short-tier shape confirmed).

## verdict: PASS
