import argparse
import hashlib


def generate_hash(text: str, algorithm: str) -> str:
    algorithm = algorithm.lower()
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    h = hashlib.new(algorithm)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Hash Generator (MD5 / SHA)")
    parser.add_argument("--text", required=True, help="Text to hash")
    parser.add_argument(
        "--algo",
        default="sha256",
        help="Algorithm (md5, sha1, sha256, sha512)",
    )
    args = parser.parse_args()

    result = generate_hash(args.text, args.algo)
    print(f"Algorithm: {args.algo}")
    print(f"Hash: {result}")


if __name__ == "__main__":
    main()
