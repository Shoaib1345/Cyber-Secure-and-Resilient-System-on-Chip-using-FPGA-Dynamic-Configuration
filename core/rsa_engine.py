"""
rsa_engine.py
Generate RSA keypair and explain the meaning/usages of keys.
"""
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys(private_path="data/private.pem", public_path="data/public.pem", bits=3072):
    os.makedirs(os.path.dirname(private_path) or ".", exist_ok=True)
    key = rsa.generate_private_key(public_exponent=65537, key_size=bits)
    priv = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    pub = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(private_path, "wb") as f:
        f.write(priv)
    with open(public_path, "wb") as f:
        f.write(pub)
    return private_path, public_path

def load_public_key_text(public_path):
    try:
        return open(public_path, "r").read()
    except Exception:
        return None

def explain_keygen(private_path="data/private.pem", public_path="data/public.pem"):
    """
    Return a human-friendly explanation about key generation and what each key is used for.
    """
    text = []
    text.append("=== RSA Key Generation Explanation ===")
    text.append("RSA is an asymmetric cryptographic algorithm using a key pair:")
    text.append("  • Private Key (kept secret): used to create digital signatures and decrypt (when used).")
    text.append("  • Public Key (shared): used to verify signatures and encrypt for the holder of the private key.")
    text.append("")
    text.append("Why we generate keys for this prototype:")
    text.append("  • Sign bitstream files using the private key so devices can ensure authenticity.")
    text.append("  • Embed or store the public key on the device (or a trusted location) to verify signatures.")
    text.append("")
    text.append("Where each key is used in the system:")
    text.append("  • Private Key -> Signing tool (manufacturer/secure server). NEVER stored on the FPGA or in untrusted storage.")
    text.append("  • Public Key  -> Stored on the device (FPGA SoC) to verify incoming bitstreams before applying them.")
    text.append("")
    text.append(f"Saved to: Private -> {private_path}; Public -> {public_path}")
    text.append("Security confirmation:")
    text.append("  • Keep the private key offline; rotate keys if compromised; use hardware-backed key storage on real devices.")
    return "\n".join(text)
