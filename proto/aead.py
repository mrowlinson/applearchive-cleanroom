#!/usr/bin/env python3
"""aead.py v1 -- AEA-decrypt PROTOTYPE (REFERENCE ONLY, not the deliverable).

Clean-room decode of Apple Encrypted Archives from behavior beds (APROBE-01)
+ allow-listed OSS craft (kinnay/AEA row A-006/5). Validates against the
oracle only. v1 scope: profiles 0-5, checksums none+sha256 (murmur Q-010
pending), segment codecs none+zlib+lzma+lz4, range-decrypt, id.
"""

import argparse
import hashlib
import hmac
import io
import lzma
import struct
import sys
import zlib

import lz4.block
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


class FmtErr(Exception):
    pass


SCRYPT_N = {0: 0x4000, 1: 0x10000, 2: 0x40000, 3: 0x100000}
KEY_SIZE = {0: 32, 1: 80, 2: 80, 3: 80, 4: 80, 5: 80}
SIG_SIZE = {0: 128, 1: 0, 2: 160, 3: 0, 4: 160, 5: 0}
PUB_SIZE = {0: 32, 1: 0, 2: 0, 3: 65, 4: 65, 5: 0}
CKSUM_SIZE = {0: 0, 1: 8, 2: 32}


def hkdf(size, ikm, info, salt=b""):
    return HKDF(hashes.SHA256(), size, salt, info).derive(ikm)


def mac(key32, data, salt):
    return hmac.digest(key32, salt + data + struct.pack("<Q", len(salt)), "sha256")


def dec_ver(key, data, salt, want):
    if mac(key[:32], data, salt) != want:
        raise FmtErr("HMAC mismatch")
    if len(key) == 80:
        d = Cipher(algorithms.AES(key[32:64]), modes.CTR(key[64:])).decryptor()
        return d.update(data) + d.finalize()
    return data


def scrypt_key(pw, salt, n):
    return Scrypt(salt, 32, n, 8, 1).derive(pw.encode())


def x962(pub):
    return pub.public_bytes(serialization.Encoding.X962,
                            serialization.PublicFormat.UncompressedPoint)


class KD:
    def __init__(self, main, ks):
        self.main, self.ks = main, ks

    def sigkey(self):
        return hkdf(self.ks, hkdf(32, self.main, b"AEA_SEK"), b"AEA_SEK2")

    def rootkey(self):
        return hkdf(self.ks, self.main, b"AEA_RHEK")

    def clustkey(self, i):
        return hkdf(32, self.main, b"AEA_CK" + struct.pack("<I", i))

    def chek(self, ck):
        return hkdf(self.ks, ck, b"AEA_CHEK")

    def segkey(self, ck, i):
        return hkdf(self.ks, ck, b"AEA_SK" + struct.pack("<I", i))


def load_priv(pem, name):
    try:
        k = serialization.load_pem_private_key(pem, None)
    except Exception:
        raise FmtErr("%s invalid" % name)
    if not isinstance(k, ec.EllipticCurvePrivateKey):
        raise FmtErr("%s invalid" % name)
    return k


def load_pub(pem, name):
    try:
        k = serialization.load_pem_public_key(pem)
    except Exception:
        raise FmtErr("%s invalid" % name)
    if not isinstance(k, ec.EllipticCurvePublicKey):
        raise FmtErr("%s invalid" % name)
    return k


def decomp(alg, data, size):
    if alg == "-":
        return data
    if alg == "z":
        try:
            return zlib.decompress(data)
        except zlib.error:
            raise FmtErr("zlib failed")
    if alg == "x":
        try:
            return lzma.decompress(data)
        except lzma.LZMAError:
            raise FmtErr("lzma failed")
    if alg == "4":
        try:
            return lz4.block.decompress(data, uncompressed_size=size)
        except Exception:
            raise FmtErr("lz4 failed")
    if alg == "e":
        import os
        import subprocess
        tool = os.environ.get("LZFSE_BIN", "")
        if not tool:
            raise FmtErr("lzfse needs LZFSE_BIN (own-built lzfse CLI)")
        try:
            p = subprocess.run([tool, "-decode"], input=data, capture_output=True)
        except OSError:
            raise FmtErr("lzfse tool failed")
        if p.returncode != 0 or len(p.stdout) != size:
            raise FmtErr("lzfse failed")
        return p.stdout
    if alg == "b":
        import os
        import subprocess
        tool = os.environ.get("ZBM_BIN", "")
        if not tool:
            raise FmtErr("lzbitmap needs ZBM_BIN (own-built zbmcat)")
        try:
            p = subprocess.run([tool], input=data, capture_output=True)
        except OSError:
            raise FmtErr("lzbitmap tool failed")
        if p.returncode != 0 or len(p.stdout) != size:
            raise FmtErr("lzbitmap failed")
        return p.stdout
    if alg == "m":
        import os
        import subprocess
        import tempfile
        tool = os.environ.get("LZR_BIN", "")
        if not tool:
            raise FmtErr("lzraven needs LZR_BIN (own-built lzraven_dec)")
        ip = op = None
        try:
            with tempfile.NamedTemporaryFile(delete=False) as fi:
                fi.write(data)
                ip = fi.name
            op = ip + ".out"
            p = subprocess.run([tool, ip, op], capture_output=True)
            out = None
            if p.returncode == 0:
                with open(op, "rb") as fo:
                    out = fo.read()
        except OSError:
            raise FmtErr("lzraven tool failed")
        finally:
            for q in (ip, op):
                if q is None:
                    continue
                try:
                    os.unlink(q)
                except OSError:
                    pass
        if out is None or len(out) != size:
            raise FmtErr("lzraven failed")
        return out
    raise FmtErr("codec %r unsupported in v1" % alg)


