import pandas as pd

min_wages = pd.read_csv('min_wages.csv', index_col=0)
min_wages = min_wages.set_index('Country')
min_wages = min_wages.loc[:,['Workweek (hours)[2]','Nominal hourly (US$)[6]']]
min_wages.columns = ['Hours/week','US$/hour']

# Change print size in terminal
pd.set_option('display.width',1000)
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',1000)
print(min_wages)