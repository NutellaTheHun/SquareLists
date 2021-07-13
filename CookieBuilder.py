import pandas as pd

def CookieBuilder(df):
	for productId in df["Product Id"]:
		if productId == 43 or productId == 44 or productId == 82:
			index = df.loc[df['Product Id'] == productId].index[0]
			cookie = df.at[index,'Product Options']#not a cookie yet, still that garbage string in the value
			quantity = df.at[index,'Product Quantity']
			cookie = cookie.replace(' &amp;','')
			cookie = cookie.replace(': ',',')
			cookie = cookie.rsplit(',')

			cookieDict = dict()
			for i in range(2, len(cookie)):#sum up the cookies, odd indexs contain the names, starting at index 2 because 1 and 0 are garbage."Variation:","\lies(some dumb variation name in Squareup)"
				if i % 2 == 0:
					pass
				else:
					if cookie[i] in cookieDict:
						cookieDict[cookie[i]] = cookieDict[cookie[i]] + 1 * quantity
					else:
						cookieDict[cookie[i]] = 1 * quantity
			df = df.drop([index])
			for key in cookieDict:
				line = pd.DataFrame({'Product Name': str(key), 'Product Quantity': cookieDict[key]}, index=[index + .5])
				df = df.append(line, ignore_index=False)
				df = df.sort_index().reset_index(drop=True)		
	return df