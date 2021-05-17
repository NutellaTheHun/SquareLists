import csv
import pandas as pd
import numpy as np
from BackList import CreateBackList
from CookieBuilder import CookieBuilder
from FormatProductOptions import FormatProductOptions
from Frontlist import CreateFrontList
from Forecast import CreateForecast

inputfilename = 'input/input.csv'

backlistoutput = 'output/BackList.csv'


df = pd.read_csv(inputfilename, parse_dates=['Pickup Date'])

#formats the variation strings to proper sizes (5"/8"/10")
FormatProductOptions(df)
#formats the variation 6 cookies/scones and builds into individual lines
df = CookieBuilder(df)

#"Full Name" column and "Order Type" are also used in Frontlist.py and Forecast.py, and the column renames
df["Full Name"] = df["Shipping First Name"] + ' ' + df["Shipping Last Name"]
df["Order Type"] = np.where(pd.isnull(df["Shipping Address"]), '', np.where(df["Shipping Address"] == "285 Beacon St" , "Pickup", "Delivery"))
df = df.rename(columns={"Product Options": "Size", "Product Name": "Item", "Product Quantity" : "Quantity"})

CreateForecast(df)

CreateFrontList(df)

#make back list
#CreateBackList(df)

