# Hex Viewer

A command-line file inspector: a classic hex dump (offset | hex | ASCII), file-type
detection from magic bytes, and extraction of printable strings buried in binary data.

Built to practice byte/bit-level data manipulation in Python — raw file I/O, `bytes`
iteration, and the printable-vs-unprintable distinction that comes up constantly when
working with binary formats.

## Usage

```
$ python3 hexview.py tests/fixtures/test.txt --dump
00000000 | 54 68 69 73 20 69 73 20 61 20 73 65 6e 74 65 6e  | This 
is a senten
00000010 | 63 65 2e                                         | ce.
Total bytes read: 19

$ python3 hexview.py tests/fixtures/test.txt --identify
unknown file type

$ python3 hexview.py tests/fixtures/test.txt --strings
Offset: 00000000, Characters: This is a sentence.

$ python3 hexview.py tests/fixtures/test.txt --all
00000000 | 54 68 69 73 20 69 73 20 61 20 73 65 6e 74 65 6e  | This 
is a senten
00000010 | 63 65 2e                                         | ce.
Total bytes read: 19
unknown file type
Offset: 00000000, Characters: This is a sentence.
```

## How it works

The dump feature reads chunks of up to 16 bytes of the file at a time. The feature reads chunks of 
16 bytes, since 16 bytes produces line width that fits comfortably in a standard 80-column terminal,
and 16 is a clean power-of-2 that divides evenly into common data sizes. The feature then makes a 
row for each chunk of bytes. Each row displays the offset, the hex format, and the ASCII of the 
bytes that were read.

The identify feature is used to read what type of file your file is. It reads the first 4 bytes of 
the file, and compares it to a dictionary of known signatures that correspond to specific file 
types. For instance, PNG files always begin with the bytes \x89PNG.

The string feature reads one byte at a time, and checks for strings by seeing if 4 or more bytes in 
a row can be converted to printable ASCII. The feature checks for at least 4 printable bytes in a 
row, to ensure that those bytes are actual text, and not coincidental matches. The feature then 
prints each valid string it found along with its offset.

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
python3 hexview.py <file> --dump
python3 hexview.py <file> --identify
python3 hexview.py <file> --strings
python3 hexview.py <file> --all
```

