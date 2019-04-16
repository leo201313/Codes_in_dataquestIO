## 1. Geographic Data ##

import pandas as pd
airlines = pd.read_csv("airlines.csv")
airports = pd.read_csv("airports.csv")
routes = pd.read_csv("routes.csv")
al_first = airlines.iloc[0]
ap_first = airlines.iloc[0]
ro_first = airlines.iloc[0]

print(al_first)
print(ap_first)
print(ro_first)

## 4. Workflow With Basemap ##

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
m = Basemap(projection="merc",llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180)

## 5. Converting From Spherical to Cartesian Coordinates ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()

x,y = m(longitudes,latitudes)


## 6. Generating A Scatter Plot ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)

m.scatter(x,y,s=1)
plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 8. Customizing The Plot Using Matplotlib ##

fig,ax = plt.subplots(figsize=(15,20))
ax.set_title("Scaled Up Earth With Coastlines")
# Add code here, before creating the Basemap instance.
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 9. Introduction to Great Circles ##

geo_routes = pd.read_csv("geo_routes.csv")
geo_routes.info()
print(geo_routes[:5])

## 10. Displaying Great Circles ##

fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

# Start writing your solution below this line

def create_great_circles(df):
    for index,row in df.iterrows():
        if ((row["end_lat"] - row["start_lat"] )< 180) and ((row["end_lon"] - row["start_lon"])<180):
            m.drawgreatcircle(row["start_lon"],row["start_lat"],
                              row["end_lon"],row["end_lat"])
            
dfw = geo_routes.loc[geo_routes["source"]=="DFW",:]
create_great_circles(dfw)

plt.show()
            