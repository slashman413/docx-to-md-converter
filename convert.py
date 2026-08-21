#!/usr/bin/env python3
import os
import sys
import subprocess
import glob
from pathlib import Path

def convert_docx_to_md(input_path, output_dir):
    """
    Convert a docx file to markdown using pandoc, extracting media to the output directory.
    """
    input_file = Path(input_path)
    if not input_file.exists():
        print(f"Error: {input_file} does not exist.")
        return

    # Ensure output directory exists
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Set up output file path
    output_file = out_dir / f"{input_file.stem}.md"
    
    # Media directory for extracted images (relative)
    media_dir_name = f"{input_file.stem}_media"
    media_dir = out_dir / media_dir_name

    print(f"Converting {input_file.name} to Markdown...")
    
    # Pandoc command
    # -f docx : input format
    # -t gfm : output format as GitHub Flavored Markdown
    # --extract-media : folder to save images (pass relative so links are relative)
    # --wrap=none : avoid hard wrapping lines
    
    cmd = [
        "pandoc",
        "-f", "docx",
        "-t", "gfm",
        "--extract-media", media_dir_name,
        "--wrap=none",
        "-o", output_file.name,
        str(input_file.absolute())
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=str(out_dir))
        print(f"Success! Output saved to: {output_file}")
        print(f"Media saved to: {media_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion of {input_file.name}:")
        print(e.stderr.decode('utf-8'))

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert.py <input_file_or_dir> <output_dir>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2]

    if os.path.isdir(input_path):
        # Convert all docx in directory
        for docx_file in glob.glob(os.path.join(input_path, "*.doc*")):
            convert_docx_to_md(docx_file, output_dir)
    else:
        # Convert single file
        convert_docx_to_md(input_path, output_dir)

if __name__ == "__main__":
    main()
