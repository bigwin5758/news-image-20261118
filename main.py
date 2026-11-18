"""Copy the entry image to the output directory.

The program ships with its image (entry.png) and simply copies it to
$MAKEFUN_OUTPUT_DIR (or /output) as entry.png. Deterministic: the same
bytes come out on every run. After copying it checks the output file
is there and the same size as the source, so a truncated write fails
loudly instead of shipping a broken image.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(source, dest)
    if dest.stat().st_size != source.stat().st_size:
        print("error: copied entry.png is not the same size as the source",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
