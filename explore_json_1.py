import json

in_file =open('eq_date_1_day_m1.json','r')

out_file = open('readable_eq_date.json','w')

eq_data = json.load(in_file)

json.dump(eq_data,out_file,indent=4)

list_of_eqs = eq_data['features']

print(type(list_of_eqs))

print(len(list_of_eqs))

mags,lons,lats = [],[],[]

for eq in list_of_eqs:
    mag= eq['properties']['mags']
    lon= eq['geometry']['coordinates'][0]
    lat= eq['geometry']['coordinates'][0]
    mags.append(mag)
    lons.append(lon)
    lats.append(lats)
    mags.append(mag)
    lons.append(lon)
    lats.append(lats)

print("Mags")
print(mags)
print(lons)
print("lats")
print(lat[:10])

#data = [Scattergeo(lon=lons,lats)]


data =[{
    'type':'scattergeo',
    'lon' :lons,
    'lats':lats,
    'marker': {
        'size':[5*mag for mag in mags],
    },

}]
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
my_layout = Layout(title='Global Earthquakes')

fig ={'data':data,'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')