# NOTE-1066 viewer heartbeat (attempt14)

- VERIFYs filed this stretch (all PASS): P64 d952c6f, R63
  4a3a672, band60 8255033, merge55 cb10c8b, band61 42b1e16,
  merge56 6b8939e, band62 6a04351, merge57 eaed6ba, band63
  f8fc439, merge58 d228eb4, band64 ae6ab12, merge59 cb1f3e6,
  band65 9224481, merge60 d22cdc1, band66 a07ce91, merge61
  66f5b03, band67 17a2872, merge62 57108c8, band68 cac2faf,
  merge63 dc6552e, band69 a63744d, merge64 2a7fa9a, band70
  80d12c7, merge65 c19269e, band71 1b15add, merge66 4b3e3e8.
  422 VERIFY files in quiz.
- in-flight: band72 581c8f4 C battery (built 0w, 34 R63
  refs, wall 0, py-identical merge66).
- own-harness lessons: (1) test_rgram_c.sh shares py.out/
  c.out per workdir — concurrent runs MUST use dedicated
  workdirs (corpus symlink trick works); (2) wall-grep `r2`
  pattern hits tier labels T8R2/T10R2 — false positives,
  true patterns 0; (3) test_rgram.sh has no UNCOVERED
  semantics — RGRAM_BIN=C rerun on merge trees is EXPECTED
  RED whenever py frontier exceeds C scope (merge VERIFYs
  cite VERIFY-cb10c8b).
- zero open Q (latest Q-39 answered A-46).
- tips raced: w2 R67 c55aa3c, cport band76 9570115. Backlog:
  w2 P65/R64/P66/R65/P67/R66?/P68?/R67 + cport 73..76 +
  merges. Oldest-first continues.
- /tmp ban clean; TMPDIR seat exported every shell.
