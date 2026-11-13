# rgram_gen.py -- vendored verbatim from scratch tool.
# Source: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-cport/rgram_gen.py
# Vendored: 2026-11-12 (byte-identical below this header).
#!/usr/bin/env python3
"""rgram_gen.py -- AST transpiler: OUR src/rgram.py -> src/c/rgramc.c.

Clean-room own-code port (no oracle internals; source of truth is our
rgram.py + pins). Aborts loudly (line-numbered) on any unhandled
construct. Usage: rgram_gen.py RGRAM.PY OUT.C [--upto N] [--header OUT.H]
--upto N: emit only tiers with top-level `if n <= K`, K <= N (oldest-first
incremental commits); tables auto-pruned to referenced-only (0 warnings).
"""
import ast
import sys

fail_count = [0]


def abort(node, msg):
    ln = getattr(node, "lineno", "?")
    print("TRANSPILER-ABORT line %s: %s" % (ln, msg), file=sys.stderr)
    print(ast.dump(node)[:400], file=sys.stderr)
    fail_count[0] += 1
    raise SystemExit(1)


def c_escape(s):
    out = []
    for ch in s:
        o = ord(ch)
        if ch == '"':
            out.append('\\"')
        elif ch == "\\":
            out.append("\\\\")
        elif 32 <= o < 127:
            out.append(ch)
        else:
            out.append("\\x%02x" % o)
    return "".join(out)


# ---------------- module tables ----------------
class Tab:
    def __init__(self, name, kind, val, width=0):
        self.name = name
        self.kind = kind  # INT STR STRS PAIRS DICT
        self.val = val
        self.width = width


def classify(name, v, node):
    if isinstance(v, ast.Constant) and isinstance(v.value, str):
        return Tab(name, "STR", v.value)
    if isinstance(v, ast.Tuple) and v.elts:
        es = v.elts
        if all(isinstance(e, ast.Constant) and isinstance(e.value, int)
               and not isinstance(e.value, bool) for e in es):
            return Tab(name, "INT", [e.value for e in es])
        if all(isinstance(e, ast.Constant) and isinstance(e.value, str)
               for e in es):
            return Tab(name, "STRS", [e.value for e in es])
        if all(isinstance(e, ast.Tuple) and e.elts and
               all(isinstance(x, ast.Constant) and isinstance(x.value, int)
                   and not isinstance(x.value, bool) for x in e.elts)
               for e in es):
            w = len(es[0].elts)
            if any(len(e.elts) != w for e in es):
                abort(node, "ragged pair table " + name)
            return Tab(name, "PAIRS",
                       [[x.value for x in e.elts] for e in es], w)
    if isinstance(v, ast.Dict) and v.keys:
        if all(isinstance(k, ast.Constant) and isinstance(k.value, int)
               and isinstance(x, ast.Constant) and isinstance(x.value, str)
               for k, x in zip(v.keys, v.values)):
            return Tab(name, "DICT",
                       [(k.value, x.value)
                        for k, x in zip(v.keys, v.values)])
    abort(node, "unhandled table shape " + name)


def collect_tables(mod):
    tabs = {}
    for nd in mod.body:
        if isinstance(nd, ast.Assign):
            if len(nd.targets) != 1 or \
                    not isinstance(nd.targets[0], ast.Name):
                abort(nd, "odd module-level assign")
            nm = nd.targets[0].id
            tabs[nm] = classify(nm, nd.value, nd)
    return tabs


# ---------------- range filter (--upto) ----------------
def top_n_le(stmt):
    """Top-level `if n <= K` -> K, else None."""
    if not isinstance(stmt, ast.If):
        return None
    t = stmt.test
    if isinstance(t, ast.Compare) and len(t.ops) == 1 and \
            isinstance(t.ops[0], ast.LtE) and \
            isinstance(t.left, ast.Name) and t.left.id == "n" and \
            len(t.comparators) == 1 and \
            isinstance(t.comparators[0], ast.Constant):
        return t.comparators[0].value
    return None


def filter_range(body, upto):
    if upto is None:
        return body
    out = []
    for st in body:
        k = top_n_le(st)
        if k is not None and k > upto:
            break
        out.append(st)
    return out


# ---------------- type inference ----------------
# L long | S string(buf) | B bytes-slice(off,len) | P pair-ptr(width) |
# ROW fixed-array(width) | N1 none-able-long
class Infer:
    def __init__(self, tabs):
        self.tabs = tabs
        self.vt = {}  # name -> (tag, extra)

    def set(self, node, nm, tag, extra=None):
        if nm in ("pay", "raw", "n"):
            abort(node, "reassign prologue " + nm)
        old = self.vt.get(nm)
        if old is None:
            self.vt[nm] = (tag, extra)
            return
        if old[0] == "N1" and tag == "L" or \
                old[0] == "L" and tag == "N1":
            self.vt[nm] = ("N1", None)
            return
        if old != (tag, extra):
            abort(node, "type change %s %s -> %s" %
                  (nm, old, (tag, extra)))

    def typeof(self, node, e):
        """Classify expression kind for assignment typing."""
        if isinstance(e, ast.Constant):
            if isinstance(e.value, str):
                return ("S", None)
            if isinstance(e.value, bool) or e.value is None or \
                    isinstance(e.value, int):
                return ("N1" if e.value is None else "L", None)
            abort(node, "odd constant")
        if isinstance(e, ast.Name):
            if e.id in self.tabs:
                t = self.tabs[e.id]
                if t.kind == "PAIRS":
                    return ("P", t.width)
                if t.kind == "STR":
                    return ("S", None)
                if t.kind in ("STRS", "DICT", "INT"):
                    abort(node, "whole-table assign " + e.id)
            if e.id in self.vt:
                return self.vt[e.id]
            abort(node, "use before assign " + e.id)
        if isinstance(e, ast.Subscript):
            v = e.value
            if isinstance(v, ast.Name) and v.id == "pay" and \
                    isinstance(e.slice, ast.Slice):
                return ("B", self._slicebounds(node, e.slice))
            if isinstance(v, ast.Name) and v.id in self.tabs:
                t = self.tabs[v.id]
                if t.kind == "PAIRS" and \
                        not isinstance(e.slice, ast.Slice):
                    return ("ROW", t.width)
                return ("L" if t.kind == "INT" else "S", None)
            if isinstance(v, ast.Name) and v.id in self.vt:
                tag, _ = self.vt[v.id]
                if tag == "S":
                    if isinstance(e.slice, ast.Slice):
                        return ("S", None)
                    abort(node, "str index in assign")
                if tag == "ROW":
                    return ("L", None)
                abort(node, "subscript of %s in assign" % tag)
            if isinstance(v, ast.Subscript):
                v2 = v.value
                if isinstance(v2, ast.Name) and v2.id in self.tabs:
                    t = self.tabs[v2.id]
                    if t.kind == "PAIRS":
                        return ("L", None)
                    return ("S", None)
                abort(node, "nested subscript in assign")
            if isinstance(v, ast.Call):
                return ("S", None)  # .hex()[a:b]
            return ("L", None)
        if isinstance(e, ast.Tuple):
            if not e.elts:
                abort(node, "empty tuple")
            if all(not isinstance(x, ast.Tuple) for x in e.elts):
                return ("ROW", len(e.elts))
            if all(isinstance(x, ast.Tuple) and len(x.elts) == 2 and
                   all(isinstance(y, ast.Constant) and
                       isinstance(y.value, int) and
                       not isinstance(y.value, bool)
                       for y in x.elts) for x in e.elts):
                return ("P", 2)
            abort(node, "tuple literal shape")
        if isinstance(e, ast.Call):
            f = e.func
            if isinstance(f, ast.Attribute) and f.attr == "hex":
                return ("S", None)
            if isinstance(f, ast.Attribute) and f.attr == "fromhex" and \
                    isinstance(f.value, ast.Name) and \
                    f.value.id == "bytes" and len(e.args) == 1:
                at = self.typeof(node, e.args[0])
                if at[0] == "S":
                    return ("FH", None)
                abort(node, "fromhex of non-S")
            if isinstance(f, ast.Name) and f.id in ("bit", "grp", "len",
                                                    "int", "min"):
                return ("L", None)
            abort(node, "call in assign")
        if isinstance(e, ast.BinOp):
            if isinstance(e.op, ast.Add):
                lt = self.typeof(node, e.left)
                rt = self.typeof(node, e.right)
                if lt[0] == "S" or rt[0] == "S":
                    if lt[0] == "S" and rt[0] == "S":
                        return ("S", None)
                    abort(node, "mixed str add")
                return ("L", None)
            if isinstance(e.op, ast.Mod) and \
                    isinstance(e.left, ast.Constant) and \
                    isinstance(e.left.value, str):
                return ("S", None)
            return ("L", None)
        if isinstance(e, ast.IfExp):
            bt = self.typeof(node, e.body)
            ot = self.typeof(node, e.orelse)
            if bt[0] == "S" or ot[0] == "S":
                if bt[0] == "S" and ot[0] == "S":
                    return ("S", None)
                abort(node, "mixed ifexp str")
            if bt[0] == "ROW" or ot[0] == "ROW":
                if bt == ot:
                    return bt
                abort(node, "mixed ifexp row")
            if bt[0] == "P" or ot[0] == "P":
                if bt == ot:
                    return bt
                abort(node, "mixed ifexp pairtab")
            return ("L", None)
        if isinstance(e, ast.Dict):
            if not e.keys:
                abort(node, "empty dict")
            for k, x in zip(e.keys, e.values):
                if not (isinstance(k, ast.Constant) and
                        isinstance(k.value, int)):
                    abort(node, "dict key shape")
                if not (isinstance(x, ast.Name) and
                        x.id in self.tabs and
                        self.tabs[x.id].kind == "STR"):
                    abort(node, "dict value shape")
            return ("LD", len(e.keys))
        if isinstance(e, ast.BoolOp):
            return ("L", None)
        if isinstance(e, ast.UnaryOp):
            return ("L", None)
        if isinstance(e, ast.Compare):
            return ("L", None)
        abort(node, "untyped expr " + type(e).__name__)

    @staticmethod
    def _slicebounds(node, sl):
        lo = sl.lower.value if isinstance(sl.lower, ast.Constant) else None
        hi = sl.upper.value if isinstance(sl.upper, ast.Constant) else None
        if not isinstance(lo, int) or not isinstance(hi, int) or \
                sl.step is not None:
            abort(node, "non-literal bytes slice")
        return (lo, hi)

    def stmt(self, st):
        if isinstance(st, ast.Assign):
            if len(st.targets) != 1:
                abort(st, "multi-target assign")
            tg = st.targets[0]
            if isinstance(tg, ast.Tuple):
                if not isinstance(st.value, ast.Tuple) or \
                        len(tg.elts) != len(st.value.elts):
                    abort(st, "tuple unpack shape")
                for t, v in zip(tg.elts, st.value.elts):
                    if not isinstance(t, ast.Name):
                        abort(st, "nested unpack")
                    tag, ex = self.typeof(st, v)
                    self.set(st, t.id, tag, ex)
                return
            if not isinstance(tg, ast.Name):
                abort(st, "non-name assign target")
            if tg.id in ("raw", "pay", "n"):
                return  # prologue-handled
            tag, ex = self.typeof(st, st.value)
            self.set(st, tg.id, tag, ex)
            return
        if isinstance(st, ast.For):
            tg = st.target
            if isinstance(tg, ast.Name):
                self.set(st, tg.id, "L", None)
            elif isinstance(tg, ast.Tuple) and len(tg.elts) == 2 and \
                    all(isinstance(x, ast.Name) for x in tg.elts):
                self.set(st, tg.elts[0].id, "L", None)
                self.set(st, tg.elts[1].id, "L", None)
            else:
                abort(st, "for target shape")
            for s in st.body:
                self.stmt(s)
            if st.orelse:
                abort(st, "for/else")
            return
        if isinstance(st, ast.If):
            for s in st.body + st.orelse:
                self.stmt(s)
            return
        if isinstance(st, ast.AugAssign):
            if not isinstance(st.target, ast.Name):
                abort(st, "augassign target")
            if not isinstance(st.op, ast.BitOr):
                abort(st, "augassign op")
            # type must already be known (plain assign precedes)
            return
        if isinstance(st, (ast.Return, ast.Expr)):
            return
        abort(st, "unhandled stmt " + type(st).__name__)


