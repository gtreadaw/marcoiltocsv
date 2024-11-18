import pandas as pd 
import re


#import data - change path to wherever your file path is 
input_file = "./path/to/your/file"

#parse file to open contents 
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

#stripping white space from the data 
#expanded_data = expanded_data.str.strip()


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

#assigning protein columns to sequence and protein ID

# assigning column names of split data
split_columns_prot.columns = ['ProteinID', 'Sequence']
#concatenating
df_melted = pd.concat([df_melted, split_columns_prot], axis=1)


#making final dataframe 
df_final = df_melted[['Protein', 'ProteinID', 'Sequence', 'Residue', 'AA', 'Prob', 'Heptad']]
