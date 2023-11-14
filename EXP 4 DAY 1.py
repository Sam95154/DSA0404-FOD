import pandas as pd
data = {'property_ID':[1,2,3,4,5],
        'location':["chennai","madurai","coimbatore","theni","madurai"],
        'number_of_bedrooms':[2,1,4,3,5],
        'area_in_sqft':[77,83,59,49,67],
        'listing_price':[40000,32000,13000,22000,53000]}
property_data = pd.DataFrame(data)
average_price = property_data.groupby("location")["listing_price"].mean()
prop = property_data[property_data["number_of_bedrooms"] > 4]
no_prop = len(prop)
print("1. Average Price of Each Location")
print(average_price)
print("2. No of Property morethan 4 BHK",no_prop)
prop_large = property_data.loc[property_data["area_in_sqft"].idxmax()]
print("3. Property With Largest Area")
print(prop_large)
