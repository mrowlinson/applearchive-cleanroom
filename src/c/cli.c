/* cli.c - C port of src/aae-cli (unified impl-only entry point).
 *
 * Same argv shapes as the Python reference; backends are cleanroom ONLY:
 *   probe       provenance block (no backend)
 *   aar-encode  C encoder via $AAE_C (all 7 algs; backend refusals
 *               wrapped to CLI exit 2, same markers as Python)
 *   aar-decode  C decoder via $AAD_BIN (execv, all 7 algs)
 *   aar-list    pure C reparse of proto/aad.py parse_chain/parse_inner PAT walk
 *   aea-encrypt C AEAD via $AEAD_C (argv validated here; pending if absent)
 *   aea-decrypt C AEAD via $AEAD_C (argv validated here; pending if absent)
 *   aea-id      C AEAD via $AEAD_C (argv validated here; pending if absent)
 * Black-box + own proto only. No Python, no subprocess shims (execv only).
 */
#define _DARWIN_C_SOURCE 1
#include <compression.h>
#include <errno.h>
#include <fcntl.h>
#include <lzma.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/utsname.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>
#include <zlib.h>

#define NVME_WS "/Volumes/NVME/applearchive-cleanroom-ws"
#define AAD_DEFAULT NVME_WS "/build/decode-writer/aad"
#define AAE_DEFAULT NVME_WS "/build/aae/aae"
#define AEAD_DEFAULT NVME_WS "/build/cport-aead/aead"

static const char *SUPPORTED_ALGS = "raw,lzfse,zlib,lzma,lz4,lzraven,lzbitmap";

static int die_msg(const char *msg) {
    fprintf(stderr, "aae-cli: %s\n", msg);
    return 2;
}

/* ---------- argv parser (mirrors _parse_kv) ---------- */

typedef struct {
    const char *flag; /* "--alg" */
    const char *val;  /* NULL default */
} Opt;

static int parse_kv(int argc, char **argv, Opt *opts, int nopts,
                    char ***pos_out, int *npos_out,
                    char *errbuf, size_t errlen) {
    char **pos = malloc((size_t)(argc + 1) * sizeof *pos);
    int npos = 0, i = 0;
    if (!pos)
        return -2;
    while (i < argc) {
        const char *a = argv[i];
        if (!strcmp(a, "--")) {
            for (int j = i + 1; j < argc; j++)
                pos[npos++] = argv[j];
            break;
        }
        int hit = -1;
        for (int k = 0; k < nopts; k++) {
            if (!strcmp(a, opts[k].flag)) {
                hit = k;
                break;
            }
        }
        if (hit >= 0) {
            if (i + 1 >= argc) {
                snprintf(errbuf, errlen, "flag %s needs a value", a);
                free(pos);
                return -1;
            }
            opts[hit].val = argv[i + 1];
            i += 2;
        } else if (!strcmp(a, "-")) {
            pos[npos++] = argv[i++];
        } else if (a[0] == '-') {
            snprintf(errbuf, errlen, "unknown flag: %s", a);
            free(pos);
            return -1;
        } else {
            pos[npos++] = argv[i++];
        }
    }
    *pos_out = pos;
    *npos_out = npos;
    return 0;
}

static const char *opt_val(Opt *opts, int nopts, const char *name) {
    /* name without dashes, e.g. "alg" for "--alg" */
    for (int k = 0; k < nopts; k++) {
        if (!strcmp(opts[k].flag + 2, name))
            return opts[k].val;
    }
    return NULL;
}

static int is_reg_exec(const char *p) {
    struct stat st;
    if (stat(p, &st) != 0 || !S_ISREG(st.st_mode))
        return 0;
    return access(p, X_OK) == 0;
}

static const char *env_or(const char *name, const char *dflt) {
    const char *v = getenv(name);
    return (v && *v) ? v : dflt;
}

static int do_execv(const char *bin, char **args) {
    execv(bin, args);
    fprintf(stderr, "aae-cli: exec %s: %s\n", bin, strerror(errno));
    return 1;
}

static int mkdir_p(const char *path) {
    /* mkdir -p (parents, exist_ok). Returns 0 ok, -1 fail. */
    char tmp[8192];
    size_t n = strlen(path);
    if (n == 0 || n >= sizeof tmp)
        return -1;
    memcpy(tmp, path, n + 1);
    if (tmp[n - 1] == '/')
        tmp[n - 1] = '\0';
    for (char *p = tmp + 1; *p; p++) {
        if (*p == '/') {
            *p = '\0';
            if (mkdir(tmp, 0777) != 0 && errno != EEXIST)
                return -1;
            *p = '/';
        }
    }
    if (mkdir(tmp, 0777) != 0 && errno != EEXIST)
        return -1;
    return 0;
}

static int file_exists(const char *p) {
    struct stat st;
    return stat(p, &st) == 0;
}

/* ---------- probe ---------- */

