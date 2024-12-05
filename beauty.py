import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.style.use('dark_background')
import numpy as np

#IMAGES

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

# Group by Brand for Black-owned and non-Black-owned companies, and calculate total revenue
black_owned_revenue_brand = black_owned.groupby('Brand')['Price_USD'].sum().reset_index()
black_owned_revenue_brand.columns = ['Brand', 'Total_Revenue']
black_owned_revenue_brand = black_owned_revenue_brand.sort_values(by='Total_Revenue', ascending=False)

non_black_owned_revenue_brand = non_black_owned.groupby('Brand')['Price_USD'].sum().reset_index()
non_black_owned_revenue_brand.columns = ['Brand', 'Total_Revenue']
non_black_owned_revenue_brand = non_black_owned_revenue_brand.sort_values(by='Total_Revenue', ascending=False)

print("Black-owned Revenue by Brand:")
print(black_owned_revenue_brand)
print("Non-black-owned Revenue by Brand:")
print(non_black_owned_revenue_brand)

# Group by category for Black-owned products and sum the reviews
black_owned_reviews = black_owned.groupby('Category')['Number_of_Reviews'].sum().reset_index()

# Sort by the number of reviews (descending order)
black_owned_reviews = black_owned_reviews.sort_values(by='Number_of_Reviews', ascending=False)
print("Black-owned Reviews Sorted and Summed:")
print(black_owned_reviews)

# Group by Country and Brand for Black-owned companies, and calculate total revenue
black_owned_country_revenue = black_owned.groupby(['Country_of_Origin', 'Brand'])['Price_USD'].sum().reset_index()

# Sort by Country of Origin alphabetically, and within each country by revenue in descending order
black_owned_country_revenue = black_owned_country_revenue.sort_values(by=['Country_of_Origin', 'Price_USD'], ascending=[True, False])

# Rename columns for clarity
black_owned_country_revenue.columns = ['Country_of_Origin', 'Brand', 'Total_Revenue']

print("Black-owned companies ranked by revenue and sorted by country:")
print(black_owned_country_revenue)


#PREPARING DATA FOR VISUALIZATION USING MATPLOTLIB
# Data for bar plot
revenues = [black_owned_revenue, non_black_owned_revenue]
labels = ['Black-Owned', 'Non-Black-Owned']

# Bar Plot
plt.figure(figsize=(8, 6))
plt.bar(labels, revenues, color=['blue', 'orange'])
plt.title('Total Revenue Comparison')
plt.ylabel('Revenue (USD)')
plt.xlabel('Ownership')
plt.show()

# Data for pie chart - Combine top brands from each group for visualization
top_black_owned = black_owned_revenue_brand.head(10)
top_non_black_owned = non_black_owned_revenue_brand.head(10)

# Pie chart for Black-owned companies
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(
    top_black_owned['Total_Revenue'], 
    labels=top_black_owned['Brand'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Blues(np.linspace(0.5, 1, len(top_black_owned)))
)
plt.title('Top Black-Owned Companies by Revenue')

# Pie chart for Non-Black-owned companies
plt.subplot(1, 2, 2)
plt.pie(
    top_non_black_owned['Total_Revenue'], 
    labels=top_non_black_owned['Brand'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Oranges(np.linspace(0.5, 1, len(top_non_black_owned)))
)
plt.title('Top Non-Black-Owned Companies by Revenue')
plt.tight_layout()
plt.show()

# Horizontal Box Plot the most popular categories
plt.figure(figsize=(10, 6))
plt.barh(black_owned_reviews['Category'], black_owned_reviews['Number_of_Reviews'], color='blue')
plt.title('Most Popular Categories for Black-Owned Products (Based on Reviews)')
plt.xlabel('Number of Reviews')
plt.ylabel('Product Category')
plt.gca().invert_yaxis()  # Flip the y-axis for better readability
plt.show()

# Data for grouped bar chart 
top_countries = black_owned_country_revenue['Country_of_Origin'].unique()[:208]
filtered_data = black_owned_country_revenue[black_owned_country_revenue['Country_of_Origin'].isin(top_countries)]

# Grouped Bar Chart Plot
plt.figure(figsize=(14, 8))
for country in top_countries:
    country_data = filtered_data[filtered_data['Country_of_Origin'] == country]
    plt.bar(
        country_data['Brand'], 
        country_data['Total_Revenue'], 
        label=country, alpha=0.8
    )

plt.title('Top Black-Owned Companies by Revenue, Sorted by Country', fontsize=16)
plt.xlabel('Brand', fontsize=14)
plt.ylabel('Total Revenue (USD)', fontsize=14)
plt.xticks(rotation=20, ha='right')
plt.legend(bbox_to_anchor=(1, 1), title='Country of Origin')
plt.tight_layout()
plt.show()

melanin_newdata.to_csv('final_products_report.csv', index=False)
print("Data has been saved to 'final_products_report.csv'.")
