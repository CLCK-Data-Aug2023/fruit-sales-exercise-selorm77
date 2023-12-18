# add your code here
import pandas as pd
df_fruitsales = pd.DataFrame(columns=["Apples", "Bananas"])
df_fruitsales
# new sales data for the periods specified
sales = pd.DataFrame({"Apples": [35, 41], "Bananas": [21, 34]}, index=["2017 Sales", "2018 Sales"])
df_sales = pd.DataFrame(sales)
df_sales
df_sales.to_csv("fruits.csv")