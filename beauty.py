import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.style.use('dark_background')
import numpy as np

#DATASETS BEING READ IN
extended_cosmetics_df = pd.read_csv('extended_cosmetics_products.csv')
beauty_products_df = pd.read_csv('beauty_products.csv')

#CLEANING DATASET BY CHANGING COLUMN HEADINGS TO UPPERCASE TO STAND OUT BETTER
extended_cosmetics_df.columns = extended_cosmetics_df.columns.str.upper()
beauty_products_df.columns = beauty_products_df.columns.str.upper()

#CLEANING DATA USING DATAFRAME SLICING-CREATING PYTHON LIST TO PULL NEEDED COLUMNS
columns_from_ec_df = extended_cosmetics_df[['PRODUCT_NAME', 'BRAND', 'CATEGORY', 'PRICE_USD', 'RATING', 'NUMBER_OF_REVIEWS', 'COUNTRY_OF_ORIGIN']]
columns_from_bp_df = beauty_products_df[['BRAND', 'BLACK_OWNED']]

#CLEANING THE BRAND COLUMN - CORRECTING THE BRAND(e.l.f.)
columns_from_ec_df['BRAND'] = columns_from_ec_df['BRAND'].replace(['E.l.f', 'e.l.f', 'E.L.F', 'Elf', 'e.L.F', 'E.l.f.', 'E.L.F.','e.L.F.'], 'e.l.f.')

#COMBINED NEW DATASET BY USING MERGE(LEFT JOIN)-if how='left' is not used, it's an inner join
melanin_newdata = pd.merge(columns_from_ec_df, columns_from_bp_df, how='left', left_on='BRAND', right_on='BRAND')
melanin_newdata['BLACK_OWNED'] = melanin_newdata['BLACK_OWNED'].fillna(True)

#FILTERING THE DATA TO CALCULATE NEW VALUES
black_owned = melanin_newdata[melanin_newdata['BLACK_OWNED'] == True]
non_black_owned = melanin_newdata[melanin_newdata['BLACK_OWNED'] == False]

#TOTAL REVENUE AND TOTAL REVENUE GROUPED
all_revenue = melanin_newdata['PRICE_USD'].sum()
black_owned_revenue = black_owned['PRICE_USD'].sum()
non_black_owned_revenue = non_black_owned['PRICE_USD'].sum()

print(f'Total revenue: ${all_revenue}')
print(f'Black-owned companies revenue: ${black_owned_revenue}')
print(f'Other companies revenue: ${non_black_owned_revenue}')

#GROUP BY CATEGORY AND SUM $$
grouped = melanin_newdata.groupby(['PRODUCT_NAME', 'BRAND', 'BLACK_OWNED'])['PRICE_USD'].sum().reset_index()

#SEPARATE THE RESULTS FOR EASIER INTERPRETATION
black_owned_grouped = grouped[grouped['BLACK_OWNED'] == True]
non_black_owned_grouped = grouped[grouped['BLACK_OWNED'] == False]

print("Revenue by category for Black-owned companies:")
print(black_owned_grouped)

print("\nRevenue by category for non_Black-owned companies:")
print(non_black_owned_grouped)

# Group by Brand for Black-owned and non-Black-owned companies, and calculate total revenue
black_owned_revenue_brand = black_owned.groupby('BRAND')['PRICE_USD'].sum().reset_index()
black_owned_revenue_brand.columns = ['BRAND', 'TOTAL_REVENUE']
black_owned_revenue_brand = black_owned_revenue_brand.sort_values(by='TOTAL_REVENUE', ascending=False)

non_black_owned_revenue_brand = non_black_owned.groupby('BRAND')['PRICE_USD'].sum().reset_index()
non_black_owned_revenue_brand.columns = ['BRAND', 'TOTAL_REVENUE']
non_black_owned_revenue_brand = non_black_owned_revenue_brand.sort_values(by='TOTAL_REVENUE', ascending=False)

print("Black-owned Revenue by Brand:")
print(black_owned_revenue_brand)
print("Non-black-owned Revenue by Brand:")
print(non_black_owned_revenue_brand)

# Group by category for Black-owned products and sum the reviews
black_owned_reviews = black_owned.groupby('CATEGORY')['NUMBER_OF_REVIEWS'].sum().reset_index()

# Sort by the number of reviews (descending order)
black_owned_reviews = black_owned_reviews.sort_values(by='NUMBER_OF_REVIEWS', ascending=False)
print("Black-owned Reviews Sorted and Summed:")
print(black_owned_reviews)

# Group by Country and Brand for Black-owned companies, and calculate total revenue
black_owned_country_revenue = black_owned.groupby(['COUNTRY_OF_ORIGIN', 'BRAND'])['PRICE_USD'].sum().reset_index()

# Sort by Country of Origin alphabetically, and within each country by revenue in descending order
black_owned_country_revenue = black_owned_country_revenue.sort_values(by=['COUNTRY_OF_ORIGIN', 'PRICE_USD'], ascending=[True, False])

# Rename columns for clarity
black_owned_country_revenue.columns = ['COUNTRY_OF_ORIGIN', 'BRAND', 'TOTAL_REVENUE']

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
plt.figure(figsize=(14, 8))
plt.subplot(1, 2, 1)
plt.pie(
    top_black_owned['TOTAL_REVENUE'], 
    labels=top_black_owned['BRAND'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Blues(np.linspace(0.5, 1, len(top_black_owned)))
)
plt.title('Top Black-Owned Companies by Revenue')

# Pie chart for Non-Black-owned companies
plt.subplot(1, 2, 2)
plt.pie(
    top_non_black_owned['TOTAL_REVENUE'], 
    labels=top_non_black_owned['BRAND'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Oranges(np.linspace(0.5, 1, len(top_non_black_owned)))
)
plt.title('Top Non-Black-Owned Companies by Revenue')
plt.tight_layout()
plt.show()

# Horizontal Box Plot the most popular categories
plt.figure(figsize=(14, 10))
plt.barh(black_owned_reviews['CATEGORY'], black_owned_reviews['NUMBER_OF_REVIEWS'], color='blue')
plt.title('Most Popular Categories for Black-Owned Products (Based on Reviews)')
plt.xlabel('Number of Reviews')
plt.ylabel('Product Category')
plt.gca().invert_yaxis()  # Flip the y-axis for better readability
plt.show()

# Data for grouped bar chart 
top_countries = black_owned_country_revenue['COUNTRY_OF_ORIGIN'].unique()[:208]
filtered_data = black_owned_country_revenue[black_owned_country_revenue['COUNTRY_OF_ORIGIN'].isin(top_countries)]

# Grouped Bar Chart Plot
plt.figure(figsize=(18, 8))
for country in top_countries:
    country_data = filtered_data[filtered_data['COUNTRY_OF_ORIGIN'] == country]
    plt.bar(
        country_data['BRAND'], 
        country_data['TOTAL_REVENUE'], 
        label=country, alpha=1.0
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
