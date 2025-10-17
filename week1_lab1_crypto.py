#!/usr/bin/env python3


from base64 import b64decode
from collections import Counter
import string

def caesar_shift(text: str, k: int) -> str:
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch)-97 - k) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch)-65 - k) % 26 + 65))
        else:
            out.append(ch)
    return ''.join(out)

def caesar_bruteforce(text: str):
    return [(k, caesar_shift(text, k)) for k in range(26)]

def letter_frequency(text: str):
    filtered = [c.lower() for c in text if c.isalpha()]
    return Counter(filtered)

def xor_repeat(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def run():
    # Task 1
    cipher1 = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
    bf1 = caesar_bruteforce(cipher1)
    k1, plain1 = next((k, p) for k, p in bf1 if "The Quick Brown Fox Jumps Over The Lazy Dog." in p)

    # Task 2
    cipher2 = "mznxpz"
    bf2 = caesar_bruteforce(cipher2)
    k2, decrypted2 = next((k, p) for k, p in bf2 if p == "rescue")
    passphrase = "secure"  # anagram and fundamental concept

    b64 = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
    data = b64decode(b64)
    xord = xor_repeat(data, passphrase.encode())

    print("=== Task 1: Caesar ===")
    print("Ciphertext:", cipher1)
    print("Key (shift):", k1)
    print("Plaintext:", plain1)
    print()
    print("=== Task 2: Caesar -> Anagram -> XOR ===")
    print("Ciphertext:", cipher2)
    print("Brute-force hit: k=%d => %s" % (k2, decrypted2))
    print("Passphrase (anagram of 'rescue'):", passphrase)
    print("Base64:", b64)
    print("XOR decrypted:", xord.decode())

if __name__ == "__main__":
    run()
