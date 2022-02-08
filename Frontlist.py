import csv
import datetime
import pandas as pd
import numpy as np
import datetime
from PickupDate import CreatePickupDate

def CreateFrontList(df):
	date = input("Enter a date mm/dd/yyyy:  ")
	#for next day pull(old)
	#tomorrow = datetime.date.today() + datetime.timedelta(days=1)

	#for testing specific days, and now normal operations
	tomorrow = datetime.datetime.strptime(date, '%m/%d/%Y') # not "tomorrow" any more

	frontlistoutput = 'output/FrontList.csv'
	df['Fulfillment Time'] = df['Fulfillment Time'].loc[df['Fulfillment Time'].shift(1) != df['Fulfillment Time']]
	df['Fulfillment Time'] = df['Fulfillment Time'].shift(-1)

	#filter by tomorrow
	df["Pickup Date"] = pd.to_datetime(df["Pickup Date"], format='%m/%d/%Y')
	df = df.loc[df['Pickup Date'] == tomorrow]

	for value in df["Order Notes"].values:
		if value != "":
			index = df.loc[df['Order Notes'] == value].index
			orderType = df.loc[index, 'Order Type']
			if "Pickup" in str(orderType):
				df.loc[index, 'Item'] = "CHECK NOTES"

	CreatePickupDate(df)

	frontlist = df[["Full Name","Fulfillment Time", "Order Type", "Size", "Item", "Quantity"]]

	frontlist.to_csv(frontlistoutput, index=False)