# ---------------- versioning (tier-local name reuse) ----------------
class Versioner:
    """Locals reused with different types across tiers (e.g. exp as
    long in one tier, string in another) get versioned names."""

    def __init__(self, tabs):
        self.tabs = tabs
        self.inf = Infer(tabs)
        self.inf.set = self.tolerant_set
        self.cur = {}  # name -> [tag, ver]
        self.bumps = set()  # (id(node), name)

    def tolerant_set(self, node, nm, tag, extra=None):
        if nm in ("pay", "raw", "n"):
            return
        old = self.cur.get(nm)
        if old is None:
            self.cur[nm] = [tag, extra, 0]
            self.inf.vt[nm] = (tag, extra)
            return
        if tag == "LD":
            # every LD assign gets its own static arrays
            self.bumps.add((id(node), nm))
            self.cur[nm] = [tag, extra, old[2] + 1]
            self.inf.vt[nm] = (tag, extra)
            return
        if old[0] == "N1" and tag == "L" or \
                old[0] == "L" and tag == "N1":
            self.cur[nm] = ["N1", None, old[2]]
            self.inf.vt[nm] = ("N1", None)
            return
        if old[0:2] != [tag, extra]:
            self.bumps.add((id(node), nm))
            self.cur[nm] = [tag, extra, old[2] + 1]
            self.inf.vt[nm] = (tag, extra)

    def typeof(self, node, e):
        # resolve Name values through current version tags
        return self.inf.typeof(node, e)

    def scan(self, body):
        for st in body:
            self.inf.stmt(st)

    def rewrite(self, body):
        ver = {}

        def rn(nm):
            v = ver.get(nm, 0)
            return nm if v == 0 else "%s__v%d" % (nm, v)

        def rename_uses(e):
            for nd in ast.walk(e):
                if isinstance(nd, ast.Name) and nd.id in ver and \
                        isinstance(nd.ctx, ast.Load):
                    nd.id = rn(nd.id)

        def do_target(node, tg):
            if isinstance(tg, ast.Name):
                if (id(node), tg.id) in self.bumps:
                    ver[tg.id] = ver.get(tg.id, 0) + 1
                tg.id = rn(tg.id)
            elif isinstance(tg, ast.Tuple):
                for x in tg.elts:
                    do_target(node, x)

        def do_stmt(st):
            if isinstance(st, ast.Assign):
                tg = st.targets[0]
                if isinstance(tg, ast.Tuple):
                    for t, v in zip(tg.elts, st.value.elts):
                        rename_uses(v)
                    for t in tg.elts:
                        do_target(st, t)
                else:
                    rename_uses(st.value)
                    if isinstance(tg, ast.Name) and \
                            tg.id not in ("raw", "pay", "n"):
                        do_target(st, tg)
                return
            if isinstance(st, ast.For):
                rename_uses(st.iter)
                do_target(st, st.target)
                for s in st.body:
                    do_stmt(s)
                return
            if isinstance(st, ast.If):
                rename_uses(st.test)
                for s in st.body:
                    do_stmt(s)
                for s in st.orelse:
                    do_stmt(s)
                return
            if isinstance(st, ast.AugAssign):
                rename_uses(st.value)
                if isinstance(st.target, ast.Name):
                    st.target.id = rn(st.target.id)
                return
            if isinstance(st, (ast.Return, ast.Expr)):
                rename_uses(st.value)
                return
            abort(st, "version stmt " + type(st).__name__)

        for st in body:
            # init version map for prologue-skipped names
            do_stmt(st)

    def run(self, body):
        # seed: prologue names never versioned (Infer skips them)
        self.scan(body)
        nb = len(self.bumps)
        self.rewrite(body)
        return nb


