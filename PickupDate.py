import pandas as pd

def CreatePickupDate(df):
	#formats long date string to just the time
	for date in df["Fulfillment Time"].values:
		try:
			stringIndex = str(date).index(":")
			index = df.loc[df["Fulfillment Time"] == date].index[0]
			pickupTime = date[stringIndex - 2] + date[stringIndex - 1] + ":" + date[stringIndex + 1] + date[stringIndex + 2]
			df.loc[index, "Fulfillment Time"] = pickupTime

		except ValueError:
			pass
	return df

