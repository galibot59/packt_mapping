import folium

map = folium.Map(location=[38.58,-99.09],zoom_start=6)

fg = folium.FeatureGroup(
    name="My Map"
)
for coordinate in  [[38.2,-99.1],[39.2,-99.1]]:
    fg.add_child(folium.Marker(location=coordinate,popup="I am an Marker",icon=folium.Icon(
        color="green"
    )))

map.add_child(fg)
map.save("Map1.html")