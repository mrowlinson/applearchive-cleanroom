#!/usr/bin/env python3
"""gen_lzraventab.py -- extract lzraven synthesis tables from src/rgram.py.

Reads the 5 literal tables (_T2SCRAM, _T2W32, _T2W240, _T3CASC, _T3P245)
out of src/rgram.py and emits src/c/lzraventab.h. Deterministic: fixed
ordering, fixed hex case, no timestamps. Never imports rgram (267k
lines); parses the 5 assignment statements with ast instead.

Usage (repo root): python3 src/c/gen_lzraventab.py > src/c/lzraventab.h
Regenerate + diff whenever src/rgram.py tables change.
"""
import ast
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(_HERE))
WANT = ("_T2SCRAM", "_T2W32", "_T2W240", "_T3CASC", "_T3P245")


def main():
    with open(os.path.join(ROOT, "src", "rgram.py")) as f:
        tree = ast.parse(f.read())
    got = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id in WANT:
            got[node.targets[0].id] = ast.literal_eval(node.value)
    if set(got) != set(WANT):
        sys.stderr.write("missing tables: %s\n" % (set(WANT) - set(got)))
        return 1
    o = []
    o.append("/* lzraventab.h -- lzraven synthesis tables (GENERATED, DO NOT EDIT).")
    o.append(" * Extracted from src/rgram.py by: python3 src/c/gen_lzraventab.py")
    o.append(" * (run from repo root, output to src/c/lzraventab.h). Deterministic:")
    o.append(" * fixed order, lowercase hex, no timestamps. This header is the")
    o.append(" * only table copy the C encoder reads; never import rgram.py")
    o.append(" * (267k lines) on the C path.")
    o.append(" */")
    o.append("#ifndef AAE_LZRAVENTAB_H")
    o.append("#define AAE_LZRAVENTAB_H")
    o.append("#include <stdint.h>")
    o.append("")
    o.append("/* T2 g332 scramble rows, off 144..153. */")
    o.append("static const uint16_t LZRAV_T2SCRAM[10] = {%s};"
             % ", ".join("0x%04x" % v for v in got["_T2SCRAM"]))
    o.append("/* T2 post-lock window states, kw = min((off-153)>>4,4). */")
    o.append("static const uint16_t LZRAV_T2W32[5] = {%s};"
             % ", ".join("0x%04x" % v for v in got["_T2W32"]))
    o.append("/* T2 window bytes 30/31 alternates (byte30, field bits 249-253). */")
    o.append("static const uint8_t LZRAV_T2W240[5][2] = {%s};"
             % ", ".join("{0x%02x, 0x%02x}" % (a, b)
                         for a, b in got["_T2W240"]))
    o.append("/* T3 bytes16-19 cascade rows, off 219..228 (off-219 index). */")
    o.append("static const uint8_t LZRAV_T3CASC[10][4] = {%s};"
             % ", ".join("{%s}" % ", ".join("0x%s" % got["_T3CASC"][i][j:j + 2]
                                            for j in (0, 2, 4, 6))
                         for i in range(10)))
    o.append("/* T3 bytes16-19 settled states: 245-260, 261-276, 277-292, 293-308. */")
    o.append("static const uint8_t LZRAV_T3P245[4][4] = {%s};"
             % ", ".join("{%s}" % ", ".join("0x%s" % got["_T3P245"][i][j:j + 2]
                                            for j in (0, 2, 4, 6))
                         for i in range(4)))
    o.append("#endif")
    sys.stdout.write("\n".join(o) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
