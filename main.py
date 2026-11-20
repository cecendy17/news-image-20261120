#!/usr/bin/env python3
"""News-image entry point (stdlib only).

make.fun bounty: "Sum up 20 November's world news in one image".

This program writes the entry image to /output/entry.png. It uses only
the Python standard library (pathlib / shutil / hashlib) and performs
no network access. The image itself (entry.png, bundled next to this
file) was rendered beforehand by generate.py (Python + Pillow, run
locally, no network); this file is the deterministic sandbox entry
point: it copies those exact bytes to the output path, so running it
twice always produces byte-identical output.

Usage (as the judge runs it):
    python3 main.py            # writes /output/entry.png

Local test (optional output-path override, first argument only):
    python3 main.py /tmp/out/entry.png
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DEFAULT_OUT = Path("/output/entry.png")


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    if not SRC.is_file():
        print(f"error: bundled image not found: {SRC}", file=sys.stderr)
        return 1
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out)  # exact byte copy, deterministic
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"wrote {out} ({out.stat().st_size} bytes) sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