static int cmd_probe(int argc, char **argv, const char *self) {
    struct utsname u;
    char date[32];
    time_t now;
    (void)argv;
    if (argc != 0)
        return die_msg("usage: aae-cli probe");
    uname(&u);
    now = time(NULL);
    strftime(date, sizeof date, "%Y-%m-%dT%H:%M:%SZ", gmtime(&now));
    printf("backend=impl-unified(aae-cli-c)\n");
    printf("date_utc=%s\n", date);
    printf("os=%s\n", u.sysname);
    printf("arch=%s\n", u.machine);
    printf("cli=%s\n", self);
    printf("aad_bin=%s\n", env_or("AAD_BIN", AAD_DEFAULT));
    printf("aae_c=%s\n", env_or("AAE_C", AAE_DEFAULT));
    printf("aead_c=%s\n", env_or("AEAD_C", AEAD_DEFAULT));
    printf("cc=%s\n", __VERSION__);
    return 0;
}

/* ---------- aar-encode ---------- */

static int valid_alg(const char *a) {
    static const char *k[] = {"raw",    "lzfse", "zlib", "lzma",
                              "lz4",    "lzraven", "lzbitmap"};
    for (size_t i = 0; i < 7; i++) {
        if (!strcmp(a, k[i]))
            return 1;
    }
    return 0;
}

/* encode.py parse_size: ^([0-9]+)([bkmg]?)$ lowercase only. -1 = no match. */
static long long parse_size_enc(const char *s) {
    size_t n = strlen(s), i = 0;
    unsigned long long v = 0;
    if (n == 0)
        return -1;
    while (i < n && s[i] >= '0' && s[i] <= '9') {
        v = v * 10 + (unsigned)(s[i] - '0');
        if (v > 0xFFFFFFFFFFFFFFFULL)
            return -2;
        i++;
    }
    if (i == 0)
        return -1;
    {
        unsigned long long m = 1;
        if (i < n) {
            if (i + 1 != n)
                return -1;
            switch (s[i]) {
            case 'b': m = 1; break;
            case 'k': m = 1024; break;
            case 'm': m = 1024ULL * 1024; break;
            case 'g': m = 1024ULL * 1024 * 1024; break;
            default: return -1;
            }
        }
        if (v > 0xFFFFFFFFFFFFFFFFULL / m)
            return -2;
        v *= m;
    }
    if (v > 0x7FFFFFFFFFFFFFFFULL)
        return -2;
    return (long long)v;
}

/* Run the encoder backend for raven/bitmap with stderr captured: the
 * backend exits 1 with the honest marker on refusal-class inputs, but the
 * CLI contract reserves 1 for operation failures and 2 for
 * usage/harness-level errors — the same wrap proto/encode.py callers get
 * via SystemExit (src/aae-cli:117-130). Success passes through (exit 0,
 * stderr forwarded verbatim). fork+exec of the backend only; no shims. */
static int run_encode_capture(const char *exe, char **args, const char *alg) {
    int pf[2];
    pid_t pid;
    char *cap = NULL;
    size_t capn = 0, capc = 0;
    int st;
    if (pipe(pf) != 0)
        return do_execv(exe, args); /* fallback: direct */
    pid = fork();
    if (pid < 0) {
        close(pf[0]);
        close(pf[1]);
        return do_execv(exe, args);
    }
    if (pid == 0) {
        dup2(pf[1], STDERR_FILENO);
        close(pf[0]);
        close(pf[1]);
        execv(exe, args);
        _exit(127);
    }
    close(pf[1]);
    for (;;) {
        char tmp[4096];
        ssize_t n = read(pf[0], tmp, sizeof tmp);
        if (n <= 0)
            break;
        if (capn + (size_t)n + 1 > capc) {
            size_t nc = capc ? capc * 2 : 8192;
            char *nn;
            while (nc < capn + (size_t)n + 1)
                nc *= 2;
            if (nc > (1 << 20))
                break; /* stop buffering huge stderr */
            nn = realloc(cap, nc);
            if (!nn)
                break;
            cap = nn;
            capc = nc;
        }
        if (capn + (size_t)n + 1 <= capc) {
            memcpy(cap + capn, tmp, (size_t)n);
            capn += (size_t)n;
        }
    }
    close(pf[0]);
    while (waitpid(pid, &st, 0) < 0 && errno == EINTR)
        ;
    if (WIFEXITED(st) && WEXITSTATUS(st) == 0) {
        if (capn)
            fwrite(cap, 1, capn, stderr);
        free(cap);
        return 0;
    }
    {
        /* wrapped refusal, byte-identical in form to the Python CLI */
        char *nl = cap ? memchr(cap, '\n', capn) : NULL;
        size_t ln = nl ? (size_t)(nl - cap) : capn;
        fprintf(stderr, "aae-cli: aar-encode --alg %s: %.*s\n", alg, (int)ln,
                cap ? cap : "");
        free(cap);
        return 2;
    }
}