# ---------------- emitter ----------------
class Emit:
    def __init__(self, tabs, vt, srclines):
        self.tabs = tabs
        self.vt = vt  # name -> (tag, extra)
        self.srclines = srclines
        self.out = []
        self.tempn = 0
        self.loopn = 0
        self.pending = []  # (indent, line) flushed before current stmt
        self.need = set()  # helper usage flags
        self.tabN = set()  # tables needing _N const
        self.folded = set()  # generated _uK folded arrays

    def newtemp(self):
        self.tempn += 1
        return "_t%d" % self.tempn

    def w(self, ind, s):
        self.out.append("    " * ind + s)

    def flush(self, ind):
        for _, ln in self.pending:
            self.w(ind, ln)
        self.pending = []

    # ---- helpers ----
    def vtype(self, node, nm):
        if nm in ("pay", "raw"):
            abort(node, "bare bytes name " + nm)
        if nm in self.vt:
            return self.vt[nm]
        abort(node, "unknown var " + nm)

    def str_ptr(self, node, e):
        """S-valued node -> C char* expression (no copy)."""
        if isinstance(e, ast.Name) and e.id in self.tabs and \
                self.tabs[e.id].kind == "STR":
            return e.id
        if isinstance(e, ast.Subscript):
            v = e.value
            if isinstance(v, ast.Name) and v.id in self.vt and \
                    self.vt[v.id][0] == "LD" and \
                    not isinstance(e.slice, ast.Slice):
                self.need.add("dictstr")
                return "dictstr(%s_KEYS, %s_VALS, %s_N, %s)" % (
                    v.id, v.id, v.id, self.E(e.slice))
            if isinstance(v, ast.Name) and v.id in self.tabs:
                t = self.tabs[v.id]
                idx = self.E(e.slice)
                if t.kind == "STRS":
                    return "%s[%s]" % (t.name, idx)
                if t.kind == "DICT":
                    self.need.add("dictstr")
                    return "dictstr(%s_KEYS, %s_VALS, %s_N, %s)" % (
                        t.name, t.name, t.name, idx)
            if isinstance(v, ast.Name) and v.id in self.vt and \
                    self.vt[v.id][0] == "S" and \
                    isinstance(e.slice, ast.Slice):
                sl = e.slice
                if sl.step is not None or sl.upper is not None:
                    abort(node, "bounded str slice as pointer")
                if sl.lower is None:
                    return v.id
                return "(%s + %s)" % (v.id, self.E(sl.lower))
        if isinstance(e, ast.Name) and e.id in self.vt and \
                self.vt[e.id][0] == "S":
            return e.id
        abort(node, "not an S-pointer expr")

    def slice_ptrlen(self, node, e):
        """S slice -> (ptr-expr, len-expr)."""
        if not isinstance(e, ast.Subscript) or \
                not isinstance(e.slice, ast.Slice):
            abort(node, "slice_ptrlen non-slice")
        sl = e.slice
        if sl.step is not None:
            abort(node, "str slice step")
        v = e.value
        if isinstance(v, ast.Subscript):
            base = self.str_ptr(node, v)
        elif isinstance(v, ast.Name):
            base = self.str_ptr(node, v)
        else:
            abort(node, "slice base shape")
        lo = self.E(sl.lower) if sl.lower is not None else "0"
        if sl.upper is None:
            return ("((%s) + (%s))" % (base, lo), None)
        hi = self.E(sl.upper)
        return ("((%s) + (%s))" % (base, lo),
                "((%s) - (%s))" % (hi, lo))

    # ---- L expressions -> inline C ----
    def E(self, e):
        if isinstance(e, ast.Constant):
            if isinstance(e.value, bool):
                return "1" if e.value else "0"
            if isinstance(e.value, int):
                return repr(e.value)
            abort(e, "str constant in L-expr")
        if isinstance(e, ast.Name):
            if e.id in ("n", "paylen", "rawlen"):
                return e.id
            if e.id in self.tabs:
                abort(e, "bare table in L-expr " + e.id)
            tag, _ = self.vtype(e, e.id)
            if tag in ("L", "N1"):
                return e.id
            abort(e, "non-L var in L-expr " + e.id)
        if isinstance(e, ast.BinOp):
            if isinstance(e.op, ast.Mod) and \
                    isinstance(e.left, ast.Constant) and \
                    isinstance(e.left.value, str):
                abort(e, "str-% outside fail/print")
            op = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*",
                  ast.Mod: "%", ast.LShift: "<<", ast.RShift: ">>",
                  ast.BitAnd: "&", ast.BitOr: "|", ast.BitXor: "^",
                  ast.FloorDiv: "/"}.get(type(e.op))
            if op is None:
                abort(e, "binop " + type(e.op).__name__)
            return "((%s) %s (%s))" % (self.E(e.left), op,
                                       self.E(e.right))
        if isinstance(e, ast.UnaryOp):
            op = {ast.USub: "-", ast.UAdd: "+", ast.Not: "!",
                  ast.Invert: "~"}.get(type(e.op))
            if op is None:
                abort(e, "unaryop")
            return "(%s(%s))" % (op, self.E(e.operand))
        if isinstance(e, ast.BoolOp):
            op = "&&" if isinstance(e.op, ast.And) else "||"
            parts = []
            for v in e.values:
                if isinstance(v, ast.Name):
                    tag, _ = self.vtype(e, v.id)
                    if tag in ("S", "B", "P", "ROW", "FH"):
                        abort(e, "non-bool Name in boolop")
                elif not isinstance(v, (ast.Compare, ast.BoolOp,
                                        ast.UnaryOp)):
                    abort(e, "non-bool value in boolop")
                code = self.E(v)
                if isinstance(v, ast.BoolOp):
                    code = "(%s)" % code
                parts.append(code)
            return (" %s " % op).join(parts)
        if isinstance(e, ast.IfExp):
            return "((%s) ? (%s) : (%s))" % (self.E(e.test),
                                             self.E(e.body),
                                             self.E(e.orelse))
        if isinstance(e, ast.Compare):
            return self.cmp(e)
        if isinstance(e, ast.Call):
            return self.call(e)
        if isinstance(e, ast.Subscript):
            return self.sub(e)
        abort(e, "L-expr " + type(e).__name__)

    def call(self, e):
        f = e.func
        if isinstance(f, ast.Attribute):
            abort(e, "method call in L-expr")
        if not isinstance(f, ast.Name):
            abort(e, "call shape")
        nm, ag = f.id, e.args
        if nm == "bit":
            if len(ag) != 2 or not isinstance(ag[0], ast.Name) or \
                    ag[0].id != "pay":
                abort(e, "bit args")
            self.need.add("bit")
            return "bit_at(pay, paylen, %s)" % self.E(ag[1])
        if nm == "grp":
            if len(ag) != 2 or not isinstance(ag[0], ast.Name) or \
                    ag[0].id != "pay":
                abort(e, "grp args")
            t = ag[1]
            if isinstance(t, ast.Tuple):
                self.need.add("grp_list")
                es = ", ".join("(long)(%s)" % self.E(x) for x in t.elts)
                return "grp_list(pay, paylen, (const long[]){%s}, %d)" % (
                    es, len(t.elts))
            if isinstance(t, ast.Call) and isinstance(t.func, ast.Name) \
                    and t.func.id == "tuple" and len(t.args) == 1 and \
                    isinstance(t.args[0], ast.Call) and \
                    isinstance(t.args[0].func, ast.Name) and \
                    t.args[0].func.id == "range" and \
                    len(t.args[0].args) == 2:
                self.need.add("grp_range")
                a0, a1 = t.args[0].args
                return "grp_range(pay, paylen, %s, %s)" % (self.E(a0),
                                                           self.E(a1))
            abort(e, "grp index shape")
        if nm == "len":
            if len(ag) != 1 or not isinstance(ag[0], ast.Name) or \
                    ag[0].id not in ("pay", "raw"):
                abort(e, "len args")
            return "paylen" if ag[0].id == "pay" else "rawlen"
        if nm == "int":
            if len(ag) == 1:
                # bool/cmp strip: C comparison already yields 0/1;
                # bare cmp matches committed precedent, e.g.
                # int(off >= 67) -> (off) >= (67) (callers parenthesize)
                if isinstance(ag[0], ast.Compare):
                    return self.E(ag[0])
                if isinstance(ag[0], ast.BoolOp):
                    return "(%s)" % self.E(ag[0])
                abort(e, "int() decimal outside prologue")
            if len(ag) != 2 or not isinstance(ag[1], ast.Constant) or \
                    ag[1].value != 16:
                abort(e, "int args")
            self.need.add("hexval")
            a0 = ag[0]
            if isinstance(a0, ast.Subscript) and isinstance(
                    a0.value, ast.Call):
                t0 = self.newtemp()
                hx = ast.Call(func=a0.value.func, args=[],
                              keywords=[])
                ast.copy_location(hx, a0.value)
                self.M_hex(hx, t0)
                sl = a0.slice
                if sl.step is not None or sl.lower is None or \
                        sl.upper is None:
                    abort(e, "int() of hex-slice bounds")
                lo, hi = self.E(sl.lower), self.E(sl.upper)
                return "hexval((%s) + (%s), (%s) - (%s))" % (t0, lo,
                                                             hi, lo)
            if isinstance(a0, ast.Subscript) and \
                    isinstance(a0.value, ast.Name) and \
                    a0.value.id in self.tabs and \
                    self.tabs[a0.value.id].kind == "STRS" and \
                    not isinstance(a0.slice, ast.Slice):
                p = self.str_ptr(e, a0)
                return "hexval(%s, (long)strlen(%s))" % (p, p)
            p, n = self.slice_ptrlen(e, a0)
            if n is None:
                abort(e, "int() of open slice")
            return "hexval(%s, %s)" % (p, n)
        if nm == "min":
            if len(ag) != 2:
                abort(e, "min arity")
            self.need.add("lmin")
            return "lmin(%s, %s)" % (self.E(ag[0]), self.E(ag[1]))
        abort(e, "call " + nm)

    def sub(self, e):
        v = e.value
        if isinstance(v, ast.Name) and v.id == "pay":
            if isinstance(e.slice, ast.Slice):
                abort(e, "pay slice in L-expr")
            return "(pay[%s])" % self.E(e.slice)
        if isinstance(v, ast.Name) and v.id in self.tabs:
            t = self.tabs[v.id]
            if isinstance(e.slice, ast.Slice):
                abort(e, "table slice in L-expr")
            idx = self.E(e.slice)
            if t.kind == "INT":
                return "(%s[%s])" % (t.name, idx)
            if t.kind == "PAIRS":
                abort(e, "pair-row in L-expr")
            abort(e, "str-table elem in L-expr")
        if isinstance(v, ast.Subscript):
            # pairTAB[i][j] or folded _uK[i][j]
            v2 = v.value
            if isinstance(v2, ast.Name) and \
                    not isinstance(v.slice, ast.Slice) and \
                    not isinstance(e.slice, ast.Slice) and \
                    ((v2.id in self.tabs and
                      self.tabs[v2.id].kind == "PAIRS") or
                     v2.id in self.folded):
                return "(%s[%s][%s])" % (v2.id, self.E(v.slice),
                                         self.E(e.slice))
            abort(e, "nested subscript")
        if isinstance(v, ast.Name) and v.id in self.vt and \
                self.vt[v.id][0] == "ROW":
            if isinstance(e.slice, ast.Slice):
                abort(e, "row slice")
            return "(%s[%s])" % (v.id, self.E(e.slice))
        if isinstance(v, ast.Name) and v.id in self.vt and \
                self.vt[v.id][0] == "B":
            if isinstance(e.slice, ast.Slice):
                abort(e, "bytes-var slice")
            off, _ = self.vt[v.id][1]
            return "(pay[%d + (%s)])" % (off, self.E(e.slice))
        if isinstance(v, ast.Name) and v.id in self.vt and \
                self.vt[v.id][0] == "FH":
            if isinstance(e.slice, ast.Slice):
                abort(e, "fromhex-var slice")
            self.need.add("hexval")
            return "(hexval((%s) + (2*(%s)), 2))" % (v.id,
                                                     self.E(e.slice))
        if isinstance(v, ast.Tuple):
            if isinstance(e.slice, ast.Slice):
                abort(e, "tuple-literal slice")
            es = ", ".join("(long)(%s)" % self.E(x) for x in v.elts)
            return "((const long[]){%s}[%s])" % (es, self.E(e.slice))
        if isinstance(v, ast.Call) and isinstance(v.func, ast.Attribute) \
                and v.func.attr == "fromhex" and isinstance(
                    v.func.value, ast.Name) and \
                v.func.value.id == "bytes" and len(v.args) == 1 and \
                isinstance(v.args[0], ast.Name) and \
                v.args[0].id in self.tabs and \
                self.tabs[v.args[0].id].kind == "STR" and \
                not isinstance(e.slice, ast.Slice):
            hx = self.tabs[v.args[0].id].val
            if len(hx) % 2:
                abort(e, "fromhex odd length")
            bs = bytes.fromhex(hx)
            self.loopn += 1
            k = self.loopn
            self.pending.append(
                (0, "static const uint8_t _f%d[] = {%s};" % (
                    k, ", ".join(repr(b) for b in bs))))
            return "(_f%d[%s])" % (k, self.E(e.slice))
        abort(e, "subscript shape")

    # ---- comparisons ----
    def kind(self, e):
        """Rough value kind: L S TUP ROWSUB BYTES OTHER."""
        if isinstance(e, ast.Tuple):
            return "TUP"
        if isinstance(e, ast.IfExp):
            a, b = self.kind(e.body), self.kind(e.orelse)
            if a == b:
                return a
            abort(e, "mixed ifexp kinds")
        if isinstance(e, ast.Name):
            if e.id == "n":
                return "L"
            if e.id == "pay":
                return "BYTES"
            if e.id in self.tabs:
                if self.tabs[e.id].kind == "STR":
                    return "S"
                return "TAB"
            if e.id in self.vt:
                tag, _ = self.vt[e.id]
                if tag in ("L", "N1"):
                    return "L"
                if tag == "S":
                    return "S"
                if tag == "B":
                    return "BYTES"
                if tag == "ROW":
                    return "TUP"
            abort(e, "kind of name " + e.id)
        if isinstance(e, ast.Subscript):
            v = e.value
            if isinstance(v, ast.Name) and v.id == "pay":
                return "L"
            if isinstance(v, ast.Name) and v.id in self.vt and \
                    self.vt[v.id][0] == "LD":
                return "S"
            if isinstance(v, ast.Name) and v.id in self.tabs:
                t = self.tabs[v.id]
                if t.kind == "INT":
                    return "L"
                if t.kind == "PAIRS":
                    return "TUP"
                return "S"
            if isinstance(v, ast.Subscript):
                v2 = v.value
                if isinstance(v2, ast.Name) and v2.id in self.tabs:
                    t2 = self.tabs[v2.id]
                    if t2.kind == "PAIRS":
                        return "L"
                    return "S"
                abort(e, "kind of nested subscript")
            if isinstance(v, ast.Tuple):
                return "L"
            if isinstance(v, ast.Name) and v.id in self.vt:
                tag = self.vt[v.id][0]
                if tag == "S":
                    return "S"
                if tag == "ROW" and \
                        not isinstance(e.slice, ast.Slice):
                    return "L"
                if tag == "B" and \
                        not isinstance(e.slice, ast.Slice):
                    return "L"
                if tag == "FH" and \
                        not isinstance(e.slice, ast.Slice):
                    return "L"
            if isinstance(v, ast.Call):
                if isinstance(v.func, ast.Attribute) and \
                        v.func.attr == "fromhex" and \
                        not isinstance(e.slice, ast.Slice):
                    return "L"
                return "S"  # .hex()[a:b]
            if isinstance(v, ast.BinOp) and \
                    Emit.fold_tuple(v) is not None:
                return "TUP"
            abort(e, "kind of subscript")
        if isinstance(e, ast.Call):
            f = e.func
            if isinstance(f, ast.Attribute) and f.attr == "hex":
                return "S"
            if isinstance(f, ast.Name) and f.id == "bytes":
                return "BYTES"
            return "L"
        if isinstance(e, ast.BinOp) and isinstance(e.op, ast.Mod) and \
                isinstance(e.left, ast.Constant) and \
                isinstance(e.left.value, str):
            return "S"
        if isinstance(e, ast.BinOp) and isinstance(e.op, ast.Add):
            kl, kr = self.kind(e.left), self.kind(e.right)
            if kl == "S" and kr == "S":
                return "S"
            if kl == "L" and kr == "L":
                return "L"
            abort(e, "mixed add kinds")
        return "L"

    @staticmethod
    def fold_tuple(node):
        """Constant tuple Add/Mult -> element list, or None."""
        if isinstance(node, ast.Tuple):
            return list(node.elts)
        if isinstance(node, ast.BinOp) and isinstance(
                node.op, ast.Mult):
            for a, b in ((node.left, node.right),
                         (node.right, node.left)):
                fa = Emit.fold_tuple(a)
                if fa is not None and isinstance(
                        b, ast.Constant) and isinstance(b.value, int):
                    return fa * b.value
            return None
        if isinstance(node, ast.BinOp) and isinstance(node.op,
                                                      ast.Add):
            fa, fb = Emit.fold_tuple(node.left), Emit.fold_tuple(
                node.right)
            if fa is not None and fb is not None:
                return fa + fb
            return None
        return None

    def tup_elems(self, e):
        """Tuple-valued node -> list of L-expr AST nodes."""
        if isinstance(e, ast.Tuple):
            return list(e.elts)
        if isinstance(e, ast.Subscript) and isinstance(e.value,
                                                       ast.BinOp):
            rows = Emit.fold_tuple(e.value)
            if rows is not None and rows and all(
                    isinstance(x, ast.Tuple) for x in rows):
                w = len(rows[0].elts)
                if any(len(x.elts) != w for x in rows):
                    abort(e, "folded width")
                for x in rows:
                    for y in x.elts:
                        if not isinstance(y, ast.Constant):
                            abort(e, "folded non-const")
                self.loopn += 1
                k = self.loopn
                self.folded.add("_u%d" % k)
                txt = ", ".join(
                    "{%s}" % ", ".join(repr(y.value)
                                       for y in x.elts)
                    for x in rows)
                self.pending.append(
                    (0, "static const long _u%d[][ %d ] = {%s};" % (
                        k, w, txt)))
                out = []
                for j in range(w):
                    nd = ast.parse("_u%d[0][%d]" % (k, j)).body[
                        0].value
                    nd.value.slice = e.slice
                    out.append(nd)
                return out
            abort(e, "unfoldable tuple arith")
        if isinstance(e, ast.Name) and e.id in self.vt and \
                self.vt[e.id][0] == "ROW":
            w = self.vt[e.id][1]
            return [ast.parse("%s[%d]" % (e.id, i)).body[0].value
                    for i in range(w)]
        if isinstance(e, ast.Subscript):
            v = e.value
            if isinstance(v, ast.Name) and v.id in self.tabs and \
                    self.tabs[v.id].kind == "PAIRS":
                t = self.tabs[v.id]
                out = []
                for j in range(t.width):
                    nd = ast.parse("%s[0][%d]" % (
                        t.name, j)).body[0].value
                    nd.value.slice = e.slice
                    out.append(nd)
                return out
        abort(e, "not tuple-valued")

    def cmp(self, e):
        ops = e.ops
        if len(ops) > 1:
            # chained: a <= b <= c -> pairwise &&
            parts = []
            left = e.left
            for op, right in zip(ops, e.comparators):
                if not isinstance(op, (ast.LtE, ast.Lt)):
                    abort(e, "chain op")
                one = ast.Compare(left=left, ops=[op],
                                  comparators=[right])
                ast.copy_location(one, e)
                parts.append(self.cmp(one))
                left = right
            return " && ".join(parts)
        op = ops[0]
        l, r = e.left, e.comparators[0]
        if isinstance(op, (ast.In, ast.NotIn)):
            if isinstance(r, ast.Tuple):
                code = " || ".join("((%s) == (%s))" % (self.E(l),
                                                       self.E(x))
                                    for x in r.elts)
                return ("(%s)" % code) if isinstance(op, ast.In) else \
                    ("!(%s)" % code)
            if isinstance(r, ast.Name) and r.id in self.tabs and \
                    self.tabs[r.id].kind == "DICT":
                self.need.add("dict_has")
                t = self.tabs[r.id]
                code = "dict_has(%s_KEYS, %s_N, (%s))" % (
                    t.name, t.name, self.E(l))
                return code if isinstance(op, ast.In) else \
                    "!(%s)" % code
            if isinstance(r, ast.Name) and r.id in self.vt and \
                    self.vt[r.id][0] == "LD":
                self.need.add("dict_has")
                code = "dict_has(%s_KEYS, %s_N, (%s))" % (
                    r.id, r.id, self.E(l))
                return code if isinstance(op, ast.In) else \
                    "!(%s)" % code
            abort(e, "membership shape")
        if isinstance(op, (ast.Is, ast.IsNot)):
            if not (isinstance(l, ast.Name) and
                    isinstance(r, ast.Constant) and r.value is None):
                abort(e, "is-comparand")
            tag, _ = self.vtype(e, l.id)
            if tag != "N1":
                abort(e, "is-None on non-N1")
            return "(%s_none)" % l.id if isinstance(op, ast.Is) else \
                "(!%s_none)" % l.id
        kl, kr = self.kind(l), self.kind(r)
        if kl == "TUP" or kr == "TUP":
            if kl != "TUP" or kr != "TUP":
                abort(e, "tuple vs non-tuple")
            if isinstance(op, (ast.Eq, ast.NotEq)):
                return self.tup_cmp(e, l, r,
                                    isinstance(op, ast.Eq))
            abort(e, "tuple ordering")
        if kl == "BYTES" or kr == "BYTES":
            if not isinstance(op, (ast.Eq, ast.NotEq)):
                abort(e, "bytes ordering")
            return self.bytes_cmp(e, l, r, isinstance(op, ast.Eq))
        if kl == "S" or kr == "S":
            if kl != "S" or kr != "S":
                abort(e, "str vs non-str")
            if not isinstance(op, (ast.Eq, ast.NotEq)):
                abort(e, "str ordering")
            return self.str_cmp(e, l, r, isinstance(op, ast.Eq))
        opm = {ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<",
               ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">="}.get(type(op))
        if opm is None:
            abort(e, "compare op")
        # no outer parens (-Wparentheses-equality); callers add them
        # only where an operator needs them (?: test, ! operand)
        return "(%s) %s (%s)" % (self.E(l), opm, self.E(r))

    def tup_cmp(self, node, l, r, is_eq):
        # distribute IfExp sides
        if isinstance(l, ast.IfExp) or isinstance(r, ast.IfExp):
            if isinstance(l, ast.IfExp) and isinstance(r, ast.IfExp):
                abort(node, "double-ifexp tuple cmp")
            if isinstance(l, ast.IfExp):
                t, o = l.test, r
                a = self.tup_cmp(node, l.body, r, True)
                b = self.tup_cmp(node, l.orelse, r, True)
            else:
                t, o = r.test, l
                a = self.tup_cmp(node, l, r.body, True)
                b = self.tup_cmp(node, l, r.orelse, True)
            code = "((%s) ? (%s) : (%s))" % (self.E(t), a, b)
            return code if is_eq else "!(%s)" % code
        le, re = self.tup_elems(l), self.tup_elems(r)
        if len(le) != len(re):
            abort(node, "tuple len mismatch")
        code = " && ".join("((%s) == (%s))" % (self.E(a), self.E(b))
                           for a, b in zip(le, re))
        return ("(%s)" % code) if is_eq else ("!(%s)" % code)

    def bytes_cmp(self, node, l, r, is_eq):
        bside = l if self.kind(l) == "BYTES" else r
        oside = r if bside is l else l
        blen = None
        if isinstance(bside, ast.Name) and bside.id in self.vt and \
                self.vt[bside.id][0] == "B":
            off, ln = self.vt[bside.id][1]
            blen = ln - off
            base = "(pay + %d)" % off
            boff = off
        elif isinstance(bside, ast.Name) and bside.id == "pay":
            base = "(pay)"
            boff = None
        else:
            abort(node, "bytes side shape")
        if isinstance(oside, ast.Call) and isinstance(oside.func,
                                                      ast.Name) and \
                oside.func.id == "bytes" and len(oside.args) == 1:
            a = oside.args[0]
            if not isinstance(a, ast.Tuple):
                self.need.add("zero")
                kc = self.E(a)
                if blen is not None:
                    if not (isinstance(a, ast.Constant) and
                            a.value == blen):
                        abort(node, "bytes(k) len mismatch")
                    code = "(memcmp(%s, ZERO76, %d) == 0)" % (base,
                                                              blen)
                else:
                    code = "((paylen == (%s)) && (memcmp(%s, ZERO76, " \
                        "(%s)) == 0))" % (kc, base, kc)
                return code if is_eq else "!(%s)" % code
            es = a.elts
            if boff is None:
                abort(node, "pay vs bytes-tuple")
            if len(es) != blen:
                abort(node, "bytes-tuple len mismatch")
            code = " && ".join(
                "((pay[%d]) == (%s))" % (boff + i, self.E(x))
                for i, x in enumerate(es))
            return ("(%s)" % code) if is_eq else ("!(%s)" % code)
        abort(node, "bytes comparand shape")

    def str_cmp(self, node, l, r, is_eq):
        # IfExp side -> distribute over materialized other side
        if isinstance(l, ast.IfExp) or isinstance(r, ast.IfExp):
            if isinstance(l, ast.IfExp) and isinstance(r, ast.IfExp):
                abort(node, "double-ifexp str cmp")
            t1, t2, tx = self.newtemp(), self.newtemp(), self.newtemp()
            if isinstance(l, ast.IfExp):
                tst, A, B, X = l.test, l.body, l.orelse, r
            else:
                tst, A, B, X = r.test, r.body, r.orelse, l
            self.M(A, t1)
            self.M(B, t2)
            self.M(X, tx)
            code = "(strcmp(%s, (%s) ? %s : %s) == 0)" % (tx,
                                                          self.E(tst),
                                                          t1, t2)
            return code if is_eq else "!(%s)" % code
        t1, t2 = self.newtemp(), self.newtemp()
        self.M(l, t1)
        self.M(r, t2)
        code = "(strcmp(%s, %s) == 0)" % (t1, t2)
        return code if is_eq else "!(%s)" % code

    # ---- S materialization: emit stmts writing node into buf ----
    def M(self, e, buf):
        if isinstance(e, ast.Constant) and isinstance(e.value, str):
            self.pending.append((0, 'strcpy(%s, "%s");' % (
                buf, c_escape(e.value))))
            return
        if isinstance(e, ast.IfExp):
            tst = self.E(e.test)
            self.pending.append((0, "if (%s) {" % tst))
            n0 = len(self.pending)
            self.M(e.body, buf)
            self.pending.append((0, "} else {"))
            self.M(e.orelse, buf)
            self.pending.append((0, "}"))
            # mark block lines (indent handled at flush: keep flat, the
            # C is still valid; readability secondary for temps)
            return
        if isinstance(e, ast.BinOp) and isinstance(e.op, ast.Add):
            self.M(e.left, buf)
            t = self.newtemp()
            self.M(e.right, t)
            self.pending.append((0, "strcat(%s, %s);" % (buf, t)))
            return
        if isinstance(e, ast.BinOp) and isinstance(e.op, ast.Mod) and \
                isinstance(e.left, ast.Constant) and \
                isinstance(e.left.value, str):
            r = e.right
            args = r.elts if isinstance(r, ast.Tuple) else [r]
            cfmt, outs = self.fmt_args(e, e.left.value, args)
            self.pending.append(
                (0, "snprintf(%s, sizeof %s, \"%s\", %s);" % (
                    buf, buf, c_escape(cfmt), ", ".join(outs))))
            return
        if isinstance(e, ast.Call) and isinstance(e.func, ast.Attribute) \
                and e.func.attr == "hex":
            self.M_hex(e, buf)
            return
        if isinstance(e, ast.Subscript):
            v = e.value
            if isinstance(e.slice, ast.Slice) and isinstance(
                    v, ast.Call):
                # .hex()[a:b]: materialize then slice
                t0 = self.newtemp()
                hx = ast.Call(func=v.func, args=[], keywords=[])
                ast.copy_location(hx, v)
                self.M_hex(hx, t0)
                sl = e.slice
                if sl.step is not None:
                    abort(e, "hex-slice step")
                lo = self.E(sl.lower) if sl.lower is not None else "0"
                if sl.upper is None:
                    self.pending.append((0, "strcpy(%s, %s + (%s));" % (
                        buf, t0, lo)))
                else:
                    hi = self.E(sl.upper)
                    self.pending.append(
                        (0, "{ long _n = (%s) - (%s); memcpy(%s, %s + "
                         "(%s), _n); %s[_n] = 0; }" % (hi, lo, buf,
                                                       t0, lo, buf)))
                return
            if isinstance(e.slice, ast.Slice):
                p, n = self.slice_ptrlen(e, e)
                if n is None:
                    self.pending.append((0, "strcpy(%s, %s);" % (
                        buf, p)))
                else:
                    self.pending.append(
                        (0, "{ long _n = %s; memcpy(%s, %s, _n); "
                         "%s[_n] = 0; }" % (n, buf, p, buf)))
                return
            # open index on STRS/DICT -> whole string
            p = self.str_ptr(e, e)
            self.pending.append((0, "strcpy(%s, %s);" % (buf, p)))
            return
        if isinstance(e, ast.Name):
            p = self.str_ptr(e, e)
            self.pending.append((0, "strcpy(%s, %s);" % (buf, p)))
            return
        abort(e, "materialize " + type(e).__name__)

    def M_hex(self, e, buf):
        self.need.add("hex_of")
        b = e.func.value
        if isinstance(b, ast.Name) and b.id == "pay":
            self.pending.append(
                (0, "hex_of(pay, paylen, %s);" % buf))
            return
        if isinstance(b, ast.Name) and b.id in self.vt and \
                self.vt[b.id][0] == "B":
            off, ln = self.vt[b.id][1]
            self.pending.append(
                (0, "hex_of(pay + %d, %d, %s);" % (off, ln - off,
                                                   buf)))
            return
        if isinstance(b, ast.Subscript) and isinstance(b.value,
                                                      ast.Name) and \
                b.value.id == "pay" and isinstance(b.slice, ast.Slice):
            sl = b.slice
            if sl.step is not None or sl.lower is None or \
                    sl.upper is None:
                abort(e, "pay hex slice bounds")
            lo, hi = self.E(sl.lower), self.E(sl.upper)
            self.pending.append(
                (0, "{ long _a = %s, _b = %s; "
                 "hex_of(pay + _a, _b - _a, %s); }" % (lo, hi, buf)))
            return
        if isinstance(b, ast.Call) and isinstance(b.func, ast.Name) \
                and b.func.id == "bytes" and len(b.args) == 1 and \
                isinstance(b.args[0], (ast.Tuple, ast.List)):
            es = b.args[0].elts
            self.loopn += 1
            k = self.loopn
            self.pending.append(
                (0, "{ uint8_t _b%d[%d];" % (k, len(es))))
            for i, x in enumerate(es):
                self.pending.append(
                    (0, "_b%d[%d] = (uint8_t)(%s);" % (k, i,
                                                      self.E(x))))
            self.pending.append(
                (0, "hex_of(_b%d, %d, %s); }" % (k, len(es), buf)))
            return
        abort(e, "hex base shape")

    # ---- statements ----
    def is_argv_check(self, st):
        if not isinstance(st, ast.If):
            return False
        for nd in ast.walk(st.test):
            if isinstance(nd, ast.Attribute) and nd.attr == "argv" \
                    and isinstance(nd.value, ast.Name) and \
                    nd.value.id == "sys":
                return True
        return False

    def is_raw_assign(self, st):
        return isinstance(st, ast.Assign) and \
            len(st.targets) == 1 and \
            isinstance(st.targets[0], ast.Name) and \
            st.targets[0].id == "raw"

    def is_n_assign(self, st):
        return isinstance(st, ast.Assign) and \
            len(st.targets) == 1 and \
            isinstance(st.targets[0], ast.Name) and \
            st.targets[0].id == "n"

    def is_pay_assign(self, st):
        return isinstance(st, ast.Assign) and \
            len(st.targets) == 1 and \
            isinstance(st.targets[0], ast.Name) and \
            st.targets[0].id == "pay"

    def stmt(self, st, ind, top=False):
        if top and self.is_argv_check(st):
            return "argv"
        if top and self.is_raw_assign(st):
            return "raw"
        if top and self.is_n_assign(st):
            return "ninit"
        if top and self.is_pay_assign(st):
            self.pay_assign(st, ind)
            return None
        if isinstance(st, ast.Assign):
            self.do_assign(st, ind)
        elif isinstance(st, ast.AugAssign):
            tg = st.target
            if not isinstance(tg, ast.Name) or \
                    not isinstance(st.op, ast.BitOr):
                abort(st, "augassign shape")
            tag, _ = self.vtype(st, tg.id)
            if tag != "L":
                abort(st, "augassign non-L")
            code = self.E(st.value)
            self.flush(ind)
            self.w(ind, "%s = ((%s) | (%s));" % (tg.id, tg.id, code))
        elif isinstance(st, ast.If):
            self.do_if(st, ind)
        elif isinstance(st, ast.For):
            self.do_for(st, ind)
        elif isinstance(st, ast.Return):
            self.do_return(st, ind)
        elif isinstance(st, ast.Expr):
            self.do_print(st, ind)
        else:
            abort(st, "stmt " + type(st).__name__)
        return None

    def pay_assign(self, st, ind):
        v = st.value
        if not isinstance(v, ast.IfExp):
            abort(st, "pay shape")
        self.flush(ind)
        self.w(ind, "pay = raw + 12;")
        self.w(ind, "paylen = rawlen > 16 ? rawlen - 16 : rawlen - 12;")

    def do_assign(self, st, ind):
        tg = st.targets[0]
        if isinstance(tg, ast.Tuple):
            for t, v in zip(tg.elts, st.value.elts):
                self.assign_one(st, t.id, v, ind)
            return
        self.assign_one(st, tg.id, st.value, ind)

    def assign_one(self, st, nm, v, ind):
        tag, ex = self.vtype(st, nm)
        if tag == "B":
            return  # pay+off alias; bounds asserted at infer
        if tag == "S":
            # via temp: RHS may read the target (exp = exp[:8]+...)
            t = self.newtemp()
            self.M(v, t)
            self.flush(ind)
            self.w(ind, "strcpy(%s, %s);" % (nm, t))
            return
        if tag == "FH":
            # fromhex bytes held as hex string; indexed via hexval
            if not (isinstance(v, ast.Call) and
                    isinstance(v.func, ast.Attribute) and
                    v.func.attr == "fromhex"):
                abort(st, "FH assign shape")
            t = self.newtemp()
            self.M(v.args[0], t)
            self.flush(ind)
            self.w(ind, "strcpy(%s, %s);" % (nm, t))
            return
        if tag == "P":
            if isinstance(v, ast.IfExp):
                tst = self.E(v.test)
                self.flush(ind)
                self.w(ind, "if (%s) {" % tst)
                self.assign_one(st, nm, v.body, ind + 1)
                self.w(ind, "} else {")
                self.assign_one(st, nm, v.orelse, ind + 1)
                self.w(ind, "}")
                return
            if isinstance(v, ast.Name) and v.id in self.tabs and \
                    self.tabs[v.id].kind == "PAIRS" and \
                    self.tabs[v.id].width == ex:
                self.flush(ind)
                self.tabN.add(v.id)
                self.w(ind, "%s = %s; %s_n = %s_N;" % (nm, v.id, nm,
                                                       v.id))
                return
            if isinstance(v, ast.Tuple) and ex == 2:
                # static: use may outlive the assigning block
                for x in v.elts:
                    if not (isinstance(x, ast.Tuple) and
                            len(x.elts) == 2 and all(
                                isinstance(y, ast.Constant) for y
                                in x.elts)):
                        abort(st, "P literal non-const")
                self.loopn += 1
                k = self.loopn
                rows = ", ".join(
                    "{%s,%s}" % (self.E(x.elts[0]),
                                 self.E(x.elts[1])) for x in v.elts)
                self.flush(ind)
                self.w(ind, "static const long _c%d[][2] = {%s};" % (
                    k, rows))
                self.w(ind, "%s = _c%d; %s_n = %d;" % (nm, k, nm,
                                                       len(v.elts)))
                return
            abort(st, "P assign shape")
        if tag == "ROW":
            lines = []
            self.assign_row(st, nm, v, ex, lines)
            self.flush(ind)
            for ln in lines:
                self.w(ind, ln)
            return
        if tag == "LD":
            if not isinstance(v, ast.Dict):
                abort(st, "LD assign shape")
            self.loopn += 1
            keys = ", ".join(repr(k.value) for k in v.keys)
            vals = ", ".join(x.id for x in v.values)
            self.flush(ind)
            self.w(ind, "static const long %s_KEYS[] = {%s};" % (
                nm, keys))
            self.w(ind, "static const char *%s_VALS[] = {%s};" % (
                nm, vals))
            self.w(ind, "enum { %s_N = %d };" % (nm, len(v.keys)))
            return
        if tag == "N1":
            if isinstance(v, ast.Constant) and v.value is None:
                self.flush(ind)
                self.w(ind, "%s_none = 1;" % nm)
            else:
                code = self.E(v)
                self.flush(ind)
                self.w(ind, "%s = (%s); %s_none = 0;" % (nm, code, nm))
            return
        code = self.E(v)
        self.flush(ind)
        self.w(ind, "%s = (%s);" % (nm, code))

    def assign_row(self, st, nm, v, w, lines, ind=0):
        pre = "    " * ind
        if isinstance(v, ast.Tuple):
            if len(v.elts) != w:
                abort(st, "row literal width")
            for i, x in enumerate(v.elts):
                lines.append("%s%s[%d] = (%s);" % (pre, nm, i,
                                                   self.E(x)))
            return
        if isinstance(v, ast.IfExp):
            tst = self.E(v.test)
            lines.append("%sif (%s) {" % (pre, tst))
            self.assign_row(st, nm, v.body, w, lines, ind + 1)
            lines.append("%s} else {" % pre)
            self.assign_row(st, nm, v.orelse, w, lines, ind + 1)
            lines.append("%s}" % pre)
            return
        if isinstance(v, ast.Name) and v.id in self.vt and \
                self.vt[v.id] == ("ROW", w):
            for i in range(w):
                lines.append("%s%s[%d] = %s[%d];" % (pre, nm, i,
                                                     v.id, i))
            return
        if isinstance(v, ast.Subscript) and isinstance(v.value,
                                                      ast.Name) and \
                v.value.id in self.tabs and \
                self.tabs[v.value.id].kind == "PAIRS" and \
                self.tabs[v.value.id].width == w and \
                not isinstance(v.slice, ast.Slice):
            idx = self.E(v.slice)
            for i in range(w):
                lines.append("%s%s[%d] = %s[%s][%d];" % (
                    pre, nm, i, v.value.id, idx, i))
            return
        abort(st, "row assign shape")

    def do_if(self, st, ind):
        tst = self.E(st.test)
        self.flush(ind)
        self.w(ind, "if (%s) {" % tst)
        for s in st.body:
            self.stmt(s, ind + 1)
        if st.orelse:
            # elif emits as nested if in else (pending-correct:
            # test materialization must run only when outer test
            # is false, which flat `else if` cannot express when
            # the test needs temp setup).
            self.w(ind, "} else {")
            for s in st.orelse:
                self.stmt(s, ind + 1)
            self.w(ind, "}")
        else:
            self.w(ind, "}")

    def do_for(self, st, ind):
        tg, it = st.target, st.iter
        self.loopn += 1
        k = self.loopn
        if isinstance(tg, ast.Name) and isinstance(it, ast.Tuple):
            es = ", ".join("(long)(%s)" % self.E(x)
                           for x in it.elts)
            self.flush(ind)
            self.w(ind, "{ const long _a%d[] = {%s};" % (k, es))
            self.w(ind + 1, "for (long _i%d = 0; _i%d < %d; _i%d++) {" % (
                k, k, len(it.elts), k))
            self.w(ind + 2, "%s = _a%d[_i%d];" % (tg.id, k, k))
            for s in st.body:
                self.stmt(s, ind + 2)
            self.w(ind + 1, "}")
            self.w(ind, "}")
            return
        if isinstance(tg, ast.Tuple) and len(tg.elts) == 2 and \
                all(isinstance(x, ast.Name) for x in tg.elts):
            b, vv = tg.elts[0].id, tg.elts[1].id
            if isinstance(it, ast.Tuple):
                if not all(isinstance(x, ast.Tuple) and
                           len(x.elts) == 2 for x in it.elts):
                    abort(st, "for pair-literal shape")
                rows = ", ".join(
                    "{%s,%s}" % (self.E(x.elts[0]),
                                 self.E(x.elts[1])) for x in it.elts)
                self.flush(ind)
                self.w(ind, "{ const long _a%d[][2] = {%s};" % (
                    k, rows))
                self.w(ind + 1, "for (long _i%d = 0; _i%d < %d; "
                       "_i%d++) {" % (k, k, len(it.elts), k))
                self.w(ind + 2, "%s = _a%d[_i%d][0]; %s = "
                       "_a%d[_i%d][1];" % (b, k, k, vv, k, k))
                for s in st.body:
                    self.stmt(s, ind + 2)
                self.w(ind + 1, "}")
                self.w(ind, "}")
                return
            if isinstance(it, ast.Name):
                if it.id in self.tabs and \
                        self.tabs[it.id].kind == "PAIRS" and \
                        self.tabs[it.id].width == 2:
                    self.tabN.add(it.id)
                    arr, cnt = it.id, it.id + "_N"
                elif it.id in self.vt and self.vt[it.id] == ("P", 2):
                    arr, cnt = it.id, it.id + "_n"
                else:
                    abort(st, "for-iter pair source")
                self.flush(ind)
                self.w(ind, "for (long _i%d = 0; _i%d < %s; "
                       "_i%d++) {" % (k, k, cnt, k))
                self.w(ind + 1, "%s = %s[_i%d][0]; %s = %s[_i%d][1];" % (
                    b, arr, k, vv, arr, k))
                for s in st.body:
                    self.stmt(s, ind + 1)
                self.w(ind, "}")
                return
        abort(st, "for shape")

    def fmt_args(self, st, fmt, args):
        """Map python % fmt to C printf fmt + arg exprs."""
        import re
        specs = re.findall(r"%[#0\- +]*(?:\d+)?[diuxXoscp]", fmt)
        if len(specs) != len(args):
            abort(st, "fmt/args count")
        out = []
        for sp, a in zip(specs, args):
            if sp.endswith("s"):
                out.append(self.str_ptr(st, a))
            elif sp[-1] in "diuxX":
                if self.kind(a) != "L":
                    abort(st, "numeric fmt of non-L")
                out.append("(long)(%s)" % self.E(a))
            else:
                abort(st, "fmt spec " + sp)
        cfmt = fmt
        cfmt = re.sub(r"%([#0\- +]*\d*)x", r"%\1lx", cfmt)
        cfmt = re.sub(r"%([#0\- +]*\d*)d", r"%\1ld", cfmt)
        cfmt = re.sub(r"%([#0\- +]*\d*)i", r"%\1li", cfmt)
        cfmt = re.sub(r"%([#0\- +]*\d*)u", r"%\1lu", cfmt)
        if re.search(r"%(?![#0\- +]*\d*l[diux]|s)", cfmt):
            abort(st, "unmapped fmt left: " + cfmt)
        return cfmt, out

    def fail_call(self, st, e):
        if len(e.args) != 1 or e.keywords:
            abort(st, "fail arity")
        a = e.args[0]
        if isinstance(a, ast.Constant) and isinstance(a.value, str):
            return 'failf("%s")' % c_escape(a.value)
        if isinstance(a, ast.BinOp) and isinstance(a.op, ast.Mod) and \
                isinstance(a.left, ast.Constant) and \
                isinstance(a.left.value, str):
            r = a.right
            args = r.elts if isinstance(r, ast.Tuple) else [r]
            cfmt, outs = self.fmt_args(st, a.left.value, args)
            return 'failf("%s", %s)' % (c_escape(cfmt),
                                        ", ".join(outs))
        abort(st, "fail arg shape")

    def do_return(self, st, ind):
        v = st.value
        if isinstance(v, ast.Constant) and isinstance(v.value, int):
            self.flush(ind)
            self.w(ind, "return %d;" % v.value)
            return
        if isinstance(v, ast.Call) and isinstance(v.func, ast.Name) \
                and v.func.id == "fail":
            code = self.fail_call(st, v)
            self.flush(ind)
            self.w(ind, "return %s;" % code)
            return
        abort(st, "return shape")

    def do_print(self, st, ind):
        if not (isinstance(st.value, ast.Call) and
                isinstance(st.value.func, ast.Name) and
                st.value.func.id == "print"):
            abort(st, "expr stmt not print")
        e = st.value
        err = False
        for kw in e.keywords:
            if kw.arg == "file" and isinstance(kw.value, ast.Attribute) \
                    and kw.value.attr == "stderr":
                err = True
            else:
                abort(st, "print kw")
        if len(e.args) != 1:
            abort(st, "print arity")
        a = e.args[0]
        if isinstance(a, ast.Constant) and isinstance(a.value, str):
            self.flush(ind)
            if err:
                self.w(ind, 'fprintf(stderr, "%s\\n");' %
                       c_escape(a.value))
            else:
                self.w(ind, 'printf("%s\\n");' % c_escape(a.value))
            return
        if isinstance(a, ast.BinOp) and isinstance(a.op, ast.Mod) and \
                isinstance(a.left, ast.Constant) and \
                isinstance(a.left.value, str):
            r = a.right
            args = r.elts if isinstance(r, ast.Tuple) else [r]
            cfmt, outs = self.fmt_args(st, a.left.value, args)
            self.flush(ind)
            if err:
                self.w(ind, 'fprintf(stderr, "%s\\n", %s);' % (
                    c_escape(cfmt), ", ".join(outs)))
            else:
                self.w(ind, 'printf("%s\\n", %s);' % (
                    c_escape(cfmt), ", ".join(outs)))
            return
        abort(st, "print arg shape")


