#!/bin/sh
# sweep-setdiff.sh — verdict by setdiff vs base run (full keys), never eyeball.
# Usage: tests/sweep-setdiff.sh base.tsv new.tsv; exit 0 empty / 1 nonempty / 2 harness error.
# Scratch: sibling .sweep-sd-PID dir next to base file (stays in repo tmp when results do).
set -u
[ $# -eq 2 ] || { echo "usage: $0 base.tsv new.tsv" >&2; exit 2; }
[ -f "$1" ] && [ -f "$2" ] || { echo "SETDIFF-ERROR missing file" >&2; exit 2; }
echo "== base provenance =="; grep '^#' "$1" || true
echo "== new provenance =="; grep '^#' "$2" || true
SCR="$(dirname "$1")/.sweep-sd-$$"; mkdir -p "$SCR"
grep -v '^#' "$1" | sort > "$SCR/base"; grep -v '^#' "$2" | sort > "$SCR/new"
if cmp -s "$SCR/base" "$SCR/new"; then echo "SETDIFF-EMPTY"; rm -rf "$SCR"; exit 0; fi
echo "SETDIFF-NONEMPTY:"; diff "$SCR/base" "$SCR/new" || true; rm -rf "$SCR"; exit 1