static int cmd_aar_encode(int argc, char **argv) {
    static const char *flags[] = {"--alg", "--block", "--threads"};
    Opt opts[3] = {{"--alg", NULL}, {"--block", NULL}, {"--threads", NULL}};
    char err[1024], m[8192];
    char **pos = NULL;
    int npos = 0, r;
    const char *alg, *blk, *thr, *exe, *src, *dst;
    char *args[10];
    int na = 0;
    (void)flags;
    r = parse_kv(argc, argv, opts, 3, &pos, &npos, err, sizeof err);
    if (r != 0) {
        snprintf(m, sizeof m, "aar-encode: %s", err);
        free(pos);
        return die_msg(m);
    }
    alg = opt_val(opts, 3, "alg");
    if (!alg)
        alg = "raw";
    if (!valid_alg(alg)) {
        snprintf(m, sizeof m,
                 "aar-encode: unsupported alg '%s' (supported: %s)", alg,
                 SUPPORTED_ALGS);
        free(pos);
        return die_msg(m);
    }
    if (npos != 2) {
        free(pos);
        return die_msg("usage: aae-cli aar-encode --alg ALG [--block S] "
                       "[--threads N] SRCDIR OUT.aar");
    }
    src = pos[0];
    dst = pos[1];
    blk = opt_val(opts, 3, "block");
    if (blk) {
        long long v = parse_size_enc(blk);
        if (v >= 0 && (v < 1 || v > 134217728)) {
            snprintf(m, sizeof m,
                     "aar-encode --alg %s: invalid block size %lld "
                     "(oracle range 1..134217728)",
                     alg, v);
            free(pos);
            return die_msg(m);
        }
        /* regex failure: pass through; backend reports (exit 1 both). */
    }
    exe = env_or("AAE_C", AAE_DEFAULT);
    if (!is_reg_exec(exe)) {
        snprintf(m, sizeof m,
                 "missing C encode binary: %s "
                 "(build: make -C src/c BUILDDIR=<nvme>/build/aae)",
                 exe);
        free(pos);
        return die_msg(m);
    }
    thr = opt_val(opts, 3, "threads");
    args[na++] = (char *)exe;
    args[na++] = (char *)src;
    args[na++] = (char *)dst;
    args[na++] = "--alg";
    args[na++] = (char *)alg;
    if (blk) {
        args[na++] = "--block";
        args[na++] = (char *)blk;
    }
    if (thr) {
        args[na++] = "--threads";
        args[na++] = (char *)thr;
    }
    args[na] = NULL;
    free(pos);
    if (!strcmp(alg, "lzraven") || !strcmp(alg, "lzbitmap"))
        return run_encode_capture(exe, args, alg);
    return do_execv(exe, args);
}

/* ---------- aar-decode ---------- */

static int cmd_aar_decode(int argc, char **argv) {
    const char *exe, *src, *dst;
    char m[8192];
    char *args[8];
    if (argc != 2 || argv[0][0] == '-')
        return die_msg("usage: aae-cli aar-decode IN.aar OUTDIR");
    src = argv[0];
    dst = argv[1];
    if (!file_exists(src)) {
        snprintf(m, sizeof m, "missing: %s", src);
        return die_msg(m);
    }
    exe = env_or("AAD_BIN", AAD_DEFAULT);
    if (!is_reg_exec(exe)) {
        snprintf(m, sizeof m,
                 "missing C decode binary: %s "
                 "(build: make OUTDIR=<nvme>/build/decode-writer)",
                 exe);
        return die_msg(m);
    }
    if (mkdir_p(dst) != 0) {
        snprintf(m, sizeof m, "cannot mkdir: %s", dst);
        return die_msg(m);
    }
    args[0] = (char *)exe;
    args[1] = (char *)src;
    args[2] = (char *)dst;
    args[3] = NULL;
    return do_execv(exe, args);
}

/* ---------- aar-list: pure C reparse (proto/aad.py PAT walk) ---------- */

typedef struct {
    uint8_t *p;
    size_t n;
} Blob;

static int read_all(const char *path, Blob *out) {
    FILE *f = fopen(path, "rb");
    long sz;
    if (!f)
        return -1;
    if (fseek(f, 0, SEEK_END) != 0) {
        fclose(f);
        return -1;
    }
    sz = ftell(f);
    if (sz < 0) {
        fclose(f);
        return -1;
    }
    rewind(f);
    out->p = malloc((size_t)sz ? (size_t)sz : 1);
    if (!out->p) {
        fclose(f);
        return -1;
    }
    out->n = fread(out->p, 1, (size_t)sz, f);
    fclose(f);
    if (out->n != (size_t)sz) {
        free(out->p);
        out->p = NULL;
        return -1;
    }
    return 0;
}

static const char STREAM_TAIL[] =
    "Extraction failed\nextract failedError 0xbd011800\nNo more data\n"
    "read error\ntruncated stream\n"
    "archive stream read error (header)\nstream cancelled";
static const char NONSUPP[] =
    "Extraction failed\nextract failedError 0xbd035000\n"
    "Invalid/non-supported archive stream\n"
    "archive stream read error (header)\nstream cancelled";
static const char BSIZE_ERR[] =
    "Failed to create decompression stream\nError creating input stream\n"
    "extract failedError 0x9404c000\ninvalid block size";

static void t1_msg(char *b, size_t n, const char *code, const char *msg,
                   int blob) {
    if (blob)
        snprintf(b, n,
                 "Extraction failed\nextract failedError %s\n%s\n"
                 "istream read error\nRefill buffer failed\nread error\n"
                 "archive stream read error (blob)\nstream cancelled",
                 code, msg);
    else
        snprintf(b, n,
                 "Extraction failed\nextract failedError %s\n%s\n"
                 "istream read error\nrefill buffer\n"
                 "archive stream read error (header)\nstream cancelled",
                 code, msg);
}

