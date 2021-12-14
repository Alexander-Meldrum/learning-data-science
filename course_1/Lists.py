# https://stackoverflow.com/questions/509211/understanding-slice-notation

from csv import reader

with open('cars.csv', 'r') as f:
    csv_reader = reader(f, delimiter=';')
    cars = list(csv_reader)

cars = cars[2:]

for car in cars:
    car[4] = float(car[4])

### Sort by horsepower
### Normal sort
# def item_5(row):
#     return row[4]
# cars.sort(key=item_5)

### Lambda Sort
cars.sort(key= lambda row: row[4])


# for car in cars:
#     print(car)


### Slicing
# for car in cars[-1:-11:-1]:
#     print(car)

### List objects
    # Changing top level items [0] is different from chaning for example [0][0]

cars_view = cars[-1:-11:-1]
cars_view[0][0] = 'FORD'

for car in cars:
    print(car)