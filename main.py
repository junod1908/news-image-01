"""news-image-01 entry program.

Copies the poster image stored beside this file (entry.png) to the output
directory as entry.png. Deterministic: the output is a byte-for-byte copy of
the stored image on every run. Standard library only, no network.

The grader runs this in a container with a writable /output; outside that
container, MAKEFUN_OUTPUT_DIR names the output directory instead.
"""

import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
CHUNK = 65536


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    written = 0
    with SOURCE.open("rb") as src, dest.open("wb") as dst:
        while chunk := src.read(CHUNK):
            dst.write(chunk)
            written += len(chunk)
    if written != SOURCE.stat().st_size:
        raise IOError(f"copy incomplete: wrote {written} of {SOURCE.stat().st_size} bytes")


if __name__ == "__main__":
    main()
