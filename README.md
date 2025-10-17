# week1-lab1-cryptography
Solutions for Week 1 / Lab 1 – Cryptography Fundamentals

Task 1 — Caesar Cipher (2 pts)
The given ciphertext was:
“Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu.”
By applying a brute-force decryption with different shift values, I discovered that a shift of 14 correctly revealed the original message:
“The Quick Brown Fox Jumps Over The Lazy Dog.”

This shows how simple the Caesar cipher is to break.
It’s considered insecure because it has only 26 possible keys, making brute-force attacks trivial.
Additionally, since it uses a single substitution pattern, the frequency of letters remains the same, allowing attackers to use frequency analysis to decrypt it easily.
Today, this kind of cipher is used only for educational purposes, puzzles, or CTF challenges—not for real security.

Task 2 — XOR Encryption (3 pts)
Step 1 — Caesar Decryption
The next ciphertext was: “mznxpz”
Using brute-force again, I found that with a shift of 21, the decrypted text is “rescue.”

Step 2 — Solving the Anagram
The word “rescue” can be rearranged into “secure,” which makes sense as a passphrase, since “secure” is a key concept in cryptography.

Step 3 — XOR Decryption
The provided ciphertext was encoded in Base64: Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ=         
To reproduce these results, you can run my Python solution:   python3 week1_lab1_crypto.py

After decoding it from Base64 and performing XOR decryption with the repeating key “secure,” I obtained the final plaintext message:

“This is the XOR challenge!”