# ---------------- table emission ----------------
def emit_tables(tabs, used, tabN):
    out = []
    for nm in tabs:
        if nm not in used:
            continue
        t = tabs[nm]
        if t.kind == "INT":
            out.append("static const long %s[] = {%s};" % (
                nm, ", ".join(repr(v) for v in t.val)))
        elif t.kind == "STR":
            out.append('static const char %s[] = "%s";' % (
                nm, c_escape(t.val)))
        elif t.kind == "STRS":
            out.append("static const char *%s[] = {" % nm)
            for s in t.val:
                out.append('    "%s",' % c_escape(s))
            out.append("};")
        elif t.kind == "PAIRS":
            w = t.width
            out.append("enum { PAIRW_%s = %d };" % (nm, w))
            out.append("static const long %s[][PAIRW_%s] = {" % (
                nm, nm))
            for row in t.val:
                out.append("    {%s}," % ", ".join(repr(v)
                                                   for v in row))
            out.append("};")
            if nm in tabN:
                out.append("static const long %s_N = %d;" % (
                    nm, len(t.val)))
        elif t.kind == "DICT":
            out.append("static const long %s_KEYS[] = {%s};" % (
                nm, ", ".join(repr(k) for k, _ in t.val)))
            out.append("static const char *%s_VALS[] = {" % nm)
            for _, s in t.val:
                out.append('    "%s",' % c_escape(s))
            out.append("};")
            out.append("static const long %s_N = %d;" % (
                nm, len(t.val)))
    return out


