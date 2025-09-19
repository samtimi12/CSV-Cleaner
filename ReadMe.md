# CSV/Excel Cleaner Tool

A simple yet powerful tool that cleans messy CSV and Excel files with just a few clicks. Built with Python, Pandas, and Tkinter.

This tool is designed for:
- Removing duplicate rows and columns  
- Automatically merging values when duplicate columns exist (e.g., `Score` and `Score1`)  
- Preserving original column order and casing  
- Stripping extra spaces inside cells (while keeping text case intact)  
- Replacing empty values with `Null`  
- Supporting both CSV and Excel (.xlsx/.xls) files  
- Saving cleaned files in the same format as the input  

---

## Features

- Auto-detects whether the input file is CSV or Excel  
- GUI interface for easy use  
- Cleans and formats data with one click  
- Saves the cleaned version with an auto-prefixed name (`cleaned_filename.csv` or `cleaned_filename.xlsx`)  
- Packaged as a Windows executable for non-developers  

---

## Example

### Input file (`students.csv` / `students.xlsx`)

| Name     | Age | Score | Score |
|----------|-----|-------|-------|
| Alice    | 20  | 85    | 85    |
| Bob      |     | 90    | 90    |
| Charlie  | 22  |       |       |
| Alice    | 20  | 85    | 85    |

### Cleaned output (`cleaned_students.csv` / `cleaned_students.xlsx`)

| Name     | Age  | Score |
|----------|------|-------|
| Alice    | 20   | 85    |
| Bob      | Null | 90    |
| Charlie  | 22   | Null  |

---

## Installation

### Option 1: Run the executable (Windows only)

1. Download the latest release from the Releases section.  
2. Double-click the `cleaner.exe` file.  
3. Use the GUI to select your file and output folder.  

No Python installation is required.

### Option 2: Run from source (developers)

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/csv-excel-cleaner.git
   cd csv-excel-cleaner
2. Create a virtual environment and activate it:
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate  # Linux/Mac
3. Install dependencies:
    pip install -r requirements.txt
4. Run the script
    python cleaner.py

## Build your own executable

To package as a .exe:
    pip install pyinstaller
    pyinstaller --onefile --noconsole cleaner.py

The executable will be created in the dist/ folder.

## Requirements

See requirements.txt:
    pandas
    openpyxl

## Tech Stack

- Python
- Pandas
- Tkinter
- PyInstaller

## Licenses

This project is licensed under the MIT License. You are free to use, modify, and distribute it.