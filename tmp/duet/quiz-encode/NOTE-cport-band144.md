# NOTE-cport-band144: T10P114 sealed (n<=56500, 760 tiers)

- merge 6e9422a (w2 f906538, +2 tiers +24 pins): py RGRAM-GREEN 7092/7092 + SMOKE-GREEN fh.
- band 9f75d55 (rgramc.c +1355/-911, regen no-upto fh rc=0 tables 2010/2014 stderr 0 deterministic): PYID 3546/3546, C bat 7092/7092 GREEN fh (RGRAM_BIN=C), build 0w, SMOKE/UNITS fh post-C-cut.
- fix vs prior WIP: WIP was upto-regen (2333878B); correct no-upto (2333823B, 55B scope-guard delta) installed before gates. bat144-c (upto bin) superseded by batfh2-b144-c.
- next: R112 effd356 (+2 tiers +24 pins; expect 7116/7116, PYID 3558).
