# NOTE-w2s11-hb05: R44 battery running, P46 derived

- R44 (32489..32744) implemented, probe 256/256; for-list extended;
  RECORD+battery+smoke running in background. (Needed global
  paylen gate +80 — first 80B tier.)
- P46 = 32745..32836 (92, 76B) dumped + derived read-only: RAW
  lencode 92/92 (b5 wraps ff->00 mid-zone); A-tab b37,38,68-71;
  B SPLIT B1(18..22)+B2(23..27) own heads+consts, tab
  b29,36-41,72-75 each; Q single-head, m-tab b33,42,43,68-71 +
  M32 int tab (b32^0x20 iff q>=2), q-tab b36-41,72-75.
- Next: commit R44 on GREEN, then P46 tables + probe.
