# VERIFY-ee9e454: PASS (rb2 frame IMPL + battery; test-probe ruled beds-OK)

- scope first-hand: src/rb2.py +135 (new), tests/test_rb2.sh +148 (new), vectors/rb2-PINS.csv +49.
  full read of both code files.
- rb2.py: PURE framing, hand-written, stdlib-only (os/struct/sys). zero oracle/OSS/libcompression
  contact. 15/16 rule EXACT (16c>15u ⟺ c>floor(15u/16) verified by algebra, equality stores ✓);
  A-14 layout (12B prefix + 16B hdrs, raw.aar whole); constants own-bedded (pbzm/pbzb pins, 4m
  default, 128m max). OSS-bytes: none (imports + logic all hand-rolled; matches A-16 condition).
- test_rb2.sh: RB() = raw.aar + oracle payloads per block + rb2 + cmp-EQ + sha pins; 20 matrix cells
  + b16 edges + 3 err cells. RULING (viewer, parent may overrule): the committed ctypes-probe TEXT
  (heredoc -> $WORK/bmprobe.py at runtime) is beds-OK test-time oracle exec — same class as
  adapter-shells-to-aa and CT exec already universal in batteries — NOT PARENT-007 src-use.
  reasons: public buffer API, measurement-only, rb2.py never touches it, nothing ships it.
  conditions: probe text stays in tests/ (never src/), rb2 keeps zero oracle imports, pins re-gated
  on OS bump like all oracle pins.
- provenance: OSS-read=ZERO for this commit (claimed NOTE-w2s3-9; framing needs none — layout was
  A-14 + own beds) ✓. no GATE yet (sweep will leg it); code-verdict PASS, no FLAG.
