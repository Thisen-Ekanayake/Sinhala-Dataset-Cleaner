# Sinhala Dataset Cleaner
A simple Python tool to clean Sinhala text files by removing non-Sinhala characters while keeping numbers and punctuation by default.
The tool also normalizes whitespace by collapsing multiple spaces and newlines into a single space.

Cleaned outputs are saved as both .txt and .docx files in the same directory as the original files, with _cleaned appended to the filenames.
This tool is packaged as a standalone .exe for easy use by non-technical users - no need to install Python or run commands.

## Features
- Removes all characters except Sinhala letters (Unicode U+0D80–U+0DFF), numbers, and common punctuation.
- Normalizes whitespace automatically.
- Batch process multiple .txt files via a file picker GUI.
- Saves output in both .txt and .docx formats.
- Easy-to-use graphical interface using Tkinter.
- Keeps original files unchanged.

## For non-technical users:
- **Just download Sinhala_Text_Cleaner.exe and run**

## For Developers:
- **Read below instructions**

### Requirements
- Python 3.6 or above
- python-docx library for .docx file creation

### Install dependencies using pip:
```
pip install python-docx
```

### Usage
**Run the script:**
```
python sinhala_cleaner.py
```
- A file selection window will appear — select one or multiple .txt files to clean.
- The tool will process the files, saving cleaned versions alongside the originals.
- After completion, you will see a summary dialog with cleaned files and any errors.
- Choose whether to clean more files or exit the tool.

## How It Works
- Reads selected .txt files in UTF-8 encoding.
- Removes unwanted characters using a regex filter.
- Collapses multiple whitespace characters into a single space.
- Saves the cleaned text as originalfilename_cleaned.txt and .docx.

## Example
**Original file:**
- example.txt

**Cleaned files:**
- example_cleaned.txt
- example_cleaned.docx

## Author
- Thisen Ekanayake

## License
- MIT License
