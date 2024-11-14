import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

extended_cosmetics_df = pd.read_csv('extended_cosmetics_products.csv')
beauty_products_df = pd.read_csv('beauty_products.csv')

#USING DATAFRAME SLICING-CREATING PYTHON LIST TO PULL NEEDED COLUMNS
columns_from_ec_df = extended_cosmetics_df[['Product_Name','Brand','Category','Price_USD','Rating','Number_of_Reviews','Skin_Type','Cruelty_Free','Country_of_Origin']]
columns_from_bp_df = beauty_products_df[['Brand','All_vegan','Black_owned']]

#CLEANING UP THE DATA IN EACH DATASET



#COMBINED NEW DATASET BY USING MERGE(JOIN)
melanin_newdata = pd.merge(columns_from_ec_df, columns_from_bp_df, left_on='Brand', right_on='Brand')

#columns_from_ec_df.columns = columns_from_ec_df.columns.str.strip()
#columns_from_bp_df.columns = columns_from_bp_df.columns.str.strip()



#print(columns_from_ec_df)
print(melanin_newdata)

