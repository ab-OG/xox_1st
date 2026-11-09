# XOX 1st

A local-first command-line toolkit for turning recorded audio and video into timestamped transcripts and subtitles.

## What it does

The early prototype uses a local `whisper-cli` installation to process media supported by that Whisper build. It can produce plain-text transcripts and VTT subtitles while keeping source media and generated files on your machine.

## Quick start

Install `whisper-cli` and make sure it is available on your `PATH`. Then run:

```sh
python3 src/xox.py recording.wav --language auto --output transcript
```

This produces `transcript.txt` and `transcript.vtt`. To specify a language, for example Hindi:

```sh
python3 src/xox.py recording.wav --language hi --output recording_hi
```

## Status and privacy

Early-stage prototype, developed and tested on Apple Silicon; Metal acceleration is available when supported by the local Whisper build. The workflow is designed for local processing and does not require uploading recordings to a hosted transcription service. Review generated transcripts for recognition errors before relying on them.

## Roadmap

Planned directions include broader media handling, batch transcription, searchable transcript indexing, speaker/segment metadata, evaluation tools, and optional evidence/annotation workflows.

## License

MIT
