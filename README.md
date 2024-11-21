#Melanin Market Trends:
*A data analysis project esearching the most popular hair and skin products on the market especially for women of color.*
As a Data Analyst, I have been recently hired to working for a hair and skin products manufacturer that deals specifically with beauty products for women of color. I have been tasks with researching beauty trends and determining what brands and types of products are most popular and have the most sales.  
![black_face_animated](https://github.com/user-attachments/assets/1bdf2cd6-245e-4ada-98c2-9f4a3a9c5679)

##Essential Questions

1. What are the top-selling hair and skin products and brands within Black beauty?
2. Which brands have the highest customer ratings and reviews?
3. Which specific product types are the most popular?

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
3. Made 3 matplotlib visualizations to display my data 