/* decode one block payload -> malloc'd bytes (NULL + *fail=1 on failure). */
static uint8_t *dec_block(const char *magic, const uint8_t *pay, size_t comp,
                          unsigned long long unc, size_t *outlen, int *fail) {
    uint8_t *out;
    *fail = 0;
    if (comp == unc) {
        out = malloc(unc ? (size_t)unc : 1);
        if (!out) {
            *fail = 1;
            return NULL;
        }
        if (unc)
            memcpy(out, pay, (size_t)unc);
        *outlen = (size_t)unc;
        return out;
    }
    if (!memcmp(magic, "pbzz", 4)) {
        uLongf dl = (uLongf)unc;
        out = malloc(unc ? (size_t)unc : 1);
        if (!out) {
            *fail = 1;
            return NULL;
        }
        if (uncompress(out, &dl, pay, (uLong)comp) != Z_OK || dl != unc) {
            z_stream zs;
            memset(&zs, 0, sizeof zs);
            if (comp < 2 || inflateInit2(&zs, -15) != Z_OK) {
                free(out);
                *fail = 1;
                return NULL;
            }
            zs.next_in = (Bytef *)pay + 2;
            zs.avail_in = (uInt)(comp - 2);
            zs.next_out = out;
            zs.avail_out = (uInt)unc;
            {
                int r = inflate(&zs, Z_FINISH);
                size_t got = zs.total_out;
                inflateEnd(&zs);
                if (r != Z_STREAM_END || got != unc) {
                    free(out);
                    *fail = 1;
                    return NULL;
                }
            }
        }
        *outlen = (size_t)unc;
        return out;
    }
    if (!memcmp(magic, "pbzx", 4)) {
        lzma_stream zs = LZMA_STREAM_INIT;
        size_t cap = unc ? (size_t)unc : 1, have = 0;
        if (lzma_stream_decoder(&zs, UINT64_MAX, 0) != LZMA_OK) {
            *fail = 1;
            return NULL;
        }
        out = malloc(cap);
        if (!out) {
            lzma_end(&zs);
            *fail = 1;
            return NULL;
        }
        zs.next_in = pay;
        zs.avail_in = comp;
        for (;;) {
            lzma_ret r;
            if (have == cap) {
                uint8_t *no;
                cap *= 2;
                no = realloc(out, cap);
                if (!no) {
                    free(out);
                    lzma_end(&zs);
                    *fail = 1;
                    return NULL;
                }
                out = no;
            }
            zs.next_out = out + have;
            zs.avail_out = cap - have;
            r = lzma_code(&zs, LZMA_FINISH);
            have = cap - zs.avail_out;
            if (r == LZMA_STREAM_END)
                break;
            if (r != LZMA_OK) {
                free(out);
                lzma_end(&zs);
                *fail = 1;
                return NULL;
            }
        }
        lzma_end(&zs);
        if (have != unc) {
            free(out);
            *fail = 1;
            return NULL;
        }
        *outlen = have;
        return out;
    }
    if (!memcmp(magic, "pbze", 4)) {
        size_t dstn = (size_t)unc + 1;
        size_t scrn = compression_decode_scratch_buffer_size(COMPRESSION_LZFSE);
        uint8_t *dst = malloc(dstn ? dstn : 1);
        uint8_t *scr = malloc(scrn ? scrn : 1);
        size_t got;
        if (!dst || !scr) {
            free(dst);
            free(scr);
            *fail = 1;
            return NULL;
        }
        got = compression_decode_buffer(dst, dstn, pay, comp, scr,
                                        COMPRESSION_LZFSE);
        free(scr);
        if (got == unc && unc) {
            *outlen = got;
            return dst;
        }
        free(dst);
        *fail = 1;
        return NULL;
    }
    /* pbz4/pbzm/pbzb need out-of-scope backends: honest error, exit 1. */
    *fail = 1;
    return NULL;
}

static uint64_t rd64be(const uint8_t *p) {
    uint64_t v = 0;
    int i;
    for (i = 0; i < 8; i++)
        v = (v << 8) | p[i];
    return v;
}

/* parse_chain mirror. 0 ok; -1 FmtErr in errbuf. Partial inner returned
 * even on mid-blob returns (mid set). */
