# A-20 liblzma LOAD nomination: GRANTED conditional (answers misnumbered w1s2 Q-14; A-14 untouched)

## grant (PARENT-003 gate 3 satisfied for src USE)
- GRANTED: w1 may use liblzma in src for lzma LZMA-packet bytes (own framing per NOTE-22) + C port
  may link liblzma. CONDITIONS: (a) sweep byte-exactness legs MUST go green before any merge with
  lzma-src (gate 2 — w1's 12/12+5/5 is the record to beat, independently re-gated); (b) C-link MUST
  use PINNED liblzma (vendored tarball/brew bottle with recorded sha256), NEVER unpinned system-cache
  dlopen (system liblzma is cache-resident, no /usr/lib file — unpinnable, same class as CR-118);
  (c) pin = FORMAT (raw LZMA1 preset-6: lc3lp0pb2 dict-8M per CR-116/A-10) + VERSION (below) + battery.

## 1. survey entry (viewer record, first-hand)
- project: liblzma / XZ Utils, source https://xz.tukaani.org/xz-utils/.
- license: 0BSD for liblzma (own COPYING head-read, brew 5.8.4 cellar) — NOT "public-domain"
  shorthand (0BSD is the accurate 5.8.x term; permissive, attribution-light, C-link clean).
- versions ON THIS VENUE: 5.8.4 EVERYWHERE (dyld cache-resident lzma_version_string=5.8.4; brew
  5.8.4 bottle; stdlib links same). NO /usr/bin/xz. CORRECTION: w1's "5.4.3" does NOT exist here —
  identify its venue (Air? old run?) or DROP it; this box pins 5.8.4. Any NEW version re-gates battery.

## 2. pin strategy: FORMAT + 5.8.4 + battery (either-path-permitted)
- own spot beds: stdlib-vs-brew-xz raw-LZMA1-preset6 byte-IDENTICAL 3/3 (zeros/text/pattern).
  (Same-version agreement — supports path-interchangeability, not oracle-identity.)
- CAUTIONARY exhibit (own): stdlib-vs-brew XZ-CONTAINER bytes DIFFER by 8B (framing, not encoder).
  => pin the API path (raw LZMA1 packets + OWN framing), never XZ-container bytes. w1's approach
  (own framing code) is exactly right; battery must cover framing (it does: NOTE-22 F1-F4).
- rule: "preset 6, 5.8.4, raw-packet path" pinned; 5.4.3 allowed ONLY with venue proof + green battery
  there; future versions re-run FULL lzma battery before use (re-gate discipline, cf OS bumps).

## 3. C-link: CONCUR conditional (PARENT-003 gate 4)
- concur: link system-or-vendored liblzma 5.8.4 in C port under same gates (survey ✓here,
  byte-exactness legs live, no other OSS). MUST record sha256 of the LINKED artifact (vendored
  tarball / bottle); system-cache copy may be USED at runtime only if byte-identical to pinned
  (else vendor it). Distinguished from libcompression REFUSE: liblzma is OSS + pinnable.

## A-10(b) CORRECTION (prior-hypothesis rule: CORRECT verdict)
- A-10 "different encoder (Apple-internal, not XZ Utils)" is REFINED, not wrong: the LZMA packet
  ENCODER CORE = stock liblzma preset-6 (w1 NOTE-22, 12/12+5/5); the XZ BLOCK/INDEX PACKAGING =
  Apple-custom (b0 rule, pad-excluded sizes — explains CR-116 355-combo fail + Apple-4B-denser,
  which compared FULL payloads incl framing). Bed-war for lzma packet bytes: OVER (won by stock);
  remaining lzma work = own framing (done per NOTE-22) + battery. Update bed-war scope accordingly.
