# import libraries
import folium
import pandas as pd
from bottle import route, run
from bottle import static_file
import petl as etl
table2 = etl.fromcsv('new.csv')
# Make a data frame with dots to show on the map
data = pd.DataFrame({
    'lat': [-25.274398, 20.593684, 30.375321, 35.86166, 32.427908, 50.503887, -14.235004, 56.130366,6.428055,19.2823,37.09024,33.886917,47.516231,33.93911,38.963745],
    'lon': [133.775136, 78.96288, 69.345116, 104.195397, 53.688046, 4.469936, -51.92528, -106.346771,-9.429499,166.6470,-95.712891,9.537499,14.550072,67.709953,35.243322],
    'name':  ["Australia", "India" , "Pakistan", "China", "Iran" ,"Belgium","Brazil","Canada","Liberia","United States Virgin Islands",
             "United States", "Tanzania", "Austria","Afghanistan","Turkey" ],
})
data
# Make an empty map
m = folium.Map(location=[20, 0], zoom_start=3.5)
m = folium.Map(location=[48.85, 2.35], tiles="OpenStreetMap", zoom_start=2)
s = 'Name: ' + data.iloc[0]['name']
# I can add marker one by one on the map
j = 1
for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup = table2[j]).add_to(m)
    j = j + 1

# Save it as html
m.save('312_markers_on_folium_map1.html')
print ("Forming HTML File...............")
print("Check File In Directory")
@route('/static/<312_markers_on_folium_map1.html>')
def server_static(filename):
    return static_file(filename, root='D:\Python\Data Integration\312_markers_on_folium_map1.html')