M64 = (1 << 64) - 1
MUR_SEED = 0xE2236FDC26A5F6D2


def murmur64a(data, seed=MUR_SEED):
    m, r = 0xC6A4A7935BD1E995, 47
    h = (seed ^ ((len(data) * m) & M64)) & M64
    nblk = len(data) & ~7
    for i in range(0, nblk, 8):
        (k,) = struct.unpack_from("<Q", data, i)
        k = (k * m) & M64
        k ^= k >> r
        k = (k * m) & M64
        h ^= k
        h = (h * m) & M64
    tail = len(data) - nblk
    if tail:
        t = 0
        for j in range(tail):
            t |= data[nblk + j] << (8 * j)
        h = (((h ^ t) & M64) * m) & M64
    h ^= h >> r
    h = (h * m) & M64
    h ^= h >> r
    return struct.pack("<Q", h)


def cksum(alg, data):
    if alg == 0:
        return b""
    if alg == 1:
        return murmur64a(data)
    if alg == 2:
        return hashlib.sha256(data).digest()
    raise FmtErr("checksum %d unsupported in v1" % alg)


def decrypt_aea(blob, symkey=None, recip_priv=None, password=None, sign_pub=None,
                range_off=None, range_size=None):
    f = io.BytesIO(blob)
    hdr = f.read(12)
    if len(hdr) < 12 or hdr[:4] != b"AEA1":
        raise FmtErr("bad magic")
    prof = hdr[4] | (hdr[5] << 8) | (hdr[6] << 16)
    sstr = hdr[7]
    if prof not in KEY_SIZE:
        raise FmtErr("bad profile")
    if prof == 5 and sstr not in SCRYPT_N:
        raise FmtErr("bad scrypt strength")
    (auth_sz,) = struct.unpack("<I", hdr[8:12])
    auth = f.read(auth_sz)
    if len(auth) < auth_sz:
        raise FmtErr("truncated prologue")
    sig_start = f.tell()
    sig = f.read(SIG_SIZE[prof])
    sig_end = f.tell()
    pub = f.read(PUB_SIZE[prof])
    salt = f.read(32)
    rmac = f.read(32)
    rdata = f.read(48)
    cmac = f.read(32)
    if len(cmac) < 32:
        raise FmtErr("truncated prologue")
    prologue_end = f.tell()

    sender = recip = spub = None
    if prof == 0:
        symkey = pub
    elif prof in (1, 2):
        if symkey is None or len(symkey) != 32:
            raise FmtErr("symmetric key required (32B)")
    elif prof in (3, 4):
        if recip_priv is None:
            raise FmtErr("recipient_priv required")
        rp = load_priv(recip_priv, "recipient_priv")
        recip = rp.public_key()
        sender = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), pub)
        symkey = rp.exchange(ec.ECDH(), sender)
    elif prof == 5:
        if password is None:
            raise FmtErr("password required")
        ext = hkdf(64, salt, b"AEA_SCRYPT")
        salt = ext[32:]
        symkey = scrypt_key(password, ext[:32], SCRYPT_N[sstr])

    if prof in (0, 2, 4):
        if sign_pub is None:
            raise FmtErr("sign_pub required")
        spub = load_pub(sign_pub, "sign_pub")

    info = b"AEA_AMK" + bytes([hdr[4], hdr[5], hdr[6], hdr[7]])
    for k in (sender, recip, spub):
        if k is not None:
            info += x962(k)
    kd = KD(hkdf(32, symkey, info, salt), KEY_SIZE[prof])

    if prof in (0, 2, 4):
        s = sig
        if prof != 0:
            s = dec_ver(kd.sigkey(), sig[:128], b"", sig[128:])
        der = s[:s[1] + 2]
        pro = blob[:sig_start] + bytes(sig_end - sig_start) + blob[sig_end:prologue_end]
        try:
            spub.verify(der, pro, ec.ECDSA(hashes.SHA256()))
        except InvalidSignature:
            raise FmtErr("signature invalid")

    rh = dec_ver(kd.rootkey(), rdata, cmac + auth, rmac)
    orig, arc, segsz, segper, comp, ckalg = struct.unpack("<QQIIcB", rh[:26])
    comp = comp.decode("ascii")
    if ckalg not in CKSUM_SIZE:
        raise FmtErr("bad checksum alg")
    if orig == 0:
        return b""
    shsz = 8 + CKSUM_SIZE[ckalg]

    out = io.BytesIO()
    ci = 0
    while True:
        ck = kd.clustkey(ci)
        chk = kd.chek(ck)
        sh = f.read(shsz * segper)
        nmac = f.read(32)
        smacs = f.read(32 * segper)
        if len(smacs) < 32 * segper:
            raise FmtErr("truncated cluster header")
        sh = dec_ver(chk, sh, nmac + smacs, cmac)
        for i in range(segper):
            h = sh[shsz * i:shsz * (i + 1)]
            osz, csz = struct.unpack("<II", h[:8])
            want_ck = h[8:]
            data = f.read(csz)
            if len(data) < csz:
                raise FmtErr("truncated segment")
            data = dec_ver(kd.segkey(ck, i), data, b"", smacs[32 * i:32 * (i + 1)])
            if osz > csz:
                data = decomp(comp, data, osz)
            if len(data) != osz:
                raise FmtErr("segment size wrong")
            if cksum(ckalg, data) != want_ck:
                raise FmtErr("checksum wrong")
            out.write(data)
            if out.tell() >= orig:
                full = out.getvalue()[:orig]
                if range_off is not None:
                    return full[range_off:range_off + (range_size or 0)]
                return full
        cmac = nmac
        ci += 1


