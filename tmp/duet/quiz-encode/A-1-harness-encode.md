# A-1 encode selector contract (MEASURED, 11 probes, macOS 27.0.1)

## AAR encode: dir-in, file-or-stdout-out
- argv: `aa archive -d SRCDIR -a ALG -t N -o OUT.aar` (E1: exit 0, stdout 0B, stderr 0B, 274B out for 2-file toy)
- omit `-o` -> archive bytes to STDOUT, exit 0, byte-identical to file form (E4 cmp-clean, 274B)
- stdin: NO stdin form (input is always a dir). missing `-d` -> exit 1 + `resolving target directory: Invalid argument` / `archive failed` (E8)
- `-o -` = LITERAL filename `-`, exit 0, stdout 0B (E5; stray removed). NOT stdio. Same class as decode-side `-` finding.
- missing srcdir -> exit 1 + `resolving target directory: No such file or directory` / `archive failed` (E2)
- bad `-a` -> exit 1 + full usage text on stderr (E7)
- determinism: two `-t 1` runs cmp-clean (E6). CONFIRMS fixtures-lane AAR verdict on this input.
- exit codes: 0 ok / 1 fail. success is silent both streams.

## AEA encrypt: stdin-ok, file-out-only
- argv: `aea encrypt -profile P ... -i IN -o OUT` (profile 5 + 32-char pw + `-a none` bedded)
- omit `-i` -> reads STDIN, exit 0, decrypt cmp-clean (E10/E11)
- omit `-o` -> exit 1 + `-o required` (E9). ASYMMETRY vs decrypt (which pipes stdout): encrypt demands `-o`.

## Adapter wrapper (lanes/harness-oracle @543bb13, UNMERGED)
- `harness/oracle-adapter.sh` 3793B sha256 c8f5271318d9395f0ded55c432468b90d1d8b6ac96c2bef6bd32ce7ed5ef49de (own hash; MATCHES decode-side A-002)
- `aar-encode --alg ALG [--block S] [--threads N] SRCDIR OUT` -> `aa archive -d SRCDIR -a ALG -t N [-b S] -o OUT` (threads default 1 in adapter; pin `-t 1` for byte-compare)
- `aea-encrypt --profile P [opts] IN OUT` -> `aea encrypt -profile P -t N ... -i IN -o OUT`
- exit 2 = adapter usage/missing-file error; oracle exit passes through otherwise
- adopt: `git show lanes/harness-oracle:harness/oracle-adapter.sh` (read-only; never read the lane worktree), or wait for parent merge
- GAP: adapter passes `-` through (oracle treats as literal file); stdio needs omit-flag form. Same gap as decode side.

## Contamination verdict: PASS (own grep, 5 files)
- files: oracle-adapter.sh c8f52713..., smoke.sh 56d751f9..., CLI-CONTRACT.md 8c6d8073..., BATTERY.md e887afb3..., README.md 269b3d3c... (own shasum)
- patterns: FUN_ | sub_[0-9a-f]{4,} | __TEXT | __text | ghidra/Ghidra | IDA | Hopper | Binary Ninja | otool | dyld_shared_cache | \.tbd | AppleArchive\.h | AA[A-Z]...\( -> NO HITS. safe to adopt.

## Oracle pins (this run): aa 527200B 823df81f... / aea 337040B 16bfbb1c... MATCH L4