HELPERS = {
    "failf": (
        "static int failf(const char *fmt, ...) {\n"
        "    va_list ap;\n"
        "    printf(\"GRAMMAR-BREAK \");\n"
        "    va_start(ap, fmt);\n"
        "    vprintf(fmt, ap);\n"
        "    va_end(ap);\n"
        "    putchar('\\n');\n"
        "    return 1;\n"
        "}\n"),
    "zero": "static const uint8_t ZERO76[76] = {0};\n",
    "bit": (
        "static long bit_at(const uint8_t *pay, long paylen, long i) {\n"
        "    if (i < 0 || (i >> 3) >= paylen) {\n"
        "        printf(\"GRAMMAR-BREAK bit-range\\n\");\n"
        "        exit(1);\n"
        "    }\n"
        "    return (long)((pay[i >> 3] >> (i & 7)) & 1);\n"
        "}\n"),
    "grp_list": (
        "static long grp_list(const uint8_t *pay, long paylen,\n"
        "                     const long *idx, long k) {\n"
        "    long v = 0;\n"
        "    for (long j = 0; j < k; j++)\n"
        "        v |= bit_at(pay, paylen, idx[j]) << j;\n"
        "    return v;\n"
        "}\n"),
    "grp_range": (
        "static long grp_range(const uint8_t *pay, long paylen, long a,\n"
        "                      long b) {\n"
        "    long v = 0;\n"
        "    for (long i = a; i < b; i++)\n"
        "        v |= bit_at(pay, paylen, i) << (i - a);\n"
        "    return v;\n"
        "}\n"),
    "hex_of": (
        "static void hex_of(const uint8_t *p, long n, char *out) {\n"
        "    static const char H[] = \"0123456789abcdef\";\n"
        "    for (long i = 0; i < n; i++) {\n"
        "        out[2 * i] = H[p[i] >> 4];\n"
        "        out[2 * i + 1] = H[p[i] & 15];\n"
        "    }\n"
        "    out[2 * n] = 0;\n"
        "}\n"),
    "hexval": (
        "static long hexval(const char *p, long n) {\n"
        "    long v = 0;\n"
        "    for (long i = 0; i < n; i++) {\n"
        "        char c = p[i];\n"
        "        v = v * 16 + (c >= '0' && c <= '9' ? c - '0' :\n"
        "                      c >= 'a' && c <= 'f' ? c - 'a' + 10 :\n"
        "                      c >= 'A' && c <= 'F' ? c - 'A' + 10 : 0);\n"
        "    }\n"
        "    return v;\n"
        "}\n"),
    "lmin": "static long lmin(long a, long b) { return a < b ? a : b; }\n",
    "dictstr": (
        "static const char *dictstr(const long *keys,\n"
        "                           const char **vals, long n,\n"
        "                           long key) {\n"
        "    for (long i = 0; i < n; i++)\n"
        "        if (keys[i] == key)\n"
        "            return vals[i];\n"
        "    printf(\"GRAMMAR-BREAK dict-miss\\n\");\n"
        "    exit(1);\n"
        "    return 0;\n"
        "}\n"),
    "dict_has": (
        "static long dict_has(const long *keys, long n, long key) {\n"
        "    for (long i = 0; i < n; i++)\n"
        "        if (keys[i] == key)\n"
        "            return 1;\n"
        "    return 0;\n"
        "}\n"),
}

