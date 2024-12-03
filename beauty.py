import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

extended_cosmetics_df = pd.read_csv('extended_cosmetics_products.csv')
beauty_products_df = pd.read_csv('beauty_products.csv')

#CLEANING DATA USING DATAFRAME SLICING-CREATING PYTHON LIST TO PULL NEEDED COLUMNS
columns_from_ec_df = extended_cosmetics_df[['Product_Name','Brand','Category','Price_USD','Rating','Number_of_Reviews','Country_of_Origin']]
columns_from_bp_df = beauty_products_df[['Brand','Black_owned']]

#COMBINED NEW DATASET BY USING MERGE(LEFT JOIN)-if how='left' is not used, it's an inner join
melanin_newdata = pd.merge(columns_from_ec_df, columns_from_bp_df, how='left', left_on='Brand', right_on='Brand')
melanin_newdata['Black_owned'] = melanin_newdata['Black_owned'].fillna(True)

#IMAGES
img_brownfaces = mpimg.imread('brown_faces.jpeg')
img_threeladies = mpimg.imread('three_brown_ladies.jpeg')


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

# Group by category for Black-owned products and sum the reviews
black_owned_reviews = black_owned.groupby('Category')['Number_of_Reviews'].sum().reset_index()

# Sort by the number of reviews (descending order)
black_owned_reviews = black_owned_reviews.sort_values(by='Number_of_Reviews', ascending=False)
print("Black-owned Reviews Sorted and Summed:")
print(black_owned_reviews)

#PREPARING DATA FOR VISUALIZATION USING MATPLOTLIB
# Data for bar plot
revenues = [black_owned_revenue, non_black_owned_revenue]
labels = ['Black-Owned', 'Non-Black-Owned']

# Plot
plt.figure(figsize=(8, 6))
plt.bar(labels, revenues, color=['blue', 'orange'])
plt.title('Total Revenue Comparison')
plt.ylabel('Revenue (USD)')
plt.xlabel('Ownership')
plt.show()

# Data for pie chart
revenue_shares = [black_owned_revenue, non_black_owned_revenue]
labels = ['Black-Owned', 'Non-Black-Owned']
colors = ['blue', 'orange']

# Plot
plt.figure(figsize=(8, 6))
plt.pie(revenue_shares, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Revenue Proportions by Ownership')
plt.show()

# Horizontal Box Plot the most popular categories
plt.figure(figsize=(10, 6))
plt.barh(black_owned_reviews['Category'], black_owned_reviews['Number_of_Reviews'], color='blue')
plt.title('Most Popular Categories for Black-Owned Products (Based on Reviews)')
plt.xlabel('Number of Reviews')
plt.ylabel('Product Category')
plt.gca().invert_yaxis()  # Flip the y-axis for better readability
plt.show()

# Data for box plot
data = [black_owned['Price_USD'], non_black_owned['Price_USD']]

#Add image inside the box plot
plt.imshow(img_threeladies)

# Plot
plt.figure(figsize=(8, 6))
plt.boxplot(data, tick_labels=['Black-Owned', 'Non-Black-Owned'], patch_artist=True, 
            boxprops=dict(facecolor='blue', color='blue'), 
            medianprops=dict(color='yellow'), flierprops=dict(marker='o', color='red'))
plt.title('Price Distribution by Ownership')
plt.ylabel('Price (USD)')
plt.show()

melanin_newdata.to_csv('final_products_report.csv', index=False)
print("Data has been saved to 'final_products_report.csv'.")
