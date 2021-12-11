# Author: Alexander Meldrum
from csv import DictReader
import matplotlib.pyplot as plot

cars = list(DictReader(open('cars.csv','r'),delimiter=';'))[1:]

# def compare_hp(row):
#     return float(row['Horsepower'])

# cars.sort(key=compare_hp)

# Lambda version:
cars.sort(key = lambda row: float(row['Horsepower']))


# cars_copy = cars.copy()
# for car in cars:
#     if float(car['Horsepower']) == 0.0:
#         cars_copy.remove(car)
# cars = cars_copy


# list comprehension
    # https://www.w3schools.com/python/python_lists_comprehension.asp
cars = [car for car in cars if float(car['Horsepower']) != 0.0]

# for car in cars:
#     print(car['Car'],car['Horsepower'])

horsepower = []
acceleration = []

for car in cars:
    horsepower.append(float(car['Horsepower']))
    acceleration.append(float(car['Acceleration']))

for i in range(len(horsepower)):
    print(horsepower[i], acceleration[i])

# plot
plot.scatter(horsepower,acceleration)
plot.show()