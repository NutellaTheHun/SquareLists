import csv
import datetime
import pandas as pd
import numpy as np

def CreateFrontList(df):
	tomorrow = datetime.date.today() + datetime.timedelta(days=1)
	frontlistoutput = 'output/FrontList.csv'
	df['Pickup Time'] = df['Pickup Time'].loc[df['Pickup Time'].shift(1) != df['Pickup Time']]
	df['Pickup Time'] = df['Pickup Time'].shift(-1)

	#filter by tomorrow
	#df["Pickup Date"] = pd.to_datetime(df["Pickup Date"], format='%m/%d/%Y')
	#df = df.loc[df['Pickup Date'] == tomorrow]

	#filter by specific day, not done yet
	#df["Pickup Date"] = pd.to_datetime(df["Pickup Date"], format='%m/%d/%Y')
	#df = df.loc[df['Pickup Date'] == tomorrow]

	for value in df["Order Notes"].values:
		if value != "":
			index = df.loc[df['Order Notes'] == value].index
			#df.loc[index, 'Item'] = "CHECK NOTES"
			orderType = df.loc[index, 'Order Type']
			if "Pickup" in str(orderType):
				df.loc[index, 'Item'] = "CHECK NOTES"

	frontlist = df[["Full Name","Pickup Time", "Order Type", "Size", "Item", "Quantity"]]
	frontlist.to_csv(frontlistoutput, index=False)
