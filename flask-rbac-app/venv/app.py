import base64
import secrets
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "artifacts"
MESSAGE = "Security assignment demo message."


def run_command(args):
    subprocess.run(args, check=True, cwd=OUTPUT_DIR, capture_output=True, text=True)


def write_text_file(path, value):
    path.write_text(value, encoding="utf-8")


def read_text_file(path):
    return path.read_text(encoding="utf-8").strip()


def generate_symmetric_demo(message_file):
    symmetric_key = secrets.token_bytes(32)
    iv = secrets.token_bytes(16)
    key_hex = symmetric_key.hex()
    iv_hex = iv.hex()
    cipher_file = OUTPUT_DIR / "symmetric_cipher.bin"

    run_command(
        [
            "openssl",
            "enc",
            "-aes-256-cbc",
            "-K",
            key_hex,
            "-iv",
            iv_hex,
            "-in",
            str(message_file),
            "-out",
            str(cipher_file),
        ]
    )

    run_command(
        [
            "openssl",
            "enc",
            "-d",
            "-aes-256-cbc",
            "-K",
            key_hex,
            "-iv",
            iv_hex,
            "-in",
            str(cipher_file),
            "-out",
            str(OUTPUT_DIR / "symmetric_decrypted.txt"),
        ]
    )

    return {
        "algorithm": "AES-256-CBC",
        "key_hex": key_hex,
        "iv_hex": iv_hex,
        "ciphertext_base64": base64.b64encode(cipher_file.read_bytes()).decode("utf-8"),
        "decrypted_text": read_text_file(OUTPUT_DIR / "symmetric_decrypted.txt"),
    }


def generate_asymmetric_demo(message_file):
    private_key_file = OUTPUT_DIR / "private_key.pem"
    public_key_file = OUTPUT_DIR / "public_key.pem"
    cipher_file = OUTPUT_DIR / "asymmetric_cipher.bin"
    decrypted_file = OUTPUT_DIR / "asymmetric_decrypted.txt"

    run_command(
        [
            "openssl",
            "genpkey",
            "-algorithm",
            "RSA",
            "-pkeyopt",
            "rsa_keygen_bits:2048",
            "-out",
            str(private_key_file),
        ]
    )
    run_command(
        [
            "openssl",
            "rsa",
            "-pubout",
            "-in",
            str(private_key_file),
            "-out",
            str(public_key_file),
        ]
    )
    run_command(
        [
            "openssl",
            "pkeyutl",
            "-encrypt",
            "-pubin",
            "-inkey",
            str(public_key_file),
            "-in",
            str(message_file),
            "-out",
            str(cipher_file),
        ]
    )
    run_command(
        [
            "openssl",
            "pkeyutl",
            "-decrypt",
            "-inkey",
            str(private_key_file),
            "-in",
            str(cipher_file),
            "-out",
            str(decrypted_file),
        ]
    )

    return {
        "algorithm": "RSA-2048",
        "private_key_pem": read_text_file(private_key_file),
        "public_key_pem": read_text_file(public_key_file),
        "ciphertext_base64": base64.b64encode(cipher_file.read_bytes()).decode("utf-8"),
        "decrypted_text": read_text_file(decrypted_file),
    }


def build_report(message, symmetric_data, asymmetric_data):
    report = [
        "Encryption / Decryption Assignment Output",
        "=" * 40,
        "",
        "Input Message",
        f"- Plaintext: {message}",
        "",
        "Symmetric Encryption",
        f"- Algorithm: {symmetric_data['algorithm']}",
        f"- Key (hex): {symmetric_data['key_hex']}",
        f"- IV (hex): {symmetric_data['iv_hex']}",
        f"- Ciphertext (base64): {symmetric_data['ciphertext_base64']}",
        f"- Decrypted text: {symmetric_data['decrypted_text']}",
        "",
        "Asymmetric Encryption",
        f"- Algorithm: {asymmetric_data['algorithm']}",
        "- Private key (PEM):",
        asymmetric_data["private_key_pem"],
        "",
        "- Public key (PEM):",
        asymmetric_data["public_key_pem"],
        "",
        f"- Ciphertext (base64): {asymmetric_data['ciphertext_base64']}",
        f"- Decrypted text: {asymmetric_data['decrypted_text']}",
        "",
    ]
    return "\n".join(report)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    message_file = OUTPUT_DIR / "message.txt"
    write_text_file(message_file, MESSAGE)

    symmetric_data = generate_symmetric_demo(message_file)
    asymmetric_data = generate_asymmetric_demo(message_file)

    report = build_report(MESSAGE, symmetric_data, asymmetric_data)
    report_file = OUTPUT_DIR / "encryption_results.txt"
    write_text_file(report_file, report)

    print(report)
    print(f"Saved report to: {report_file}")


if __name__ == "__main__":
    main()
