import pandas as pd
import re
import argparse
import os

def process_data(input_file):
    # Parse file to open contents
    with open(input_file, "r") as file: 
        coildata = file.read()

    #regular expression to identify the string of asterisks to split the data 
    sections = re.split(r'\n\*{2,}\n', coildata)

    #split list into new list whenever the cc title starts 
    sections = [i.split('cc-probability in percent and best heptad phase') for i in sections]

    # converting sections into dataframe where first part of nested list is the protein name and \n
    # second part is the marcoil prediction
    f = (pd.DataFrame(sections, columns=['Protein', 'Marcoil']))
    
    #remove any blanks before reading 
    f.dropna(inplace=True) 

    # Split the 'Marcoil' column by newline
    expanded_data = f["Marcoil"].str.split("\n", expand=True)
    # Step 2: Replace empty strings with NaN
    expanded_data.replace("", pd.NA, inplace=True)


    #removing blank NaN after replacing empty strings
    expanded_data.dropna(how='all', inplace=True)


    # Replace multiple spaces with a single space
    stacked = pd.concat([f['Protein'], expanded_data], axis = 1)

    #convert data to long format 
    df_melted = stacked.melt(id_vars=[stacked.columns[0]], value_vars=stacked.columns[2:])

    #remove blank data
    df_melted.dropna(inplace=True) 


    #splitting column to marcoil prediction
    df_melted['value'] = df_melted['value'].str.strip()


    # Replace multiple spaces with a single space
    df_melted['value'] = df_melted['value'].str.replace(r"\s+", " ", regex=True)


    #splitting single white space after replacing multiple empty spaces to one 
    split_columns = df_melted['value'].str.split(" ", expand = True)

    # assigning column names of split data
    split_columns.columns = ['Residue', 'AA', 'Prob', 'Heptad']

    #combining data 
    df_melted = pd.concat([df_melted, split_columns], axis=1)

    #splitting data to give us protein name and sequence 
    split_columns_prot = df_melted['Protein'].str.split(r'##\s\d+', expand=True)

    # assigning column names of split data
    split_columns_prot.columns = ['ProteinID', 'Sequence']
    
    #concatenating the protein data with the split marcoil data
    df_melted = pd.concat([df_melted, split_columns_prot], axis=1)


    #making final dataframe with newly created variables
    df_final = df_melted[['Protein', 'ProteinID', 'Sequence', 'Residue', 'AA', 'Prob', 'Heptad']]
    
    return(df_final)


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Process coiled-coil prediction data files.")
    #input files to run code on 
    parser.add_argument('input_files', nargs='+', help="Input file(s) to process")
    
    #defining path to output the data
    parser.add_argument('output_path', help="Path to save the output file")
    
    #output file type - defaults to txt file but can be csv. Txt file is comma delimited format (sep = ',')
    parser.add_argument('output_type', choices=['txt', 'csv'], default='txt', help = "Type of output file - defaults to txt file")

    args = parser.parse_args()

    # Iterate over the input files and process each
    for input_file in args.input_files:
        print(f"Processing file: {input_file}")
        df = process_data(input_file)  #runs process data function from above which returns dataframe
        if args.output_type == "txt":  #outputs txt file if argument is txt
            output_file = f"{args.output_path}/{input_file.split('/')[-1].split('.')[0]}_processed.txt"
            df.to_csv(output_file, index=False)
            print(f"Data saved to {output_file}")
        elif args.output_type == "csv":  #outputs csv file if argument is csv 
            output_file = f"{args.output_path}/{input_file.split('/')[-1].split('.')[0]}_processed.csv"
            df.to_csv(output_file, index=False)
            print(f"Data saved to {output_file}")

    # Ensure the output path contains a filename
    if os.path.isdir(args.output_path):
        # If only a directory is provided, use a default filename
        output_file = os.path.join(args.output_path, "processed_data.") 
    else:
        # If provided a full file path, use it as is
        output_file = args.output_path
        

if __name__ == "__main__":
    main()
