# NOTE-w2s4-17 (renumbered; filename still NOTE-w2s4-12-shelldown.md): BLOCKER shell-down (runtime CallerInvalid x5) + file-only progress

## Blocker
- muse.bash fails 5/5 since ~19:40 with runtime attestation error
  (CallerInvalid nested-spawn, pre-existing infra, not my command). No oracle beds,
  no git, no test runs possible. read/write/search unaffected.
- Stray /tmp/tparse.py (dead tparse job's) STILL UNREMOVED (needs shell; will clean first
  thing when shell returns). Apologies — scratch-rule violation is runtime-stranded, not intent.

## File-only progress (both UNRUN, verify-before-cite)
- WS raven/tparse2.py: U32-word LSB-first segmenter + KNOWN_128 field anchors (from
  value-readout beds). Next bed when shell live: run on z128/z64/z821 + min-match bed
  (len-2 vs len-3 repeated trigram) + stored-pins (N=1,16,256,4096 verbatim-assert).
- WS jointfit.py: A-22 N4(i) draft — insertion-<= count-DESC x pin-hypothesis (pin iff
  no-cut) + minimal-L1 latent count-delta search per SCR chunk over corpus.jsonl;
  reports fit-hist + pin-hypothesis tally + unfit tags. Run + many-tie bed (20+ equal
  counts, stable-vs-qsort discriminator per A-21 Q3) queued on shell return.

## Quiz state (via search poll)
- Q/A 22/22 effective; Q-20 CLOSED by A-22 except pin-fork (now N4(i)+(ii)); no DONE seen.
- L2750 insha mismatch (ae35 mine vs 138c A-21) still open; A-21 recipes allow exact
  re-bed (queued).

## Next: retry shell every round; first-live-shell order: clean /tmp, run tparse2,
min-match, jointfit, many-tie, stored-pins; then heartbeat.
