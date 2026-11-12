# aad decode — build outputs to NVME WS, never in repo.
OUTDIR ?= /Volumes/NVME/applearchive-cleanroom-ws/build/decode-writer
CC ?= cc
CFLAGS ?= -O2 -Wall

all: $(OUTDIR)/aad

$(OUTDIR)/aad: src/aad.c
	mkdir -p $(OUTDIR)
	$(CC) $(CFLAGS) -o $@ $< -lz -lcompression

# aae-cli C port (sibling lane C owns src/c/aae.c; this target only builds
# the CLI dispatcher + list reparse from src/c/cli.c).
# Pinned liblzma 5.8.4 per quiz A-20(b): direct link, never unpinned dlopen.
LZMA_PREFIX ?= /opt/homebrew/opt/xz
LZMA_DYLIB ?= /opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib

aae-cli: $(OUTDIR)/aae-cli

$(OUTDIR)/aae-cli: src/c/cli.c
	mkdir -p $(OUTDIR)
	$(CC) $(CFLAGS) -std=c11 -Wextra -I$(LZMA_PREFIX)/include -o $@ $< -lz $(LZMA_DYLIB) -lcompression

clean:
	rm -f $(OUTDIR)/aad $(OUTDIR)/aae-cli

.PHONY: all clean aae-cli
