# Docx to Markdown Converter

This repository contains a simple Python script (`convert.py`) that uses `pandoc` to convert Microsoft Word documents (`.docx`) into GitHub Flavored Markdown (`.md`), while preserving tables, code blocks, text alignment (to the extent supported by markdown), and extracting embedded images.

## Dependencies

- Python 3.x
- [Pandoc](https://pandoc.org/) (must be installed and available in your system's PATH).

## Usage

Run the script and provide the input file (or directory) and the output directory.

```bash
python convert.py <input_file_or_dir> <output_dir>
```

### Examples

Convert a single file:
```bash
python convert.py /path/to/document.docx /path/to/output_folder
```

Convert all `.docx` files in a directory:
```bash
python convert.py /path/to/input_folder /path/to/output_folder
```

## Features
- Converts `.docx` to GitHub Flavored Markdown (`gfm`), ensuring tables and code blocks render correctly.
- Extracts images and media files into a `<filename>_media` subdirectory within the output folder.
- Does not enforce hard line wrapping for better readability.
