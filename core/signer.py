"""
signer.py
Sign and verify bitstream files using RSA-PSS and SHA256.
"""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import os

def sign_file(bitstream_path, private_key_path="data/private.pem", sig_out=None):
    if sig_out is None:
        sig_out = bitstream_path + ".sig"
    if not os.path.exists(bitstream_path):
        raise FileNotFoundError(f"Bitstream not found: {bitstream_path}")
    with open(private_key_path, "rb") as f:
        key = serialization.load_pem_private_key(f.read(), password=None)
    data = open(bitstream_path, "rb").read()
    signature = key.sign(
        data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    with open(sig_out, "wb") as f:
        f.write(signature)
    return sig_out

def verify_signature(public_key_path, bitstream_path, sig_path):
    if not (os.path.exists(public_key_path) and os.path.exists(bitstream_path) and os.path.exists(sig_path)):
        return False, "Missing public key / bitstream / signature file."
    with open(public_key_path, "rb") as f:
        pub = serialization.load_pem_public_key(f.read())
    data = open(bitstream_path, "rb").read()
    signature = open(sig_path, "rb").read()
    try:
        pub.verify(
            signature,
            data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True, "Signature valid."
    except Exception as e:
        return False, f"Signature verification failed: {e}"
