# Discovery backlog (parent-owned, hardest first)

Standing queue for memo agents. Claim hardest open item first.
Mark guesses `[guess]`. Close with ANSWER link + verdict.

1. Goal definition: port vs independent impl vs format docs? OPEN.
   Owner decision. Never decided by lanes. Blocks all code.
2. AAR header layout: magic? version? flags? All UNRESOLVED.
   Probe: `aa archive` minimal inputs, diff bytes.
3. AAR codec IDs: how LZ4/LZMA/zlib/LZFSE selected/stored? UNRESOLVED. [guess] enum field in header.
4. AEA payload layer: embedded AAR or raw stream? UNRESOLVED.
   Probe: decrypt known AEA (own key), inspect plaintext structure.
5. AEA profiles: full profile-id table? FORMAT.md lists some; verify each
   against local `aea` behavior. UNRESOLVED completeness.
6. AppleArchive.framework API surface: public classes/functions list.
   Browser-read dev docs. UNRESOLVED (JS-gated fetch).
7. Compression framework algs: which overlap AAR codecs? UNRESOLVED.
   Browser-read dev docs.
8. `aa convert` matrix: which in/out formats? UNRESOLVED. Probe `aa -h`.
9. `aa manifest` / `verify` / `check-and-fix` semantics. UNRESOLVED.
   Probe with corrupted copies.
10. xip vs AAR/AEA relation. UNRESOLVED. [guess] xip predates, separate format.
11. Archive Utility current AAR write support? UNRESOLVED. Probe app behavior.
12. First vector set: minimal .aar per codec via local `aa`. Needs JOBS #1 first.
