import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def clean_data(df):
    # Normalize column names: strip spaces, unify case, remove suffixes like .1, .2
    col_map = {}
    new_cols = []
    for col in df.columns:
        base_col = col.strip()  # remove extra spaces
        base_col_lower = base_col.lower().split(".")[0]  # treat Score.1 same as Score
        if base_col_lower not in col_map:
            col_map[base_col_lower] = base_col  # preserve first seen version
            new_cols.append(base_col)
        else:
            new_cols.append(base_col_lower)  # mark as duplicate
    df.columns = new_cols

    # Handle duplicate columns by merging into the first one
    seen = {}
    drop_cols = []
    for col in df.columns:
        col_lower = col.lower()
        if col_lower not in seen:
            seen[col_lower] = col
        else:
            # Merge values: fill empty cells in original with data from duplicate
            original_col = seen[col_lower]
            df[original_col] = df[original_col].combine_first(df[col])
            drop_cols.append(col)

    df = df.drop(columns=drop_cols)

    # Strip leading/trailing spaces in all cells (keep casing)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop duplicate rows (ignoring case + whitespace)
    df = df.drop_duplicates(
        subset=df.columns.tolist(),
        keep="first",
        ignore_index=True
    )

    # Fill empty cells with 'Null'
    df = df.where(pd.notnull(df), 'Null')

    return df


def clean_file(input_file, output_folder):
    ext = os.path.splitext(input_file)[1].lower()
    if ext == ".csv":
        df = pd.read_csv(input_file, dtype=str, keep_default_na=False, na_values=[''])
    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(input_file, dtype=str, keep_default_na=False, na_values=[''])
    else:
        raise ValueError("Unsupported file format. Please select a CSV or Excel file.")

    cleaned_df = clean_data(df)

    # Save cleaned file in same format as input
    output_file = os.path.join(output_folder, f"cleaned_{os.path.basename(input_file)}")
    if ext == ".csv":
        cleaned_df.to_csv(output_file, index=False)
    else:
        cleaned_df.to_excel(output_file, index=False)

    return output_file


def select_input_file():
    global input_file
    input_file = filedialog.askopenfilename(
        title="Select a CSV or Excel file",
        filetypes=[("CSV and Excel files", "*.csv *.xlsx *.xls")]
    )
    if input_file:
        input_label.config(text=f"Selected: {os.path.basename(input_file)}")


def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        output_label.config(text=f"Output Folder: {output_folder}")


def run_cleaner():
    try:
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        if not output_folder:
            messagebox.showerror("Error", "Please select an output folder.")
            return

        output_file = clean_file(input_file, output_folder)
        messagebox.showinfo("Success", f"File cleaned and saved as:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"Error cleaning file:\n{str(e)}")


# GUI Setup
root = tk.Tk()
root.title("CSV/Excel Cleaner")
root.geometry("500x250")

input_file = ""
output_folder = ""

tk.Label(root, text="Step 1: Select your input file").pack(pady=5)
tk.Button(root, text="Browse File", command=select_input_file).pack()
input_label = tk.Label(root, text="No file selected", fg="gray")
input_label.pack()

tk.Label(root, text="Step 2: Select output folder").pack(pady=5)
tk.Button(root, text="Browse Folder", command=select_output_folder).pack()
output_label = tk.Label(root, text="No folder selected", fg="gray")
output_label.pack()

tk.Label(root, text="Step 3: Clean the file").pack(pady=10)
tk.Button(root, text="Run Cleaner", command=run_cleaner, bg="green", fg="white").pack()

root.mainloop()
