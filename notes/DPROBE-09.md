# DPROBE-09 truncation ladders + hsize split (writer1, first-hand)

Supersedes DPROBE-07 prefix ladder (retracted). All shapes exit+tree+
stderr IDENT three ways (76-shape matrix, 0 splits). Battery: hsize-floor,
hsize-end, outer-ladder, typ-multibyte cells (all oracle-diff).

## File length ladder (outermost)
- len 0: exit 0 SILENT, empty tree (empty archive).
- len 1..5 (ANY magic): exit 1 bd011800 stream-tail (NO `parsing entry
  header` line): `Extraction failed / extract failedError 0xbd011800 /
  No more data / read error / truncated stream / archive stream read
  error (header) / stream cancelled`.
- len 6..11: AA01/YAA1 magic -> inner parse (below); anything else
  (pbz-trunc, XXXX) -> bd035000 `Invalid/non-supported archive stream`
  + `(header)/cancelled` tail, exit 1.
- len >= 12: AA01/YAA1 -> inner = whole file; known pbz (e/4/m/b/x/z) ->
  chain walk; else (XXXX, pbzQ) -> bd035000, exit 1.

## Inner layer (raw bytes or decoded concat)
- empty inner: exit 0 SILENT (len-12-valid outer, q4 empty block).
- item loop at pos: pos+6>n -> stream-tail (same 7 lines as len 1..5).
- bad magic: pos==0 -> bd035000 (stream); pos>0 -> e800 `invalid header
  magic` + corrupted tail (entry).
- hsize<6 -> f000: `header size mismatch: stored N, got 6` + corrupted
  tail, exit 1 (N decimal echo; 0/1/2/5 first-hand).
- end>n -> bd011800 header-tail (WITH `parsing entry header` line),
  exit 1 (len+1, 0xffff first-hand).
- in-keys value overrun -> a400 `truncated header` + corrupted tail
  (hs1, hsbig IDENT; hsbig craft is TRUE in-keys overrun, NOT end>n).
- u16=len sharp: subtype path both sides (9c00 subtype 0 IDENT).
- u16=6: empty header -> no-TYP abort bd03ac00 (also at len 6/8/12
  with end<=n: r6-h6/r8-h6/r12-h6).
- bad subtype -> 9c00 `invalid field subtype: N` (decimal; 75/0/15..).
- blob overrun -> bd011800 blob-tail + `1 entries failed` count.

## Outer chain (pbz, len >= 12, magic+bsize valid)
- bsize u64be 0 or >0x8000000 -> 9404 4-line cascade (DPROBE-08, kept).
- block header short: bd009800 + `Truncated block header (have/16
  bytes read)` + NOP/processStream/decoder/cancelled (NO blank line).
- block payload short: bd009800 + `Truncated block payload
  (have/need bytes read)` (need = pay decimal).
- raw/pay > bsize -> Invalid-block-header 12-line cascade WITH blank
  line (DPROBE-08, kept). Validation precedes availability (ord-T).
- per-block counts (mb-t1 10/16, mb-t2 40/113 first-hand).
- multi-block inner = concat, parsed whole (mb12/mb21 TREE-MATCH).

## TYP dispatch (code-true; doc corrected, cells added)
- Full LE uint vs uppercase kinds F D L H P S B C; all else skips.
- TYP/2 0x0044 -> dir; TYP/4 0x46 -> file; FA/AF/AA skip; lowercase
  f/d/s skip; W/R/T/M skip (W viewer-confirmed, rest same family).
