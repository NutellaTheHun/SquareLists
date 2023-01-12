import csv
import pandas as pd
import numpy as np
from CookieBuilder import CookieBuilder
from FormatProductOptions import FormatProductOptions
from Frontlist import CreateFrontList
from Forecast import CreateForecast
from Aggregate import PieAgg

pd.options.mode.chained_assignment = None

inputfilename = 'input/input.csv'

backlistoutput = 'output/BackList.csv'

df = pd.read_csv(inputfilename, parse_dates=['Pickup Date'])

#formats the variation 6 cookies/scones and builds into individual lines
df = CookieBuilder(df)

#formats the variation strings to proper sizes (5"/8"/10")
df = FormatProductOptions(df) #every item line needs a pickup date for forcaster! frontlist gets rid of it(pickupdate function)

#"Full Name" column and "Order Type" are also used in Frontlist.py and Forecast.py, and the column renames
df['Full Name'] = df['Shipping First Name'] + ' ' + df['Shipping Last Name']

#Determine Pickup or Delivery
df["Order Type"] = np.where(pd.isnull(df["Shipping Address"]), '', 
	np.where(df["Shipping Address"] == "285 Beacon St" , "Pickup", "Delivery"))

df = df.rename(columns={
	"Product Options": "Size", 
	"Product Name": "Item", 
	"Product Quantity" : "Quantity", 
	"Fulfillment Time": "Time"
	})

CreateForecast(df)

CreateFrontList(df)

PieAgg()
