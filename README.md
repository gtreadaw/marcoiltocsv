# MARCOIL to CSV Converter

**A script to convert MARCOIL coiled-coil prediction outputs into a long-format CSV file for downstream analysis.**  
*All credit for MARCOIL and its functionality goes to its original authors and designers.*

---

## **Why Use This Script?**

The MARCOIL output is not immediately analysis-friendly, especially when handling multiple datasets or species predictions. This script automates the conversion process to streamline data analysis, saving time and reducing errors.

Key highlights:
- Converts MARCOIL output into a long-format CSV file for easier analysis.
- Includes command-line arguments for greater flexibility.
- A great practice tool for integrating file handling and data processing with Python.

---

## **Features**

- Converts single MARCOIL output files into CSV format.  
- **Two versions** of the script are available:
  1. **Hard-Coded Path Version**: For quick use with a pre-defined file path.
  2. **Command-Line Interface (CLI) Version**: For flexibility and batch processing.  
- In the future: **Concatenation of multiple files** into one CSV file when a specific argument is provided.

---

## **Dependencies**

Ensure the following Python libraries are installed:

- `pandas` (tested with version 2.2.3)
- `re` (Python standard library)
- `argparse` (Python standard library)
- `os` (Python standard library)

---

## **How to Use the Script**

### 1. **Hard-Coded Path Version**

1. Open `hardcodedmarcoil.py` in your preferred Python IDE.  
2. Set the `input_file` variable to the path of the MARCOIL ProbList output file you wish to convert:

    ```python
    input_file = "./path/to/your/file"
    ```

3. Run the script.  
4. Save the resulting `df_final` DataFrame to your desired output path.

---

### 2. **Command-Line Interface (CLI) Version**

The command-line interface takes three arguments:  
- **`input`**: Path to your input file(s).  
- **`output`**: Path to your output file or directory.  
- **`filetype`**: (Optional) File type for the output, either `txt` or `csv`. Defaults to `txt`.

#### **Steps to Use CLI:**

1. Open your command line interface of choice (*tested with Bash*).  
2. Run the script with the following syntax:

    ```bash
    python cli-marcoilconvert.py <input> <output> [filetype]
    ```

#### **Example for a Single Input File:**

```bash
python cli-marcoilconvert.py ./path/to/your/input.txt ./path/to/your/output.txt csv
```

#### **Example for Multiple Input Files:**
```bash
python cli-marcoilconvert.py ./path/to/your/input1.txt ./path/to/your/input2.txt ./path/to/output_directory csv
```

Important Notes:

  For multiple input files, the output should be a folder, not a specific file name.
  The output files will be saved in the folder you specify, with _processed appended to their original filenames.
  
  Example: `input1.txt` → `input1_processed.csv`.
