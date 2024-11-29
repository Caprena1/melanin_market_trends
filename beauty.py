import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

extended_cosmetics_df = pd.read_csv('extended_cosmetics_products.csv')
beauty_products_df = pd.read_csv('beauty_products.csv')

#CLEANING DATA USING DATAFRAME SLICING-CREATING PYTHON LIST TO PULL NEEDED COLUMNS
columns_from_ec_df = extended_cosmetics_df[['Product_Name','Brand','Category','Price_USD','Rating','Number_of_Reviews','Country_of_Origin']]
columns_from_bp_df = beauty_products_df[['Brand','Black_owned']]

#COMBINED NEW DATASET BY USING MERGE(LEFT JOIN)-if how='left' is not used, it's an inner join
melanin_newdata = pd.merge(columns_from_ec_df, columns_from_bp_df, how='left', left_on='Brand', right_on='Brand')
melanin_newdata['Black_owned'] = melanin_newdata['Black_owned'].fillna(True)

#FILTERING THE DATA TO CALCULATE NEW VALUES
black_owned = melanin_newdata[melanin_newdata['Black_owned'] == True]
non_black_owned = melanin_newdata[melanin_newdata['Black_owned'] == False]

#TOTAL REVENUE AND TOTAL REVENUE GROUPED
all_revenue = melanin_newdata['Price_USD'].sum()
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
comparison = pd.Series([100, 200], index=['Non-Black', 'Black-Owned'])

# #PLOT - BAR
comparison.plot(kind='bar', color=['orange', 'blue'], title='Revenue Comparison-Bar')
plt.ylabel('Revenue Comparison 1')
plt.show()

#PLOT - PIE
comparison.plot(kind='pie', colors=['red', 'yellow'], title='Revenue Comparison-Pie', autopct='%1.1f%%')
plt.ylabel('') #Removes y-axis label for cleaner aesthetics
plt.show()

#PLOT - BOX 
plt.boxplot(comparison)
plt.title('Revenue Comparison - Box Plot')
plt.ylabel('Revenue Comparison 3')
plt.show()
#PLOT - SCATTER
plt.scatter(comparison.index, comparison.values, color='green', label='Revenue Comparison-Scatter')
plt.legend()
plt.show()

#PLOT - SINE WAVE
x = np.linspace(0,2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y, color='green', label='Revenue Comparison Sine Wave')
plt.legend()
plt.show()




