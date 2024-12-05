#Melanin Market Trends:
*A data analysis project researching the most popular hair and skin products on the market especially for women of color.*
As a Data Analyst, I have been recently hired to work for a hair and skin products manufacturer that deals specifically with beauty products for women of color. I have been tasks with researching beauty trends and determining what brands and types of products are most popular and have the most sales.  
![images/three_brown_ladies.jpeg](https://github.com/Caprena1/melanin_market_trends/blob/main/images/three_brown_ladies.jpeg)

##Essential Questions

1. What are the top-selling hair and skin products and brands within Black beauty?
2. Which brands have the highest customer ratings and reviews?
3. Which specific product types are the most popular?
4. What are the revenue differences between black and non-black products?

##Gathering the Data
The data used in this project came from these resources:
1. extended_cosmetics_products.csv
2. beauty_products.csv


##How to Run the Project
The project was created as a Python program using a virtual environment in Visual Studio Code. The project file, beauty.py, can be run with these steps:
  Setup Virtual Environment 
    For a Mac user:
      1. cd melanin_market_trends_capstone
      2. python3 -m venv venv
      3. source venv/bin/activate
      4. python -m pop install -r requirements.txt

    
  Windows:
    1. venv\Scripts\activate
    2.  Then install the packages listed in the requirements.txt file:
        pip install -r requirements.txt    

To leave this virtual environment after you've examined the project run:
    deactivate    

##Elements Included to Meet Capstone Requirements
Data Analysis Implementation:
Developed a data analysis program utilizing pandas, matplotlib, and numpy. Executed an analysis project on 2 or more data pieces and produce comprehensive data visualizations using Matplotlib.

1. Loading Data:
    Read TWO csv data files
2. Clean and operate on the data while combining them.
    Cleaned data and performed a pandas merge with both data sets. Calculated new values based on the new data set. 
      A. First, I had to remove title from the extended_cosmetics_products.csv so that headings would pull in on the first line. 
      B. Before I can do a merge or join on 'Brand', I need to clean up data to make sure it's a one-to-one vs. a many-to-many. So I need to make sure the brand names on each list are unique.
      C. Remove duplicates under product_name. 
3. Made 4 matplotlib visualizations to display my data and tell a story:
      A. BAR PLOT - This plot shows the total revenue generated by Black-owned versus Non-Black-owned companies. It helps highlight the financial impact and scale of each group.
      B. PIE PLOT - This chart visually emphasizes the top 20 companies categorized by brand that produces the most revenue. The blue pie represents black-owned companies, and the orange pie represents non-black-owned companies.
      C. HORIZONTAL BAR PLOT - This plot reveals: The product categories that attract the most customer attention, the relative popularity of categories among Black-owned brands, and the trends that could help businesses focus on high-engagement categories.
      D. GROUPED BAR CHART - This visualization highlights which black_owned companies produce the most revenue from greatest to least and sorts them by country. Added image inside plot.

      ![brown_faces](https://github.com/user-attachments/assets/94011a9d-f4fc-43b8-aaa9-2bfc194366fd)




