import csv
import numpy as np
import pandas as pd

def PieAgg():
	inputFile = 'output/FrontList.csv'
	output = 'output/Aggregate.csv'

	df = pd.read_csv(inputFile)
	df = df[['Size','Item','Quantity']]

	df['Item'].replace('', np.nan, inplace=True)
	df.dropna(subset=['Item'], inplace=True)
	df['Size'].replace(np.nan ,'0', inplace=True)#add 0 to blank sizes for items created from cookiebuilder, required for proper count for groupby line
	df['Item'] = df['Item'].str.replace('\(Gift\)', '')#removes (Gift) tag for proper summation

	df = df.groupby(['Size','Item'])['Quantity'].agg('sum').reset_index()
	df['Size'].replace('0',np.nan, inplace=True)# 0 removed for visual appearance

	df.to_csv(output, index=False)

