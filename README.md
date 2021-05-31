# Walmart Recruiting - Store Sales Forecasting:

![walmart](https://user-images.githubusercontent.com/45354762/120146953-83fcb800-c203-11eb-9fc7-2ea7c84889b2.png)

- Walmart has provided historical sales data for 45 Walmart stores located in different regions. Each store contains a number of departments, and task given is to predict the department-wide sales for each store.
- In addition, Walmart runs several promotional markdown events throughout the year. These markdowns precede prominent holidays, the four largest of which are the Super Bowl, Labor Day, Thanksgiving, and Christmas.
- The weeks including these holidays are weighted five times higher in the evaluation than non-holiday weeks. Part of the challenge presented by this competition is modeling the effects of markdowns on these holiday weeks in the absence of complete/ideal historical data.
- Kaggle-link to this problem can be found here.

#Data Field Information:
- stores.csv: This file contains anonymized information about the 45 stores, indicating the type and size of store.
- train.csv: This is the historical training data, which covers to 2010–02–05 to 2012–11–01. Within this file you will find the following fields
     - Store - the store number(45 stores)
     - Dept - the department number(99 departments) 
     - Date - the week Weekly Sales - sales for the given department in the given store 
     - IsHoliday - Whether the week is a special holiday week.
- test.csv: This fie is identical to train.csv, except we don't have the weekly sales. You must predict the sales for each triplet of store, department, and date in this file.
- features.csv: This file contains additional data related to the store, department, and regional activity for the given dates. It contains the following fields: 
      - Store - the store number 
      - Date - the week 
      - Temperature - average temperature in the region 
      - Fuel_Price - cost of fuel in the region 
      - MarkDown1–5 - anonymized data related to promotional markdowns that Walmart is running. Markdown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA. 
      - CPI - the consumer price index 
      - Unemployment - the unemployment rate 
      - IsHoliday - whether the week is a special holiday week

