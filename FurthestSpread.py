import pandas as pd

'''

given an output .csv of all franchises in a given state, return the one with the largest spread
-> Spread here is defined as the maximum area bounded by lat/long points of the outermost locations
   of a given franchise's cluster
   
   LEFTMOST, RIGHTMOST = min(longitude), max(longitude)
   TOPMOST, BOTTOMMOST = max(latitude), min(longitude)

df = (business_id, name, latitude, longitude) for each business in STATE where is_franchise > 0

'''

pwd = '...' # set the project working directory here
df = pd.DataFrame(pd.read_csv(f'{pwd}/temp_table_out.csv'), low_memory=False)

# sort by name
df.sort_values(by='name', inplace=True)
current_name = df.name.iloc[0]

max_spread = ['null', 0] # this will be [name, spread]
name_list = list(set([n for n in df.name]))

# LEFTMOST, RIGHTMOST = min(longitude), max(longitude)
# TOPMOST, BOTTOMMOST = max(latitude), min(longitude)

for business_name in name_list:
    df_l = df[df.name == business_name]
    for row in df_l.itertuples():

        LEFTMOST = 0
        RIGHTMOST = 0
        TOPMOST = 0
        BOTTOMMOST = 0

        lat = row.latitude
        long = row.longitude

        if long < LEFTMOST: LEFTMOST = lat
        elif long > RIGHTMOST: RIGHTMOST = long
        if lat > TOPMOST: TOPMOST = lat
        elif lat < BOTTOMMOST: BOTTOMMOST = lat

        horizontal = abs(RIGHTMOST - LEFTMOST)
        vertical = abs(TOPMOST - BOTTOMMOST)

        spread = horizontal * vertical

        if spread > max_spread[1]:
            max_spread = [row.name, spread]

# Just printing the name of business w/ max spread
# but you can do anything you want with this var
ret_business_name = max_spread[0]
print(ret_business_name)