static int parse_chain(const uint8_t *data, size_t len, Blob *inner,
                       char *errbuf, size_t errlen, int *mid) {
    static const char *known[] = {"pbze", "pbz4", "pbzm",
                                  "pbzb", "pbzx", "pbzz"};
    uint64_t bsize, raw, pay;
    size_t off, ki;
    int ok;
    inner->p = NULL;
    inner->n = 0;
    *mid = 0;
    if (len == 0)
        return 0;
    if (len < 6) {
        snprintf(errbuf, errlen, "%s", STREAM_TAIL);
        return -1;
    }
    if (!memcmp(data, "AA01", 4) || !memcmp(data, "YAA1", 4)) {
        inner->p = malloc(len);
        if (!inner->p)
            return -1;
        memcpy(inner->p, data, len);
        inner->n = len;
        return 0;
    }
    if (len < 12) {
        snprintf(errbuf, errlen, "%s", NONSUPP);
        return -1;
    }
    ok = 0;
    for (ki = 0; ki < 6; ki++) {
        if (!memcmp(data, known[ki], 4)) {
            ok = 1;
            break;
        }
    }
    if (!ok) {
        snprintf(errbuf, errlen, "%s", NONSUPP);
        return -1;
    }
    bsize = rd64be(data + 4);
    if (bsize == 0 || bsize > 0x8000000ULL) {
        snprintf(errbuf, errlen, "%s", BSIZE_ERR);
        return -1;
    }
    off = 12;
    while (off < len) {
        int blob = inner->n >= 262144;
        size_t comp, have = 0;
        uint8_t *blk;
        int fail = 0;
        char m[512];
        if (off + 16 > len) {
            if (!blob) {
                t1_msg(m, sizeof m, "0x94034400", "truncated stream header",
                       0);
                snprintf(errbuf, errlen, "%s", m);
                return -1;
            }
            *mid = 1;
            return 0;
        }
        raw = rd64be(data + off);
        pay = rd64be(data + off + 8);
        if (raw > bsize || pay > bsize) {
            if (!blob) {
                t1_msg(m, sizeof m, "0x94036800", "corrupted stream header",
                       0);
                snprintf(errbuf, errlen, "%s", m);
                return -1;
            }
            *mid = 1;
            return 0;
        }
        comp = (size_t)pay;
        if (off + 16 + comp > len) {
            if (!blob) {
                t1_msg(m, sizeof m, "0x94036c00", "truncated stream payload",
                       0);
                snprintf(errbuf, errlen, "%s", m);
                return -1;
            }
            *mid = 1;
            return 0;
        }
        blk = dec_block((const char *)data, data + off + 16, comp, raw,
                        &have, &fail);
        if (!blk) {
            if (!blob) {
                t1_msg(m, sizeof m, "0x94039800",
                       "block decompression failed", 0);
                snprintf(errbuf, errlen, "%s", m);
                return -1;
            }
            *mid = 1;
            return 0;
        }
        if (have) {
            uint8_t *no = realloc(inner->p, inner->n + have);
            if (!no) {
                free(blk);
                return -1;
            }
            inner->p = no;
            memcpy(inner->p + inner->n, blk, have);
            inner->n += have;
        }
        free(blk);
        off += 16 + comp;
    }
    return 0;
}

typedef struct {
    char key[3];
    uint8_t st;
    const uint8_t *val; /* P/HASH/TS bytes (into file buf) */
    size_t vlen;        /* P byte len */
    unsigned long long bloblen; /* BLOB_W entries */
} Entry;

typedef struct {
    Entry *ents;
    size_t n, cap;
} Item;

static void item_push_ent(Item *it, const char key[3], uint8_t st,
                          const uint8_t *val, size_t vlen,
                          unsigned long long bloblen) {
    if (it->n == it->cap) {
        size_t nc = it->cap ? it->cap * 2 : 8;
        Entry *ne = realloc(it->ents, nc * sizeof *ne);
        if (!ne)
            return;
        it->ents = ne;
        it->cap = nc;
    }
    memcpy(it->ents[it->n].key, key, 3);
    it->ents[it->n].st = st;
    it->ents[it->n].val = val;
    it->ents[it->n].vlen = vlen;
    it->ents[it->n].bloblen = bloblen;
    it->n++;
}

static int uint_w(uint8_t st) {
    if (st == '1')
        return 1;
    if (st == '2')
        return 2;
    if (st == '4')
        return 4;
    if (st == '8')
        return 8;
    return 0;
}

static int blob_w(uint8_t st) {
    if (st == 'A')
        return 2;
    if (st == 'B')
        return 4;
    if (st == 'C')
        return 8;
    return 0;
}

static int hash_l(uint8_t st) {
    if (st == 'F')
        return 4;
    if (st == 'G')
        return 20;
    if (st == 'H')
        return 32;
    if (st == 'I')
        return 48;
    if (st == 'J')
        return 64;
    return 0;
}

static int ts_l(uint8_t st) {
    if (st == 'S')
        return 8;
    if (st == 'T')
        return 12;
    return 0;
}

/* parse one header at pos. 0 ok (endpos set); 1 = break; 2 = BLOBOVERRUN
 * short (item kept, then break). */
