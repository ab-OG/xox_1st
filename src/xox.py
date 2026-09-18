#!/usr/bin/env python3
"""Small local wrapper around whisper-cli for timestamped transcription."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe local media with whisper-cli.")
    parser.add_argument("input", type=Path, help="Path to an audio/video file.")
    parser.add_argument("--language", default="auto", help="Whisper language code, or 'auto'.")
    parser.add_argument("--output", default=None, help="Output path without extension.")
    parser.add_argument("--model", default=None, help="Path to a Whisper model.")
    args = parser.parse_args()

    if shutil.which("whisper-cli") is None:
        parser.error("whisper-cli was not found on PATH.")

    if not args.input.exists():
        parser.error(f"Input file not found: {args.input}")

    output = Path(args.output) if args.output else args.input.with_suffix("")
    command = [
        "whisper-cli",
        "-m",
        args.model or "models/ggml-medium.bin",
        "-l",
        args.language,
        "-otxt",
        "-ovtt",
        "-of",
        str(output),
        str(args.input),
    ]

    print("Running:", " ".join(command))
    return subprocess.call(command)


if __name__ == "__main__":
    raise SystemExit(main())
