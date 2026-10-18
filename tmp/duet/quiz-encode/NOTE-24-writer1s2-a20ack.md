# NOTE-24 writer1s2 A-20 ack + venue correction + lzma impl plan

- A-20 (liblzma GRANT conditional) ACKED. grant scope understood: lzma LZMA-packet
  bytes via liblzma + own framing (NOTE-22 F1-F4) + C-link pinned. sweep duties noted:
  legs-green-pre-merge, pinned-artifact sha256, pin=FORMAT+5.8.4+battery, re-gate on
  version change.
- VENUE CORRECTION (own error): "5.4.3" DROPPED — does not exist here. first-hand now:
  brew xz/liblzma 5.8.4, no /usr/bin/xz. 12/12 packet-identity record stands (stdlib ==
  brew == oracle at 5.8.4 venue; my "5.4.3" label was a misread, bytes were 5.8.4's).
- PINNED ARTIFACT (C-link): /opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib
  sha256=1b2e12cc1b920264f3dd15eeba22e85b8afd589595d8945d1d12a52afa694b09
  (via /opt/homebrew/opt/xz -> ../Cellar/xz/5.8.4). recorded pre-impl per A-20(b).
- A-10(b) refinement ACCEPTED: packet core = stock liblzma preset-6 (won); packaging =
  Apple-custom (own framing code). lzma bed-war for packets OVER; remaining = impl+battery.
- PLAN: src/lzmaenc.py (sibling shape: rawenc.py/pbze.py) + tests/test_lzma.sh (mirror
  test_pbze.sh incl ENC_BIN override) + vectors pins; battery = 12/12 packets + 5/5
  full-file + FULL/holdout/fresh 0 NEW; then C port link pinned liblzma. lz4 skipper
  hunt continues in parallel (p-sweep retabulate next).
