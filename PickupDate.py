import pandas as pd

def CreatePickupDate(df):
	#formats long date string to just the time
	for date in df["Time"].values:
		try:
			stringIndex = str(date).index(":")
			index = df.loc[df["Time"] == date].index[0]
			if "Delivery" in str(df.at[index,"Order Type"]):
				df.loc[index, "Time"] = ""
				continue
			pickupTime = date[stringIndex - 2] + date[stringIndex - 1] + ":" + date[stringIndex + 1] + date[stringIndex + 2]
			df.loc[index, "Time"] = pickupTime

		except ValueError:
			pass
	return df

