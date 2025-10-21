# modules/signer.py
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

def generate_keys(private_key_path="data/private.pem", public_key_path="data/public.pem"):
    """Generate RSA key pair for signing and verification."""
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    with open(private_key_path, "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    with open(public_key_path, "wb") as f:
        f.write(key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    return private_key_path, public_key_path


def sign_bitstream(bit_path, private_key_path):
    """Digitally sign the bitstream file."""
    key = serialization.load_pem_private_key(open(private_key_path, "rb").read(), password=None)
    data = open(bit_path, "rb").read()
    signature = key.sign(
        data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32),
        hashes.SHA256()
    )
    sig_path = bit_path + ".sig"
    open(sig_path, "wb").write(signature)
    return sig_path
