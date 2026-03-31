# Encryption and Decryption Project

## Overview

This project demonstrates how to encrypt and decrypt a short message using two different cryptography approaches:

- symmetric encryption
- asymmetric encryption

The program is written in Python and uses the local `openssl` command-line tool to perform the cryptographic operations.

The goal of the project is to show:

- the keys used
- the input message
- the encrypted output
- the decrypted output

All of that information is saved to a text file so it can be submitted for the assignment.

## What the Project Demonstrates

### Symmetric Encryption

Symmetric encryption uses one shared secret key for both encryption and decryption.

In this project, the symmetric example uses:

- `AES-256-CBC`

The script generates:

- a random 256-bit AES key
- a random initialization vector (IV)

It then:

1. encrypts the plaintext message
2. decrypts the ciphertext back into readable text

### Asymmetric Encryption

Asymmetric encryption uses two related keys:

- a public key
- a private key

In this project, the asymmetric example uses:

- `RSA-2048`

The script generates an RSA key pair, then:

1. encrypts the plaintext using the public key
2. decrypts the ciphertext using the private key

## How the Code Works

The Python script in `app.py` performs the following steps:

1. Creates a short message and writes it to `artifacts/message.txt`
2. Generates a random AES key and IV for symmetric encryption
3. Encrypts and decrypts the message with AES
4. Generates an RSA private/public key pair
5. Encrypts and decrypts the message with RSA
6. Saves all assignment results to `artifacts/encryption_results.txt`

## How to Run the Project

Open a terminal in the project folder and run:

```bash
python3 app.py
```

## Output Files

After running the program, these files are created in the `artifacts/` folder:

- `message.txt` : the original plaintext input
- `symmetric_cipher.bin` : the AES encrypted message
- `symmetric_decrypted.txt` : the AES decrypted message
- `private_key.pem` : the RSA private key
- `public_key.pem` : the RSA public key
- `asymmetric_cipher.bin` : the RSA encrypted message
- `asymmetric_decrypted.txt` : the RSA decrypted message
- `encryption_results.txt` : the full assignment summary showing keys, inputs, and outputs

## Main Files

- `app.py` : the Python program that runs the encryption and decryption demo
- `README.md` : explains the project
- `artifacts/encryption_results.txt` : contains the required assignment evidence

## Notes

- This project is for learning and demonstration purposes.
- In real applications, keys should be protected carefully and not normally printed or stored in plain text.
- Symmetric encryption is typically used for fast data encryption.
- Asymmetric encryption is typically used for key exchange, identity, and secure communication setup.