static int parse_one_hdr(const uint8_t *data, size_t len, size_t pos,
                         Item *it, size_t *endpos) {
    uint16_t hsize;
    size_t end, p, i;
    if (pos + 6 > len)
        return 1;
    if (memcmp(data + pos, "AA01", 4) && memcmp(data + pos, "YAA1", 4))
        return 1;
    hsize = (uint16_t)(data[pos + 4] | ((uint16_t)data[pos + 5] << 8));
    if (hsize < 6)
        return 1;
    end = pos + hsize;
    if (end > len)
        return 1;
    p = pos + 6;
    while (p < end) {
        uint8_t st;
        char key[3];
        int uw, bw, hl, tl;
        if (p + 4 > end)
            return 1;
        memcpy(key, data + p, 3);
        st = data[p + 3];
        p += 4;
        if (st == '*') {
            item_push_ent(it, key, st, NULL, 0, 0);
        } else if ((uw = uint_w(st)) > 0) {
            if (p + (size_t)uw > end)
                return 1;
            item_push_ent(it, key, st, NULL, 0, 0);
            p += (size_t)uw;
        } else if ((bw = blob_w(st)) > 0) {
            unsigned long long bl = 0;
            int b;
            if (p + (size_t)bw > end)
                return 1;
            for (b = 0; b < bw; b++)
                bl |= (unsigned long long)data[p + b] << (8 * b);
            p += (size_t)bw;
            if (!memcmp(key, "TYP", 3)) {
                item_push_ent(it, key, st, NULL, 0, 0);
                continue;
            }
            item_push_ent(it, key, st, NULL, 0, bl);
        } else if ((hl = hash_l(st)) > 0) {
            if (p + (size_t)hl > end)
                return 1;
            item_push_ent(it, key, st, data + p, (size_t)hl, 0);
            p += (size_t)hl;
        } else if ((tl = ts_l(st)) > 0) {
            if (p + (size_t)tl > end)
                return 1;
            item_push_ent(it, key, st, data + p, (size_t)tl, 0);
            p += (size_t)tl;
        } else if (st == 'P') 
{
            uint16_t ln;
            if (p + 2 > end)
                return 1;
            ln = (uint16_t)(data[p] | ((uint16_t)data[p + 1] << 8));
            if (p + 2 + ln > end)
                return 1;
            item_push_ent(it, key, st, data + p + 2, ln, 0);
            p += 2 + ln;
        } else {
            return 1;
        }
    }
    if (p != end)
        return 1;
    {
        size_t bp = end;
        for (i = 0; i < it->n; i++) {
            if (blob_w(it->ents[i].st) > 0 &&
                memcmp(it->ents[i].key, "TYP", 3)) {
                if (bp + it->ents[i].bloblen > len)
                    return 2;
                bp += (size_t)it->ents[i].bloblen;
            }
        }
        *endpos = bp;
    }
    return 0;
}

static int cmd_aar_list(int argc, char **argv) {
    Blob file = {NULL, 0}, inner = {NULL, 0};
    char err[1024], m[4096];
    Item *items = NULL;
    size_t nitems = 0, cap = 0, pos = 0, i;
    int mid = 0, rc = 1;
    if (argc != 1 || argv[0][0] == '-')
        return die_msg("usage: aae-cli aar-list IN.aar");
    if (!file_exists(argv[0])) {
        char m2[8192];
        snprintf(m2, sizeof m2, "missing: %s", argv[0]);
        return die_msg(m2);
    }
    if (read_all(argv[0], &file) != 0)
        return die_msg("aar-list: cannot read input");
    if (parse_chain(file.p, file.n, &inner, err, sizeof err, &mid) != 0) {
        snprintf(m, sizeof m, "aar-list: %s", err);
        fprintf(stderr, "aae-cli: %s\n", m);
        goto out;
    }
    (void)mid;
    while (pos < inner.n) {
        Item it = {NULL, 0, 0};
        size_t endpos = 0;
        int r = parse_one_hdr(inner.p, inner.n, pos, &it, &endpos);
        if (r == 1) {
            free(it.ents);
            break;
        }
        if (nitems == cap) {
            size_t nc = cap ? cap * 2 : 16;
            Item *ni = realloc(items, nc * sizeof *ni);
            if (!ni) {
                free(it.ents);
                goto out;
            }
            items = ni;
            cap = nc;
        }
        items[nitems++] = it;
        if (r == 2)
            break;
        pos = endpos;
    }
    for (i = 0; i < nitems; i++) {
        size_t e;
        for (e = 0; e < items[i].n; e++) {
            if (!memcmp(items[i].ents[e].key, "PAT", 3)) {
                if (items[i].ents[e].val && items[i].ents[e].vlen)
                    fwrite(items[i].ents[e].val, 1,
                           items[i].ents[e].vlen, stdout);
                fputc('\n', stdout);
                break;
            }
        }
    }
    rc = 0;
out:
    for (i = 0; i < nitems; i++)
        free(items[i].ents);
    free(items);
    free(file.p);
    free(inner.p);
    return rc;
}

/* ---------- aea (encrypt/decrypt via $AEAD_C) ---------- */

static int hexdig(char c) {
    return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f') ||
           (c >= 'A' && c <= 'F');
}

/* mirror _hexval */
static const char *hexval(const char *v, char *buf, size_t n) {
    size_t nd = 0;
    const char *p;
    if (!strncmp(v, "hex:", 4) || !strncmp(v, "base64:", 7))
        return v;
    for (p = v; *p; p++) {
        if (*p == ' ')
            continue;
        if (!hexdig(*p))
            return v;
        nd++;
    }
    if (nd % 2 != 0)
        return v;
    snprintf(buf, n, "hex:%s", v);
    return buf;
}

static int aead_bin(const char *sub, const char **bin_out) {
    const char *bin = env_or("AEAD_C", AEAD_DEFAULT);
    char m[8192];
    *bin_out = bin;
    if (is_reg_exec(bin))
        return 0;
    snprintf(m, sizeof m, "%s: pending: missing AEAD_C binary: %s", sub, bin);
    die_msg(m);
    return 2;
}

typedef struct {
    char **v;
    int n, cap;
} Argv;

