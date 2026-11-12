# Unified product: `make` builds exactly ONE shipped binary (aae-cli).
# aad/aae/aeadc mains are linked in-process (cli.c calls aad_main/ae_main/
# aead_main); no execv of siblings, no backend env (AAD_BIN/AAE_C/AEAD_C gone).
# `make rgramc` builds the test-only grammar verifier separately (NOT in
# `all`, NOT shipped). The $(OUTDIR)/aad rule is test scaffolding only
# (python-mode tests/test_cli.sh $AAD_BIN): never a default target.
OUTDIR ?= build
CC ?= cc
CFLAGS ?= -O2 -Wall
# Pinned liblzma 5.8.4 per quiz A-20(b): direct link, never unpinned dlopen.
# sha256 1b2e12cc1b920264f3d5eeba22e85b8afd589595d8945d1d42a52afa694b09
# Overridable (LZMA_DYLIB= / LZMA_PREFIX= / LZMA_VER=); the default
# resolves the pinned cellar lib, homebrew first, /usr/local fallback.
# An empty pick fails the link with a message (never silently unpinned).
LZMA_VER ?= 5.8.4
LZMA_PREFIX ?= /opt/homebrew/opt/xz
LZMA_DYLIB ?= $(firstword $(wildcard /opt/homebrew/Cellar/xz/$(LZMA_VER)/lib/liblzma.5.dylib /usr/local/Cellar/xz/$(LZMA_VER)/lib/liblzma.5.dylib))

CLI_SRCS = src/c/cli.c src/aad.c src/c/aae.c src/c/lz4c.c src/c/lzravenc.c \
	   src/c/lzbitmapc.c src/c/aeadc.c
CLI_HDRS = src/c/lz4c.h src/c/lzravenc.h src/c/lzraventab.h \
	   src/c/lzbitmapc.h src/c/aeadc.h src/c/rgramc.h

all: $(OUTDIR)/aae-cli

aae-cli: $(OUTDIR)/aae-cli

$(OUTDIR)/aae-cli: $(CLI_SRCS) $(CLI_HDRS)
	mkdir -p $(OUTDIR)
	@if [ ! -f "$(LZMA_DYLIB)" ]; then echo "aae-cli: pinned liblzma $(LZMA_VER) not found (LZMA_DYLIB='$(LZMA_DYLIB)'); set LZMA_DYLIB=/path/to/liblzma.5.dylib (and LZMA_PREFIX if headers move too)" >&2; exit 1; fi
	$(CC) $(CFLAGS) -std=c11 -Wextra -DAAE_CLI_UNIFIED \
		-I$(LZMA_PREFIX)/include -o $@ $(CLI_SRCS) \
		-lz $(LZMA_DYLIB) -lcompression

# Test-only verifier (NOT in all, NOT shipped).
rgramc: $(OUTDIR)/rgramc

$(OUTDIR)/rgramc:
	$(MAKE) -C src/c BUILDDIR=$(abspath $(OUTDIR)) rgramc

# Test scaffolding for python-mode tests (NOT in all, NOT shipped).
$(OUTDIR)/aad: src/aad.c
	mkdir -p $(OUTDIR)
	$(CC) $(CFLAGS) -o $@ $< -lz -lcompression

clean:
	rm -f $(OUTDIR)/aae-cli $(OUTDIR)/aad $(OUTDIR)/aae $(OUTDIR)/aeadc $(OUTDIR)/rgramc

.PHONY: all clean aae-cli rgramc
