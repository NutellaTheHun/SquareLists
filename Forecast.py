import csv
import numpy as np

def CreateForecast(df):
	#fills empty values in the selected columns with orders information for proper filtering for forcasting
	df['Pickup Date'].fillna(method='bfill', inplace=True)

	#Makes the empty spaces have NaN so fillna will work in next line
	df[df[['Full Name','Status','Order Type', 'Shipping First Name', 'Shipping Last Name', 
	'Shipping Address', 'Shipping Postal Code', 'Shipping City', 'Shipping Region']]==""] = np.NaN
	
	temp = df['Item']
	sizeTemp = df['Size']
	df = df.fillna(method='ffill')
	df['Item'] = temp
	df['Size'] = sizeTemp

	#produces the forcast csv, "Full Name" column and "Order Type" are also used in the frontlist, and the column renames!
	forcaster = df[['Order #', 'Status', 'Pickup Date','Full Name', 'Order Type', 'Size', 'Item', 'Quantity']]

	
	forcaster.to_csv("output/forcast.csv", index = False)
	
	