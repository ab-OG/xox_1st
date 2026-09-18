# XOX 1st

Local-first audio and video transcription toolkit for developers working with recorded media.

## What it does

XOX 1st is an early-stage open-source project for turning recorded audio/video into searchable, timestamped text while keeping the processing workflow local when possible.

The first prototype is intentionally small:

- Uses a local `whisper-cli` installation for transcription
- Supports common audio/video inputs accepted by the local Whisper build
- Exports timestamped VTT subtitles and plain-text transcripts
- Keeps source media and generated transcripts on the user's machine
- Provides a simple command-line interface that can be extended with search, metadata, and analysis features

## Current status

Early prototype / active development.

The project is being developed and tested on Apple Silicon, with Whisper's Metal acceleration available when supported by the local build.

## Quick start

Make sure `whisper-cli` is installed and available on your PATH.

```bash
python3 src/xox.py recording.wav --language auto --output transcript
```

This produces:

- `transcript.txt`
- `transcript.vtt`

For a fixed language:

```bash
python3 src/xox.py recording.wav --language hi --output recording_hi
```

## Roadmap

- Better media format handling
- Batch transcription
- Searchable transcript index
- Speaker/segment metadata
- Evaluation and benchmarking utilities
- Optional evidence and annotation workflows
- Improved documentation and packaging

## Privacy

XOX 1st is designed around local processing. It does not require uploading recordings to a hosted transcription service.

## License

MIT
