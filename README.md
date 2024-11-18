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
1. Hard-Coded Path Version

    Open hardcodedmarcoil.py in your preferred Python IDE.

    Set the input_file variable to the path of the MARCOIL file you wish to convert:

```input_file = "./path/to/your/file"```

Run the script.

Save the resulting df_final DataFrame to your desired output path.

2. Command-Line Interface

  The commmand-line interface takes three arguments:
  
  - `Input` (Path to your input file)
  - `Output` (Path to your ourput file)
  - `filetype` (Output file type either txt or csv. Defaults to txt file.)

  Open your commandline of choice  -I have tested it with Bash only-

  Run the command-line interface in the following way: 
  
  ```python cli-marcoilconvert.py ./path/to/your/input.txt ./path/to/your/output.txt csv```

  If you want to run multiple input files, just add them sequentually like so: 
  
   ```python cli-marcoilconvert.py ./path/to/your/input.txt ./path/to/your/input2.txt ./path/to/your/output csv```

  Make sure the output is just a folder, not a file name. It will output all files with the input file name with _processed amended to the end. 

   