CHEAD = """/* rgramc -- lzraven zeros-N payload grammar verifier.
 * C port of ../rgram.py (own-code port; generated by NVME scratch
 * tool rgram_gen.py, verified py-identical on sealed pins).
 * Usage: rgramc FILE.rav N. Exit 0 + CLOSED / 1 + GRAMMAR-BREAK / 2.
 */
#include "rgramc.h"
#include <stdarg.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

"""

HFILE = """/* rgramc -- C port of ../rgram.py (lzraven zeros-N grammar verifier).
 * Verdict core (file/arg handling lives in rgramc.c main). */
#ifndef AAE_RGRAMC_H
#define AAE_RGRAMC_H
#include <stddef.h>
#include <stdint.h>

/* verify raw[0..rawlen) as lzraven zeros-N encoding. Prints CLOSED or
 * GRAMMAR-BREAK to stdout (usage/scope errors to stderr). Returns
 * 0 pass / 1 rule break / 2 bad input. Mirrors rgram.main(). */
int rgram_verify(const uint8_t *raw, long rawlen, long n);
#endif
"""

CMAIN = """
int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "usage: rgram.py FILE.rav N\\n");
        return 2;
    }
    const char *path = argv[1];
    long n = atol(argv[2]);
    FILE *f = fopen(path, "rb");
    if (!f) {
        fprintf(stderr, "rgramc: cannot open %s\\n", path);
        return 1;
    }
    fseek(f, 0, SEEK_END);
    long rawlen = ftell(f);
    fseek(f, 0, SEEK_SET);
    uint8_t *raw = malloc(rawlen > 0 ? (size_t)rawlen : 1);
    if (!raw) {
        fclose(f);
        return 1;
    }
    if (rawlen > 0 && fread(raw, 1, (size_t)rawlen, f) !=
        (size_t)rawlen) {
        fclose(f);
        free(raw);
        return 1;
    }
    fclose(f);
    int rc = rgram_verify(raw, rawlen, n);
    free(raw);
    return rc;
}
"""


