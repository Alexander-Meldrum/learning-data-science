import pandas as pd
### Series is the data structure for a single column of a DataFrame, not only conceptually, 
### but literally, i.e. the data in a DataFrame is actually stored in memory as a collection of Series

# data = {
#     'City': ['Paris', 'Oslo','Athens','London'],
#     'Population': [2248271,1019531,664046,8908081],
#     'Year': [2020,2020,2012,2018]
# }

# df = pd.DataFrame(data)
# print(df)


### Define Index:
data = {
    'Population': [2248271,1019531,664046,8908081],
    'Year': [2020,2020,2012,2018]
}

df = pd.DataFrame(data, index=['Paris', 'Oslo','Athens','London'])

print(df)
print('-----')
print(df.iloc[3])
#print(df.loc['London'])

### Adding Columns to DF
df['Country'] = ['France','Norway','Greece','England']
df['Growth'] = [213,545454,432,-213]
print(df)

### Math on columns:
df['New population'] = df['Population'] + df['Growth']
print(df)
### Replace column
df['Population'] = df['Population'] + df['Growth']
print(df)