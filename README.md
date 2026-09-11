# Hex Viewer

A command-line file inspector: a classic hex dump (offset | hex | ASCII), file-type
detection from magic bytes, and extraction of printable strings buried in binary data.

Built to practice byte/bit-level data manipulation in Python — raw file I/O, `bytes`
iteration, and the printable-vs-unprintable distinction that comes up constantly when
working with binary formats.

## Usage

```
$ hexview dump file.bin
(paste real output here once the dump command works)

$ hexview identify file.bin
(paste real output here)

$ hexview strings file.bin --min-len 4
(paste real output here)
```

## How it works

(Fill this in once the tool is built. Cover: why 16 bytes per row, how magic-byte
detection works, how the string-extraction scan works.)

## Installation

```
git clone <your-repo-url>
cd hex-viewer
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```
python -m hexview dump <file>
```

(Update this once the CLI entry point exists.)
