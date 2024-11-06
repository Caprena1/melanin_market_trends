import pandas as pd

extended_cosmetics_df = pd.read_csv('extended_cosmetics_products.csv')
beauty_products_df = pd.read_csv('beauty_products.csv')

print(extended_cosmetics_df)

extended_cosmetics_df.head(10)