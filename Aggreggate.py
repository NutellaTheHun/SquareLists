import csv
import numpy as np
import pandas as pd

def Aggregate():
	inputFile = 'output/FrontList.csv'
	df = pd.read_csv(inputFile)
	df = df[['Size','Item','Quantity']]
	df['Item'].replace('', np.nan, inplace=True)
	df.dropna(subset=['Item'], inplace=True)
	#print(df[['Size','Item','Quantity']])

	for item in df['Item'].values:
		#df.loc[df['Item'] == item].index[0]
		#index = 1
		product = item
		size = df.loc[index, 'Size']
		quantity = df.loc[index, 'Quantity']
		print(product + " " + str(size) + ":" + str(quantity))
		index += 1

Aggregate()