static void av_push(Argv *a, char *s) {
    if (a->n + 1 >= a->cap) {
        int nc = a->cap ? a->cap * 2 : 32;
        char **nv = realloc(a->v, (size_t)nc * sizeof *nv);
        if (!nv)
            exit(1);
        a->v = nv;
        a->cap = nc;
    }
    a->v[a->n++] = s;
}

static void av_opt(Argv *a, const char *flag, const char *val) {
    if (val) {
        av_push(a, (char *)flag);
        av_push(a, (char *)val);
    }
}

static int cmd_aea_encrypt(int argc, char **argv) {
    static const char *flags[] = {
        "--profile", "--alg", "--block", "--threads", "--password",
        "--password-file", "--key", "--key-value", "--key-file",
        "--recipient-pub", "--sign-priv", "--checksum", "--padding",
        "--auth-data", "--auth-data-value", "--auth-data-key"};
    Opt opts[16];
    char err[1024], hv[8192], m[8192];
    char **pos = NULL;
    int npos = 0, r, i, rc;
    const char *profile, *src, *dst, *bin, *k;
    Argv a = {NULL, 0, 0};
    for (i = 0; i < 16; i++) {
        opts[i].flag = flags[i];
        opts[i].val = NULL;
    }
    r = parse_kv(argc, argv, opts, 16, &pos, &npos, err, sizeof err);
    if (r != 0) {
        snprintf(m, sizeof m, "aea-encrypt: %s", err);
        free(pos);
        return die_msg(m);
    }
    profile = opt_val(opts, 16, "profile");
    if (!profile || npos != 2) {
        free(pos);
        return die_msg("usage: aae-cli aea-encrypt --profile P [--alg A] "
                       "[--block S] [--threads N] "
                       "[--password PW|--key HEX|...] IN OUT");
    }
    src = pos[0];
    dst = pos[1];
    if (strcmp(src, "-") && !file_exists(src)) {
        snprintf(m, sizeof m, "missing: %s", src);
        free(pos);
        return die_msg(m);
    }
    if (aead_bin("aea-encrypt", &bin) != 0) {
        free(pos);
        return 2;
    }
    av_push(&a, (char *)bin);
    av_push(&a, "encrypt");
    av_push(&a, "--profile");
    av_push(&a, (char *)profile);
    av_opt(&a, "-a", opt_val(opts, 16, "alg"));
    av_opt(&a, "-b", opt_val(opts, 16, "block"));
    av_opt(&a, "--checksum", opt_val(opts, 16, "checksum"));
    av_opt(&a, "--padding", opt_val(opts, 16, "padding"));
    av_opt(&a, "--password", opt_val(opts, 16, "password"));
    av_opt(&a, "--password-file", opt_val(opts, 16, "password-file"));
    k = opt_val(opts, 16, "key");
    if (k)
        av_opt(&a, "--key-value", hexval(k, hv, sizeof hv));
    av_opt(&a, "--key-value", opt_val(opts, 16, "key-value"));
    av_opt(&a, "--key", opt_val(opts, 16, "key-file"));
    av_opt(&a, "--recipient-pub", opt_val(opts, 16, "recipient-pub"));
    av_opt(&a, "--sign-priv", opt_val(opts, 16, "sign-priv"));
    av_opt(&a, "--auth-data", opt_val(opts, 16, "auth-data"));
    av_opt(&a, "--auth-data-value", opt_val(opts, 16, "auth-data-value"));
    av_opt(&a, "--auth-data-key", opt_val(opts, 16, "auth-data-key"));
    if (strcmp(src, "-"))
        av_opt(&a, "-i", src);
    if (strcmp(dst, "-"))
        av_opt(&a, "-o", dst);
    av_push(&a, NULL);
    free(pos);
    rc = do_execv(bin, a.v);
    free(a.v);
    return rc;
}

static int cmd_aea_decrypt(int argc, char **argv) {
    static const char *flags[] = {
        "--password", "--password-file", "--key",   "--key-value",
        "--key-file", "--recipient-priv", "--sign-pub", "--range-offset",
        "--range-size"};
    Opt opts[9];
    char err[1024], hv[8192], m[8192];
    char **pos = NULL;
    int npos = 0, r, i, rc;
    const char *src, *dst, *bin, *k;
    Argv a = {NULL, 0, 0};
    for (i = 0; i < 9; i++) {
        opts[i].flag = flags[i];
        opts[i].val = NULL;
    }
    r = parse_kv(argc, argv, opts, 9, &pos, &npos, err, sizeof err);
    if (r != 0) {
        snprintf(m, sizeof m, "aea-decrypt: %s", err);
        free(pos);
        return die_msg(m);
    }
    if (npos != 2) {
        free(pos);
        return die_msg("usage: aae-cli aea-decrypt "
                       "[--password PW|--key HEX|...] IN OUT");
    }
    src = pos[0];
    dst = pos[1];
    if (strcmp(src, "-") && !file_exists(src)) {
        snprintf(m, sizeof m, "missing: %s", src);
        free(pos);
        return die_msg(m);
    }
    if (aead_bin("aea-decrypt", &bin) != 0) {
        free(pos);
        return 2;
    }
    av_push(&a, (char *)bin);
    av_push(&a, "decrypt");
    av_opt(&a, "--password", opt_val(opts, 9, "password"));
    av_opt(&a, "--password-file", opt_val(opts, 9, "password-file"));
    k = opt_val(opts, 9, "key");
    if (k)
        av_opt(&a, "--key-value", hexval(k, hv, sizeof hv));
    av_opt(&a, "--key-value", opt_val(opts, 9, "key-value"));
    av_opt(&a, "--key", opt_val(opts, 9, "key-file"));
    av_opt(&a, "--recipient-priv", opt_val(opts, 9, "recipient-priv"));
    av_opt(&a, "--sign-pub", opt_val(opts, 9, "sign-pub"));
    av_opt(&a, "--range-offset", opt_val(opts, 9, "range-offset"));
    av_opt(&a, "--range-size", opt_val(opts, 9, "range-size"));
    if (strcmp(src, "-"))
        av_opt(&a, "-i", src);
    if (strcmp(dst, "-"))
        av_opt(&a, "-o", dst);
    av_push(&a, NULL);
    free(pos);
    rc = do_execv(bin, a.v);
    free(a.v);
    return rc;
}

