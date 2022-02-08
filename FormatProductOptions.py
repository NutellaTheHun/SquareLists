import pandas as pd

def FormatProductOptions(df):
	for item in df["Product Options"].values:
		if "Pint of Vanilla Bean Horchata" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			pickup = df.at[index, 'Pickup Date']
			line = pd.DataFrame({'Product Name': "Vanilla Bean Horchata", 'Product Quantity': 1, 'Pickup Date': pickup}, index=[index + .5])
			df = df.append(line, ignore_index=False)
			df = df.sort_index().reset_index(drop=True)	
		if "Pint of Pistachio Amaretto" in str(item):
			index = df.loc[df['Product Options'] == item].index[0]
			pickup = df.at[index, 'Pickup Date']
			line = pd.DataFrame({'Product Name': "Pistachio Amaretto", 'Product Quantity': 1, 'Pickup Date': pickup}, index=[index + .5])
			df = df.append(line, ignore_index=False)
			df = df.sort_index().reset_index(drop=True)		
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
	return df

