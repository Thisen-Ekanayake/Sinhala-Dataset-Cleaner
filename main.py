import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document

# Regex: keep Sinhala, numbers, punctuation
CLEANING_REGEX = r'[^\u0D80-\u0DFF0-9\s.,!?:;"\'()\[\]<>\-]'

def clean_text(text):
    cleaned = re.sub(CLEANING_REGEX, '', text)
    # Normalize whitespace: collapse multiple spaces/newlines to single space
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            raw_text = file.read()

        cleaned_text = clean_text(raw_text)

        dir_name = os.path.dirname(filepath)
        base_name = os.path.basename(filepath)
        file_name_no_ext, _ = os.path.splitext(base_name)

        # Output paths
        txt_output_path = os.path.join(dir_name, f"{file_name_no_ext}_cleaned.txt")
        docx_output_path = os.path.join(dir_name, f"{file_name_no_ext}_cleaned.docx")

        # Save cleaned .txt
        with open(txt_output_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(cleaned_text)

        # Save cleaned .docx
        doc = Document()
        doc.add_paragraph(cleaned_text)
        doc.save(docx_output_path)

        return True, base_name
    except Exception as e:
        return False, f"{base_name} - Error: {str(e)}"

def main():
    root = tk.Tk()
    root.withdraw()

    while True:
        file_paths = filedialog.askopenfilenames(
            title="Select .txt Files to Clean",
            filetypes=[("Text Files", "*.txt")]
        )

        if not file_paths:
            break  # user canceled

        success_files = []
        error_files = []

        for file_path in file_paths:
            success, message = process_file(file_path)
            if success:
                success_files.append(message)
            else:
                error_files.append(message)

        summary = f"Cleaned Files:\n" + "\n".join(success_files)
        if error_files:
            summary += f"\n\nErrors:\n" + "\n".join(error_files)

        # Ask to clean more or exit
        response = messagebox.askquestion(
            "Cleaning Completed",
            summary + "\n\nDo you want to clean more files?",
            icon='question'
        )

        if response == 'no':
            break  # Exit loop

if __name__ == "__main__":
    main()
