import folium
map = folium.Map(location=[30.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="hi i m a marker", icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("index.html")
