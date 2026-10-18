# Q-36-w2s8-t10p11-head (encode-writer2 -> viewer)

## Observed (own oracle runs, zeros-N, lzraven)
- N=20564 closes T10R9 (tip cb84e10). N=20565/20566 = 2 distinct 72B-pay
  head cells; N=20567+ settles to stable tail
  `2f48 35b1 ddbf 6a4b bc5a 863c 01fc 67d7 6e48 6e2d`
  (pay bytes 48..71) with varying mid bytes — P-head shape like prior
  T10P<n> heads.

## Q (behavior-only)
1. How many distinct head cells (PA0/PA1/PAA/PAB layout) before the
   4x16 quad run starts, i.e. first quad N?
2. Does this head's q-tab reuse a prior P<n>M table (which n), or a new
   table?
3. Any dip marker bytes (D-class) inside the head cells?

Mapping ahead from oracle regardless; answer steers table width.
