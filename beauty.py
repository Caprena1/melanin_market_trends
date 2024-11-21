import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

extended_cosmetics_df = pd.read_csv('extended_cosmetics_products.csv')
beauty_products_df = pd.read_csv('beauty_products.csv')

#CLEANING DATA USING DATAFRAME SLICING-CREATING PYTHON LIST TO PULL NEEDED COLUMNS
columns_from_ec_df = extended_cosmetics_df[['Product_Name','Brand','Category','Price_USD','Rating','Number_of_Reviews','Country_of_Origin']]
columns_from_bp_df = beauty_products_df[['Brand','Black_owned']]

#CLEANING UP THE DATA IN EACH DATASET - DROP DUPLICATES 
#unique_brands_ec = columns_from_ec_df.drop_duplicates(subset="Brand")
#unique_brands_bp = columns_from_bp_df.drop_duplicates(subset="Brand")
#unique_productname_ec = columns_from_ec_df.drop_duplicates(subset="Product_Name")


#COMBINED NEW DATASET BY USING MERGE(LEFT JOIN)-if how='left' is not used, it's an inner join
melanin_newdata = pd.merge(columns_from_ec_df, columns_from_bp_df, how='left', left_on='Brand', right_on='Brand')
melanin_newdata['Black_owned'] = melanin_newdata['Black_owned'].fillna('True')

#FILTERING THE DATA TO CALCULATE NEW VALUES
revenue = melanin_newdata[melanin_newdata['Price_USD'] == True]
black_owned = melanin_newdata[melanin_newdata['Black_owned'] == True]
non_black_owned = melanin_newdata[melanin_newdata['Black_owned'] == False]

#TOTAL REVENUE
all_revenue = revenue['Price_USD'].sum()
black_owned_revenue = black_owned['Price_USD'].sum()
non_black_owned_revenue = non_black_owned['Price_USD'].sum()

print(f'Total revenue: ${all_revenue}')
print(f'Black-owned companies revenue: ${black_owned_revenue}')
print(f'Other companies revenue: ${non_black_owned_revenue}')

#GROUP BY CATEGORY AND SUM $$
grouped = melanin_newdata.groupby(['Product_Name', 'Brand', 'Black_owned'])['Price_USD'].sum().reset_index()

#SEPARATE THE RESULTS FOR EASIER INTERPRETATION
black_owned_grouped = grouped[grouped['Black_owned'] == True]
non_black_owned_grouped = grouped[grouped['Black_owned'] == False]

print("Revenue by category for Black-owned companies:")
print(black_owned_grouped)

print("\nRevenue by category for non_Black-owned companies:")
print(non_black_owned_grouped)

#PREPARING DATA FOR VISUALIZATION USING MATPLOTLIB
comparison = melanin_newdata.groupby('Black_owned')['Price_USD'].sum()
comparison.index = ['Non-Black-Owned', 'Black-Owned'] #Renamed for clarity

#PLOT
comparison.plot(kind='bar', color=['orange', 'blue'], title='Revenue Comparison')
plt.ylabel('Total Revenue')
plt.show

#comparison.plot(kind='bar', color=['red', 'yellow'], title='Revenue Comparison')
#plt.ylabel('Total Revenue')
#plt.show

#comparison.plot(kind='sine', color=['orange', 'blue'], title='Revenue Comparison')
#plt.ylabel('Total Revenue')
#plt.show