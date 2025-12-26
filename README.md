# Python Cyber Security Tools 🔐🐍

A collection of beginner-friendly cyber security utilities written in Python.

> ⚠️ Educational purposes only. Use responsibly and only on systems you own or have permission to test.

## Tools
- **Port Scanner** – Scan common TCP ports on a target host
- **Hash Generator** – Generate MD5 / SHA1 / SHA256 / SHA512 hashes
- **Password Strength Checker** – Check basic password strength

## Setup
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
## Usage

### Windows
> If `python` points to Python 2.x on Windows, use `py`.

```bash
py hash_generator.py --text "hello world" --algo sha256
py password_checker.py --password "P@ssw0rd123!"
py port_scanner.py --host 127.0.0.1 --ports 80,443


