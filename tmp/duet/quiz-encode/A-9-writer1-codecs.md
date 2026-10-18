# A-9 raven/bitmap path, B/C stamps, >4GB (MEASURED)

## (a) lzraven: Apple-internal, no OSS. lzbitmap: OSS format-match, encode 10B off.
- lzraven: NO public codec found (survey negative stands; no new trace). pbzm block payload ==
  `compression_tool -encode -a lzraven` bytes EXACT (3228B bed) — iteration oracle for beds, NOT shippable.
  verdict: hardest encode gap. paths: (1) black-box bed-war reimplementation (writer+viewer iterative;
  start: tiny-input I/O beds), (2) ship without lzraven + document (PARENT decision), (3) decode-side
  format study informs encode (parent routes). no OSS nomination possible.
- lzbitmap: libzbitmap (eafer/Corellium, MIT, @574abea, WS oss-survey clone) vs oracle (4737B inner):
  OSS comp 3268B vs oracle 3228B (10B diff, same ZBM magic, scattered chunk-decision diffs, oracle denser).
  OSS zbm_decompress(oracle bytes) == raw EXACT (format-compatible; decode side may use OSS decode).
  verdict: OSS-nominatable for FORMAT + decode after quiz nomination (not yet nominated — file Q when wanted);
  byte-exact ENCODE needs encoder-decision hunt (chunking/matcher settings in OSS) or bed war.
- per-alg flips: PINNED (NOTE-012, filed after your Q-9): lz4/lzma/lzraven compress@100 store@300/500,
  lzbitmap store@100 compress@300 store@500 — ALL 12 match 15/16. no per-alg rule work left; only codec bytes.

## (b) B/C stamps + widths: CONFIRM all.
- dev.aar bed (own, root-mknod): CTM/MTM 'T' present, same S/T shapes as F (S iff nsec==0).
  UID'1' 0 (root file, minimal width), GID'1', MOD'2', FLG'1', DEV'4' right after PAT. your assumptions hold.
- socket: same minus XAT. widths follow 1/2/4 minimal rule everywhere observed.

## (c) >4GB: BEDDED (no longer OPEN).
- 4.5GB sparse file, -a raw: DAT kind 'C' + u64le len (0x120000000 = 4831838208 EXACT). widths: A(u16)->B(u32)->C(u64)
  minimal-width, same rule as ints. total 4831838451 = inner exact.
- same input -a lzfse: 1153 blocks (1152x4MB + tail) chain EXACT, comps ~2.6-2.8KB (zeros). pbze unc/comp u32
  never stressed (per-block <= blocksize <= 128m). multi-block at scale VERIFIED.
- XAT widening to B/C for giant xattrs: still OPEN (micro; xattrs cap ~128KB so likely moot).
- beds cleaned (4.8GB deleted post-measure); numbers above are the record.
