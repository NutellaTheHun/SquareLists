import pandas as pd

def FormatProductOptions(df):

	for item in df["Product Options"].values:
		if "Add a handmade note card by local artist Sarah Dudek" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			df.loc[index, 'Product Name'] = "(Gift) " + df.loc[index, 'Product Name']
		if "Scone" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			flavor = item.replace("Variation : Regular, Choose Scone Flavor : ","") + " Scone"
			df.loc[index, 'Product Name'] = flavor
		if "Small" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			df.loc[index, 'Product Options'] = "5\""
		if "Medium" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			df.loc[index, 'Product Options'] = "8\""
		if "Large" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			df.loc[index, 'Product Options'] = "10\""
		if "Variation : Regular, Choose Cookie Flavors" in str(item):
			pass
		elif "Regular" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			df.loc[index, 'Product Options'] = ""

