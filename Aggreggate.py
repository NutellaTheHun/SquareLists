import csv
import numpy as np

def Aggregate():
	inputFile = 'output/FrontList.csv'
	df = pd.read_csv(inputFile)
	
	for item in df["Product Name"].values:
		