def archive_id(blob):
    if len(blob) < 12 or blob[:4] != b"AEA1":
        raise FmtErr("bad magic")
    prof = blob[4] | (blob[5] << 8) | (blob[6] << 16)
    (auth_sz,) = struct.unpack("<I", blob[8:12])
    n = 12 + auth_sz + SIG_SIZE[prof] + PUB_SIZE[prof] + 32 + 32 + 48 + 32
    return hashlib.sha256(blob[:n]).digest()


def read_key_file(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    try:
        t = raw.decode("ascii")
    except UnicodeDecodeError:
        return raw
    c = t.rstrip("\r\n")
    if c.startswith("hex:"):
        return bytes.fromhex(c[4:])
    if c.startswith("base64:"):
        import base64
        return base64.b64decode(c[7:])
    return raw


def parse_key_value(val):
    import base64
    if val.startswith("hex:"):
        return bytes.fromhex(val[4:])
    if val.startswith("base64:"):
        return base64.b64decode(val[7:])
    raise FmtErr("key-value must be hex:... or base64:... (oracle rejects bare)")


def main(argv):
    ap = argparse.ArgumentParser(prog="aead.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("decrypt")
    d.add_argument("-i", required=True)
    d.add_argument("-o", required=True)
    d.add_argument("--key", default=None)
    d.add_argument("--key-value", default=None)
    d.add_argument("--password", default=None)
    d.add_argument("--password-file", default=None)
    d.add_argument("--recipient-priv", default=None)
    d.add_argument("--sign-pub", default=None)
    d.add_argument("--range-offset", type=int, default=None)
    d.add_argument("--range-size", type=int, default=None)
    g = sub.add_parser("id")
    g.add_argument("-i", required=True)
    a = ap.parse_args(argv)
    try:
        with open(a.i, "rb") as fh:
            blob = fh.read()
        if a.cmd == "id":
            sys.stdout.write(archive_id(blob).hex() + "\n")
            return 0
        symkey = recip = pw = spub = None
        if a.key:
            symkey = read_key_file(a.key)
        if a.key_value:
            symkey = parse_key_value(a.key_value)
        if a.password:
            pw = a.password
        if a.password_file:
            with open(a.password_file, "rb") as fh:
                praw = fh.read()
            try:
                pw = praw.decode().rstrip("\r\n")
            except UnicodeDecodeError:
                raise FmtErr("password file not text")
        if a.recipient_priv:
            with open(a.recipient_priv, "rb") as fh:
                recip = fh.read()
        if a.sign_pub:
            with open(a.sign_pub, "rb") as fh:
                spub = fh.read()
        out = decrypt_aea(blob, symkey, recip, pw, spub,
                           a.range_offset, a.range_size)
        with open(a.o, "wb") as fh:
            fh.write(out)
        return 0
    except FmtErr as e:
        sys.stderr.write("aead: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
