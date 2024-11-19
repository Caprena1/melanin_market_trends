import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

extended_cosmetics_df = pd.read_csv('extended_cosmetics_products.csv')
beauty_products_df = pd.read_csv('beauty_products.csv')

#USING DATAFRAME SLICING-CREATING PYTHON LIST TO PULL NEEDED COLUMNS
columns_from_ec_df = extended_cosmetics_df[['Product_Name','Brand','Category','Price_USD','Rating','Number_of_Reviews','Country_of_Origin']]
columns_from_bp_df = beauty_products_df[['Brand','Black_owned']]

#CLEANING UP THE DATA IN EACH DATASET - DROP DUPLICATES 
unique_brands_ec = columns_from_ec_df.drop_duplicates(subset="Brand")
unique_brands_bp = columns_from_bp_df.drop_duplicates(subset="Brand")
unique_productname_ec = columns_from_ec_df.drop_duplicates(subset="Product_Name")
#combine_columns_ec_bp = [[unique_brands_ec, unique_brands_bp, unique_productname_ec]]


#COMBINED NEW DATASET BY USING MERGE(JOIN)
melanin_newdata = pd.merge(unique_brands_ec, unique_brands_bp, left_on='Brand', right_on='Brand')
#melanin_newdata_all = pd.concat(melanin_newdata,columns_from_bp_df, axis=1)

print(melanin_newdata)

