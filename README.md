# marcoiltocsv
Script to convert output of MARCOIL coiled-coil prediction to a long-format CSV file for analysis

EVERYTHING MARCOIL IS CREDITED TO THE AUTHORS AND ORIGINAL DESIGNERS OF MARCOIL

**WHY DID I WANT TO MAKE THIS?**

I was doing some data analysis with MARCOIL, and the output isn't in the most immediately useable format. I output predictions from quite a few databses, 
so thought it might be nice to make a script that will format it for me automatically should I want to analyze any other databses or species. I got to practice 
using command line arguments for this project, which was a fun learning experience!

Coming in the future I'd like to be able to concatenate datafile output if an argument is given to concatenate the files. Currently they are output individually.


Dependencies Information: 
Name: pandas Version: 2.2.3
Name: re
Name: argparse
Name: os


**HOW TO USE THIS CODE?**

I put two versions up, one hard-coded path version and one command line version. 

1. **Hard Coded Path**:
To use the hard-coded path, open the hardcodedmarcoil.py script in your python IDE of choice and set the path to your file of choice. Run all the lines, and save the df_final to your output path of choice. 
'''
input_file = "./path/to/your/file"

'''
