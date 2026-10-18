# NOTE-cport-hb29: relaunch, P108 merge gates running

- seat agent-1. tip C131 5db2d64 (PYID 3387, 6774/6774, n<=54320, 734 tiers).
- P108 staged verified: py+pins byte-same as w2 db278ab; test diff = lane RGRAM_BIN hook only.
- backlog 11: P108 db278ab > R106 c99f209 > P109 5960d11 > R107 7a7b269 > P110 c9b78a9 > R108 c8c3081 > P111 25e6dd7 > R109 d988d26 > P112 9b465a7 > R110 1eb6586 > P113 ba6e03b (n<=56152).
- plan: py gate (expect 6800) + SMOKE/UNITS fh > merge commit > C132 regen+PYID+C-green > next tier.
