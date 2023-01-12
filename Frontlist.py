import csv
import datetime
import pandas as pd
import numpy as np
import datetime
from PickupDate import CreatePickupDate

def CreateFrontList(df):
	date = input("Enter a date mm/dd/yyyy:  ")
	frontlistoutput = 'output/FrontList.csv'

	#for next day pull(old)
	#tomorrow = datetime.date.today() + datetime.timedelta(days=1)

	#for testing specific days, and now normal operations
	userDate = datetime.datetime.strptime(date, '%m/%d/%Y')

	#df['Full Name'] = df['Full Name'].fillna(method='ffill')

	df['Time'] = df['Time'].loc[df['Time'].shift(1) != df['Time']]
	df['Time'] = df['Time'].shift(-1)

	#df['Time'] = df['Time'].fillna(method='ffill')
	#df['Full Name'] = df['Full Name'].loc[df['Full Name'].shift(1) != df['Full Name']]
	#df['Full Name'] = df['Full Name'].shift(-1)

	#filter by tomorrow
	df["Pickup Date"] = pd.to_datetime(df["Pickup Date"], format='%m/%d/%Y')
	df = df.loc[df['Pickup Date'] == userDate]
	for value in df["Order Notes"].values:
		if value != "":
			index = df.loc[df['Order Notes'] == value].index
			orderType = df.loc[index, 'Order Type']
			if "Pickup" in str(orderType):
				df.at[index, 'Item'] = "CHECK NOTES" ##SET COPY WARNING

	CreatePickupDate(df) ## Set COPY WARNING

	frontlist = df[["Full Name","Time", "Order Type", "Size", "Item", "Quantity"]]

	frontlist.to_csv(frontlistoutput, index=False)
