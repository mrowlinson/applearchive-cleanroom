# A-4 first encode bed: empty + one-file inputs (MEASURED, `-t 1`, macOS 27.0.1)

## Prioritized encode entries (CLI-level; writer gap1 order)
1. `aa archive -d EMPTYDIR -a raw` — minimal inner format, no outer wrapper. START HERE.
2. `aa archive -d ONEDIR -a raw` — second header + DAT field appear. SECOND.
3. `aa archive -d EMPTYDIR -a lzfse` — outer stored-block wrapper, inner == bed 1 bytes. THIRD.
4. `aa archive -d ONEDIR -a lzfse` — outer COMPRESSED block (comp < unc). FOURTH.
- beds: EMPTYDIR = empty dir; ONEDIR = dir with one 0-byte file `empty.txt`. all `-t 1`.

## Bed numbers (sizes)
- empty/raw 113B | one/raw 241B | empty/lzfse 141B | one/lzfse 203B
- one/raw = dir entry 113B + file entry 128B (second `AA01` @0x71=113; counts: 113+128=241 exact)

## Bed 1: empty/raw 113B layout (offsets)
- @0: `41 41 30 31` (AA01) | @4: u16 `4D 00` (=77)
- @6: `54 59 50 31 44` (TYP, len 1, value `D`) — dir entry marker
- @11: `50 41 54 50 00` (PATP, empty) — empty path for root dir
- @16: `55 49 44 32 F5 01` (UID, 2B value F5 01) | @22: `47 49 44 31 14` (GID, 1B value 14)
- @27: `4D 4F 44 32 ED 01` (MOD, 2B value ED 01) | @33: `46 4C 47 31 00` (FLG, 1B 00)
- @38: `43 54 4D 54` + 8B value (CTM, 8-byte time) | @50: `4D 54 4D 54` + 8B value (MTM, 8-byte time)
- @62: `58 41 54 41 24 00` + blob: `24 00 00 00` + `com.apple.provenance` NUL + 5B `01 02 00 66 97` + `D0 7A BB 10 2C 73` — XAT field, total entry ends @113
- shape: magic + u16 + TLV fields (3-char key + len + value). TYP/PAT/UID/GID/MOD/FLG/CTM/MTM/XAT present; SIZ/DAT/cks/sh* ABSENT on dir entry.

## Bed 2 delta: one/raw file entry @113..241 (128B)
- `AA01` @113 | u16 `5C 00` (=92) @117 | TYP len1 `F` | PATP len9 `empty.txt`
- UID/GID/MOD/FLG/CTM/MTM same shapes as bed 1 (values differ: MOD `A4 01`)
- `44 41 54 41 00 00` (DAT, empty) — zero-length payload marker for 0-byte file
- XAT provenance blob same shape as bed 1
- verdict: file entry = same TLV chain + PAT filename + DAT field; CONFIRMS DAT-present-on-file vs absent-on-dir

## Bed 3: empty/lzfse 141B = 28B outer + 113B inner
- @0: `70 62 7A 65` (pbze) + 4 zero bytes + @8 `00 40 00 00` | @12: 16B block header: `00 00 00 00 | 00 00 00 71 | 00 00 00 00 | 00 00 00 71` (two 0x71=113 values)
- inner @28..141 cmp-clean vs bed-1 bytes (stored block: inner == raw output). VERIFIED by dd+cmp.
- outer overhead for stored case: 28B fixed.

## Bed 4: one/lzfse 203B = 28B outer + 175B compressed
- block header @12: `... 00 00 00 F1 ... 00 00 00 AF` (0xF1=241 unc, 0xAF=175 comp; comp < unc)
- verdict: small inputs take BOTH paths (stored when it wins, compressed otherwise) — writer must emit both. OPEN: exact store-vs-compress decision rule (probe: size sweep per alg).

## Repro (all `-t 1`, exit 0, silent)
- `aa archive -d <dir> -a <raw|lzfse> -t 1 -o <out>`; probe dir kept at /Volumes/NVME/applearchive-cleanroom-ws/tmp/encprobe.bEXeI3 (bed-*.aar + E*.out/.err)
