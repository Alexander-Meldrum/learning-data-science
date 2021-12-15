import pandas as pd
import geopandas
import matplotlib.pyplot as plt

### Load the data from CSV and set index ###
gdp_world_data = pd.read_csv('gdp_world_data.csv', index_col=0)
#pd.set_option('display.max_columns',50)
#print(gdp_world_data)


### Set index to country names ###
gdp_world_data = gdp_world_data.set_index('Country (or dependent territory)')
#print(gdp_world_data)
### Print only top: 
# print(gdp_world_data.head())

### Print Only "Albania"
#print(gdp_world_data.loc['Albania'])

### Sort by # GDP growth
gdp_world_data['2000-2019 GDP growth'] = gdp_world_data['2019'] - gdp_world_data['2000']
gdp_world_data['2000-2019 GDP % growth'] = round(100 * gdp_world_data['2019'] / gdp_world_data['2000'],2)
print(gdp_world_data.sort_values(by='2000-2019 GDP % growth',ascending = False))

### Delete columns, simplify
gdp_world_data = gdp_world_data.loc[:,['2000','2019','2000-2019 GDP growth','2000-2019 GDP % growth']]
### Rename columns
gdp_world_data.columns = ['2000','2019','Growth','%-growth']
#print(gdp_world_data.sort_values(by='%-growth',ascending = False))

### Drop N/A values
gdp_world_data = gdp_world_data.dropna()
print(gdp_world_data.sort_values(by='%-growth',ascending = False))

### Join data 
# This is the world map data
map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
map = map.set_index('name')
# Clean index difference between the two data sets
index_change = {
    'United States of America': 'United States',
    'Central African Rep.': 'Central African Republic',
    'Dem. Rep. Congo': 'Democratic Republic of the Congo',
    'Dominican Rep.': 'Dominican Republic',
    'Eq. Guinea': 'Equatorial Guinea',
    'Solomon Is.': 'Solomon Islands'
}
map = map.rename(index=index_change)
# default join is "left"
joint_data = map.join(gdp_world_data, how='outer')
# Change print size in terminal
pd.set_option('display.width',1000)
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',1000)
print(joint_data)

### Visualize the data
# This works because it's a geopandas object
joint_data.plot('%-growth',legend = True, figsize = (12,4))
plt.title('GDP Growth %, 2000-2019')
plt.savefig("growth_map.png")

joint_data['Growth per Capita'] = joint_data['Growth'] / joint_data['pop_est']
joint_data.plot('Growth per Capita', legend = True, figsize = (12,4))
plt.title('GDP Growth % per capita, 2000-2019')
plt.savefig("growth_per_capita_map.png")