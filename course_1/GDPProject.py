import pandas as pd

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
gdp_world_data['1990-2019 GDP growth'] = gdp_world_data['2019'] - gdp_world_data['1990']
gdp_world_data['1990-2019 GDP % growth'] = round(100 * gdp_world_data['2019'] / gdp_world_data['1990'],2)
print(gdp_world_data.sort_values(by='1990-2019 GDP % growth',ascending = False))

### Delete columns, simplify
gdp_world_data = gdp_world_data.loc[:,['1990','2019','1990-2019 GDP growth','1990-2019 GDP % growth']]
### Rename columns
gdp_world_data.columns = ['1990','2019','Growth','%-growth']
#print(gdp_world_data.sort_values(by='%-growth',ascending = False))

### Drop N/A values
gdp_world_data = gdp_world_data.dropna()
print(gdp_world_data.sort_values(by='%-growth',ascending = False))