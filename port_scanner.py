import argparse
import socket
from typing import List


def parse_ports(ports: str) -> List[int]:
    if "," in ports:
        return [int(p.strip()) for p in ports.split(",")]

    if "-" in ports:
        start, end = ports.split("-")
        return list(range(int(start), int(end) + 1))

    return [int(ports)]


def scan_port(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0


def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner (Educational)")
    parser.add_argument("--host", required=True, help="Target host")
    parser.add_argument("--ports", default="20-1024", help="Port range or list")
    args = parser.parse_args()

    ports = parse_ports(args.ports)
    print(f"Scanning {args.host}...")

    for port in ports:
        if scan_port(args.host, port):
            print(f"[OPEN] {port}")


if __name__ == "__main__":
    main()
