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

New from RESEARCH.md 2026-09-29 (hardest first among 13-19;
existing numbers untouched):
13. ipsw pure-Go AEA fallback: behavior-level summary only (which
    profiles/inputs it handles, failure modes). Compare vs FORMAT.md
    profile table (feeds #5). NEVER transcribe/port code. UNRESOLVED.
14. LZBITMAP codec: real? OS floor? Probe `aa -h`, Compression docs.
    UNRESOLVED. [guess] newer-OS-only codec id.
15. file.org AAR claims vs local `aa` bytes: AA01/YAA1 magic, 2-byte
    hdr size, TYP/PAT/UID/GID/MOD/DAT keys (feeds #2). UNRESOLVED
    until oracle-confirmed.
16. SIZ/CMP keys: confirm or drop. Docx-only, no second source found.
    UNRESOLVED. [guess] SIZ may be docx confabulation.
17. Native `aea` failure modes: reproduce 0xba006800 + auth-failed on
    local Apple Silicon? Probe Linux-absent + odd-tmpdir paths.
    UNRESOLVED. [guess] resource-contention claim is anecdotal.
18. XIP unwrap chain corroboration: `xar -xf` + pbzx + xz + cpio
    (feeds #10). Local tools only. UNRESOLVED.
19. Read Eclectic Light 2022 deep-dive, file behavior findings.
    <https://eclecticlight.co/2022/05/10/inside-apple-archive-more-than-a-compression-format/>
    Easiest. UNRESOLVED.
