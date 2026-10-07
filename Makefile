# aad decode — build outputs to NVME WS, never in repo.
OUTDIR ?= /Volumes/NVME/applearchive-cleanroom-ws/build/decode-writer
CC ?= cc
CFLAGS ?= -O2 -Wall

all: $(OUTDIR)/aad

$(OUTDIR)/aad: src/aad.c
	mkdir -p $(OUTDIR)
	$(CC) $(CFLAGS) -o $@ $< -lz -lcompression

clean:
	rm -f $(OUTDIR)/aad

.PHONY: all clean
