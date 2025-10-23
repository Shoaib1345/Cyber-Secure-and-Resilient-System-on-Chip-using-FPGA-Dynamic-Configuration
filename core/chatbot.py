# modules/chatbot.py
import random

RESPONSES = {
    "rsa": [
        "RSA (Rivest–Shamir–Adleman) is an asymmetric encryption system. It uses a public key to encrypt data and a private key to decrypt it.",
        "RSA helps ensure authenticity and trust in FPGA bitstream signing."
    ],
    "key": [
        "Keys are the foundation of cryptography. A private key must be kept secret, while a public key can be shared for verification.",
        "In your FPGA system, keys secure and verify reconfiguration data."
    ],
    "sign": [
        "Digital signing ensures the bitstream hasn't been tampered with.",
        "A signature proves the bitstream came from a trusted manufacturer."
    ],
    "verify": [
        "Verification ensures the bitstream was signed by an authorized entity.",
        "It prevents loading malicious configurations into the FPGA."
    ],
    "fpga": [
        "FPGAs are reconfigurable chips. They can change their logic dynamically, but security ensures only authorized updates occur.",
        "Secure FPGA reconfiguration protects against hardware attacks."
    ],
    "reconfigure": [
        "Reconfiguration allows FPGAs to load new modules at runtime. The system ensures they are signed and authentic.",
        "Dynamic configuration is useful for updating logic securely without replacing hardware."
    ],
    "default": [
        "I’m your security assistant! Try asking about RSA, signing, or FPGA configuration.",
        "Could you please rephrase that? I explain key generation, signing, and verification topics."
    ]
}

def chatbot_reply(user_input: str) -> str:
    user_input = user_input.lower()
    for keyword, replies in RESPONSES.items():
        if keyword in user_input:
            return random.choice(replies)
    return random.choice(RESPONSES["default"])
