# symmetric-encryption-demo

![PyPI Version](https://img.shields.io/badge/PyPI-not_published-lightgrey)
![Tests](https://img.shields.io/badge/tests-not_configured-lightgrey)
![Docs](https://img.shields.io/badge/docs-not_configured-lightgrey)
![Coverage](https://img.shields.io/badge/coverage-not_measured-lightgrey)

## Description

This project is a small Python demo that encrypts and decrypts a short message using symmetric encryption. Its purpose is to show, in plain language, how one shared secret key can both protect and recover data. It also produces assignment-ready output that lists the key used, the input message, and the encryption and decryption results. This project fits best as a beginner-friendly security exercise rather than a production package.

## Features

- Encrypts a short plaintext message with `AES-256-CBC`
- Decrypts the ciphertext back to the original message
- Generates a random symmetric key and IV for each run
- Saves the input, key details, ciphertext, and decrypted output to a text file
- Produces simple artifacts that are easy to review or submit for class

## Quick Start

```bash
python3 app.py
```

```python
import subprocess

subprocess.run(["python3", "app.py"], check=True)
```

After running the script, review:

- `artifacts/encryption_results.txt`
- `artifacts/message.txt`
- `artifacts/symmetric_cipher.bin`
- `artifacts/symmetric_decrypted.txt`

## Notes

- This project is for learning and demonstration purposes.
- The badges are placeholders because PyPI publishing, CI, docs, and coverage are not set up for this assignment.
- In real applications, encryption keys should not normally be printed or stored in plain text.
