import folium
import pandas

data = pandas.read_csv("3.1 Volcanoes.txt.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[30.58, -99.09])

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="hi i m a marker", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("index.html")


