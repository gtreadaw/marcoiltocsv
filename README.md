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

## **Installation**

Clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/marcoil-to-csv.git
cd marcoil-to-csv

