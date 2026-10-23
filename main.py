"""
OSINT Username Wordlist Generator
Kullanım: python3 usergen.py -u Turkiye [--output list.txt]
"""

import time
import argparse
import itertools
from pathlib import Path
import os

print("")

os.system("clear")
os.system("stty cols 83 rows 53")

with open("../Wordlister/.ascii/_Worm-Hole_.txt", "r") as Ascii:
        WormHole = Ascii.read()

print(f"\033[33m{WormHole}\033[31m")

print("\033[0m Copyright (c) EcipNether [EcipNetherDEV] 2026.")

print("")
print("\033[32mGenerating Wordlist...\033[31m")

time.sleep(1)

PREFIXES = ["", "mr", "the", "its", "im", "official", "real", "admin"]
SUFFIXES = ["", "123", "1234", "12345", "01", "1", "12", "99",
            "007", "69", "21", "00", "x", "xx", "_", ".", "yt", "tv",
            "hd", "tr", "official", "real", "pro", "dev", "admin", "test",
            "2020", "2021", "2022", "2023", "2024", "2025", "2026"]

SEPARATORS = ["", "_", ".", "-"]

YEARS = [str(y) for y in range(1970, 2027)]


def leet(s: str) -> str:
    table = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7"}
    return "".join(table.get(c, c) for c in s)


def generate(username: str):
    u = username.lower().strip()
    base = {u, u.capitalize(), u.upper(), leet(u)}

    results = set()

    for b in base:
        results.add(b)
        for p in PREFIXES:
            for sep in SEPARATORS:
                if p:
                    results.add(f"{p}{sep}{b}")

        for s in SUFFIXES:
            for sep in SEPARATORS:
                if s:
                    results.add(f"{b}{sep}{s}")

        for y in YEARS:
            results.add(f"{b}{y}")
            results.add(f"{b}_{y}")

        results.add(b + b)
        results.add(b + u[:3] if len(u) >= 3 else b)

    if " " in username:
        parts = [p.lower() for p in username.split() if p]
        if len(parts) >= 2:
            first, last = parts[0], parts[-1]
            for sep in SEPARATORS:
                results.add(f"{first}{sep}{last}")
                results.add(f"{first[0]}{sep}{last}")
                results.add(f"{first}{sep}{last[0]}")
                results.add(f"{last}{sep}{first}")
                results.add(f"{first}{last}")

    results.discard("")
    return sorted(results)


def main():
    parser = argparse.ArgumentParser(description="OSINT Username Wordlist Generator")
    parser.add_argument("-u", "--username", required=True, help="Hedef kullanıcı adı (isim soyisim de olabilir)")
    parser.add_argument("-o", "--output", default="wordlist.txt", help="Çıktı dosyası")
    args = parser.parse_args()

    words = generate(args.username)
    Path(args.output).write_text("\n".join(words), encoding="utf-8")

    print(f"\033[33m [+] \033[35m  {len(words)} aday üretildi -> {args.output}")


if __name__ == "__main__":
    main()
