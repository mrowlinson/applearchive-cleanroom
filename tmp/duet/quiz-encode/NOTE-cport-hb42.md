# NOTE-cport-hb42: band144 no-upto switch, gates running

- seat agent-1 ACTIVE (PARENT-059). tip 6e9422a + WIP rgramc.c.
- find: WIP == upto-regen (2333878B); no-upto (2333823B) differs 55B. lesson kept: WITHOUT --upto.
- fh this seat: regen no-upto rc=0 tables 2010/2014 stderr 0, deterministic vs regen-b144; installed; build 0w (-O2 -Wall -Wextra -std=c11); PYID 3546/3546 rc=0.
- next: C-battery fh (bat144-c ran vs upto bin, invalid) + SMOKE/UNITS post-C-cut + commit band144 + NOTE-cport-band144. then R112 effd356 oldest-first.