def collect_used(body, tabs):
    from collections import Counter
    total = Counter()
    precomp = Counter()  # bytes.fromhex args (consumed at gen time)
    for nd in ast.walk(ast.Module(body=body, type_ignores=[])):
        if isinstance(nd, ast.Name) and nd.id in tabs:
            total[nd.id] += 1
        if isinstance(nd, ast.Call) and isinstance(nd.func,
                                                   ast.Attribute) \
                and nd.func.attr == "fromhex" and nd.args and \
                isinstance(nd.args[0], ast.Name):
            precomp[nd.args[0].id] += 1
    return set(n for n in total if total[n] > precomp[n])


def tier_comment(srclines, st):
    ln = getattr(st, "lineno", 0)
    if 1 <= ln <= len(srclines) and "#" in srclines[ln - 1]:
        c = srclines[ln - 1].split("#", 1)[1].strip()
        return "/* T%d: %s */" % (ln, c.replace("*/", "* /"))
    return None


def main(argv):
    src = outc = None
    upto = None
    outh = None
    i = 0
    while i < len(argv):
        if argv[i] == "--upto":
            upto = int(argv[i + 1])
            i += 2
        elif argv[i] == "--header":
            outh = argv[i + 1]
            i += 2
        elif src is None:
            src = argv[i]
            i += 1
        elif outc is None:
            outc = argv[i]
            i += 1
        else:
            raise SystemExit("usage: rgram_gen.py RGRAM.PY OUT.C "
                             "[--upto N] [--header OUT.H]")
    if src is None or outc is None:
        raise SystemExit("usage: rgram_gen.py RGRAM.PY OUT.C "
                         "[--upto N] [--header OUT.H]")
    text = open(src).read()
    srclines = text.splitlines()
    mod = ast.parse(text)
    tabs = collect_tables(mod)
    mains = [n for n in mod.body if isinstance(n, ast.FunctionDef) and
             n.name == "main"]
    if len(mains) != 1:
        raise SystemExit("want exactly one main()")
    body = filter_range(mains[0].body, upto)
    vsn = Versioner(tabs)
    nbumps = vsn.run(body)
    inf = Infer(tabs)
    for st in body:
        inf.stmt(st)
    used = collect_used(body, tabs)
    em = Emit(tabs, inf.vt, srclines)
    prologue = set()
    for st in body:
        c = tier_comment(srclines, st)
        if c is not None and isinstance(st, ast.If):
            em.out.append("    " + c)
        r = em.stmt(st, 1, top=True)
        if r is not None:
            prologue.add(r)
        if isinstance(st, ast.If):
            em.out.append("")
    if upto is not None:
        em.w(1, 'fprintf(stderr, "N out of scope\\n");')
        em.w(1, "return 2;")
    if prologue != {"argv", "raw", "ninit"}:
        raise SystemExit("prologue incomplete: %s" % prologue)
    if em.pending:
        raise SystemExit("pending lines left over")
    need = set(em.need)
    if "grp_list" in need or "grp_range" in need:
        need.add("bit")
    chunks = [CHEAD]
    chunks.append(HELPERS["failf"])
    for k in ("zero", "bit", "grp_list", "grp_range", "hex_of",
              "hexval", "lmin", "dictstr", "dict_has"):
        if k in need:
            chunks.append(HELPERS[k])
    chunks.append("\n".join(emit_tables(tabs, used, em.tabN)))
    chunks.append("")
    chunks.append("int rgram_verify(const uint8_t *raw, long rawlen, "
                  "long n) {")
    chunks.append("    const uint8_t *pay = 0;")
    chunks.append("    long paylen = 0;")
    for nm, (tag, ex) in inf.vt.items():
        if tag == "P" and ex != 2:
            raise SystemExit("P var width != 2: %s" % nm)
    if any(tag == "P" for tag, _ in inf.vt.values()):
        chunks.append("    enum { PAIRW_P2 = 2 };")
    for nm, (tag, ex) in inf.vt.items():
        if tag == "L":
            chunks.append("    long %s = 0;" % nm)
        elif tag == "S":
            chunks.append("    char %s[512] = {0};" % nm)
        elif tag == "FH":
            chunks.append("    char %s[512] = {0};" % nm)
        elif tag == "B":
            off, ln = ex
            chunks.append("    /* bytes %s = pay[%d:%d] */" % (
                nm, off, ln))
        elif tag == "P":
            chunks.append("    const long (*%s)[PAIRW_%s] = 0;" % (
                nm, "P%d" % ex))
            chunks.append("    long %s_n = 0;" % nm)
        elif tag == "ROW":
            chunks.append("    long %s[%d] = {0};" % (nm, ex))
        elif tag == "N1":
            chunks.append("    long %s = 0; int %s_none = 1;" % (
                nm, nm))
        elif tag == "LD":
            chunks.append("    /* local dict %s (statics at site) */" % nm)
    for k in range(1, em.tempn + 1):
        chunks.append("    char _t%d[512];" % k)
    chunks.append("\n".join(em.out))
    chunks.append("}")
    chunks.append(CMAIN)
    open(outc, "w").write("\n".join(chunks))
    if outh is not None:
        open(outh, "w").write(HFILE)
    print("rgram_gen: tables=%d/%d temps=%d loops=%d bumps=%d "
          "upto=%s -> %s" % (len(used), len(tabs), em.tempn, em.loopn,
                              nbumps, upto, outc))


if __name__ == "__main__":
    main(sys.argv[1:])

