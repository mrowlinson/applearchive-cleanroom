# PRE-1268b 96B BLOCK-regime 48845..49100: 16x16 template + P92M-tail q

## geometry (first-hand, WS tmp/encviewer-q37, census 48845..49100 on disk)
- 48845..49100 = 256 cells = 16 BLOCKS x 16 cells, ALL 96B/
  80B pay. Each block own sig (14 distinct: k1=k2, k6=k7
  share). 1st BLOCK regime (not R-zone: no m/q tabs —
  block-index k=off>>4 + in-block m=off&15).
- TEMPLATE 6B pos[18,19,72,73,74,75] = f(m) IDENTICAL all 16
  blocks EXACT 256/256, 16/16 distinct, ALL NEW (0/16 full
  + 0 sub>=5B vs corpus).
- PER-BLOCK bytes: sig[0,1,2,3] + q68[68,69,70,71] (const
  within block 16/16 each).
- REUSE 16/16 (32nd instance): block-k q68 = P92M[k] tail4
  (PRE-1267b quad-M tails byte-for-byte, in order k=0..15).
- byte4 counter EXACT 256/256: pay[4] = (0x9b + 2*off) & 0xFF
  (global across blocks; wraps inside k3/k11 blocks).
- byte5 EXACT 256/256: b5 = 0x7d + (off>=51) + (off>=179)
  (dbl-carry, b4-wrap-driven). wrap edges:
  48895 b4=255/b5=7d -> 48896 b4=1/b5=7e;
  49023 b4=255/b5=7e -> 49024 b4=1/b5=7f.
- 64 consts, 0 violations over 256 cells.
- per-block table (k, base, sig, q68=P92M tail):
  k0 48845 005edeb0 b4c50fe3 / k1 48861 8000feb0 69489a62
  k2 48877 8000feb0 d14af465 / k3 48893 0001feb0 87980c1c
  k4 48909 8001feb0 0a0caad1 / k5 48925 800e5ebb 3fe01981
  k6 48941 80105ebb 9ec1f272 / k7 48957 80105ebb d517a184
  k8 48973 802b5ebb 022875bf / k9 48989 002c5ebb 844c482e
  k10 49005 803e5ebb d5c39d75 / k11 49021 803f5ebb 04e71d8c
  k12 49037 004e5ebb a5109ffd / k13 49053 804f5ebb dfd6916c
  k14 49069 80545ebb cbe1c996 / k15 49085 80635ebb c10736ea
- 49101+ P-head: 49101 PB0 96B sig ee110100, 49102 PB1 96B
  sig 38fcd501, 49103..49118 PBA 16 96B sig 38fcd511,
  49119 PBB-single 96B sig ad259100, 49120..49128 PBB 9 96B
  SIG-VARIEGATED (ad358300/ad05a400/adfdb400/ad4dbe00/
  ad5d8600/...), 49129..49192 64-cell quad sig 38fcd508,
  49193+ next zone sig 38fcd5d1 (same family, 4th byte
  08->d1; extent open).

## template rows (T00..T15)
- 49746abcd57d 417692f45b94 5d769d742866 6976adbb470b
  6d76fefa8b67 4977597826ed 59777376a115 fd7763b75684
  fd777eb45aa1 fd77d6f9ada1 99782377a566 9d7816789701
  fd78feb99987 3d796ab6fbea 3d79ce726deb 197b98b6e308

## verdict: PRE-ANSWER (steers T10R65-96: block regime + P92M-tail q)