static int cmd_aea_id(int argc, char **argv) {
    const char *bin, *src;
    char m[8192], m2[8192];
    char *args[8];
    if (argc != 1)
        return die_msg("usage: aae-cli aea-id IN");
    src = argv[0];
    if (strcmp(src, "-") && !file_exists(src)) {
        snprintf(m2, sizeof m2, "missing: %s", src);
        return die_msg(m2);
    }
    if (aead_bin("aea-id", &bin) != 0)
        return 2;
    if (!strcmp(src, "-")) {
        /* stdin -> NVME temp file, fork/exec/wait, unlink (no shims). */
        const char *td = getenv("TMPDIR");
        char path[8192];
        uint8_t buf[65536];
        ssize_t n;
        int fd, st, outrc;
        pid_t pid;
        if (!td || !*td)
            td = NVME_WS "/tmp";
        if (mkdir_p(td) != 0)
            return die_msg("aar-list: cannot use TMPDIR");
        snprintf(path, sizeof path, "%s/aae-cli-id-XXXXXX", td);
        fd = mkstemp(path);
        if (fd < 0) {
            snprintf(m, sizeof m, "cannot mkstemp: %s", path);
            return die_msg(m);
        }
        while ((n = read(STDIN_FILENO, buf, sizeof buf)) > 0) {
            ssize_t w = 0;
            while (w < n) {
                ssize_t k = write(fd, buf + w, (size_t)(n - w));
                if (k <= 0) {
                    close(fd);
                    unlink(path);
                    return die_msg("aea-id: stdin spool failed");
                }
                w += k;
            }
        }
        close(fd);
        if (n < 0) {
            unlink(path);
            return die_msg("aea-id: stdin read failed");
        }
        pid = fork();
        if (pid < 0) {
            unlink(path);
            return die_msg("aea-id: fork failed");
        }
        if (pid == 0) {
            args[0] = (char *)bin;
            args[1] = "id";
            args[2] = "-i";
            args[3] = path;
            args[4] = NULL;
            execv(bin, args);
            _exit(127);
        }
        while (waitpid(pid, &st, 0) < 0 && errno == EINTR)
            ;
        unlink(path);
        if (WIFEXITED(st))
            outrc = WEXITSTATUS(st);
        else
            outrc = 1;
        return outrc;
    }
    args[0] = (char *)bin;
    args[1] = "id";
    args[2] = "-i";
    args[3] = (char *)src;
    args[4] = NULL;
    return do_execv(bin, args);
}

/* ---------- top level ---------- */

static void print_usage(void) {
    printf("usage: aae-cli %s\n",
           "probe|aar-encode|aar-decode|aar-list|aea-encrypt|aea-decrypt|"
           "aea-id");
    printf("impl-only backends (no oracle): encode=C aae decode=C aad "
           "list=C reparse encrypt/decrypt/id=C aead\n");
}

int main(int argc, char **argv) {
    const char *sub;
    char m[8192];
    if (argc < 2 || !strcmp(argv[1], "-h") || !strcmp(argv[1], "--help") ||
        !strcmp(argv[1], "help")) {
        print_usage();
        return argc < 2 ? 2 : 0;
    }
    sub = argv[1];
    if (!strcmp(sub, "probe"))
        return cmd_probe(argc - 2, argv + 2, argv[0]);
    if (!strcmp(sub, "aar-encode"))
        return cmd_aar_encode(argc - 2, argv + 2);
    if (!strcmp(sub, "aar-decode"))
        return cmd_aar_decode(argc - 2, argv + 2);
    if (!strcmp(sub, "aar-list"))
        return cmd_aar_list(argc - 2, argv + 2);
    if (!strcmp(sub, "aea-encrypt"))
        return cmd_aea_encrypt(argc - 2, argv + 2);
    if (!strcmp(sub, "aea-decrypt"))
        return cmd_aea_decrypt(argc - 2, argv + 2);
    if (!strcmp(sub, "aea-id"))
        return cmd_aea_id(argc - 2, argv + 2);
    snprintf(m, sizeof m, "unknown command: %s (see: aae-cli help)", sub);
    return die_msg(m);
}
