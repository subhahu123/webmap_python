import folium
import pandas

data = pandas.read_csv("3.1 Volcanoes.txt.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[30.58, -99.09])

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("index.html")


