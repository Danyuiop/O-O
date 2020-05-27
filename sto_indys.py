import csv
import random as rd
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt

style.use("fivethirtyeight")


# noinspection PyMissingOrEmptyDocstring


class Transport:
    def __init__(self, name, Speed, Power, Wheels):
        self.name = name
        self.Speed = Speed
        self.Power = Power
        self.Wheels = Wheels


# noinspection PyMissingOrEmptyDocstring
class hraf:
    Cars = Transport('Car', (rd.randint(1, 190)), (rd.randint(1, 250)), (rd.randint(4, 10)))
    Tales = Transport('Tales', (rd.randint(1, 300)), (rd.randint(1, 34)), (rd.randint(4, 10)))
    Buses = Transport('Buses', (rd.randint(1, 129)), (rd.randint(1, 123)), (rd.randint(2, 10)))
    Trucks = Transport('Trucks', (rd.randint(1, 7)), (rd.randint(1, 145)), (rd.randint(1, 10)))


# noinspection PyMissingOrEmptyDocstring
class VBN(hraf):
    # Car
    Pick_ups = Cars = Transport('Pick_ups', rd.randint(1, 190), rd.randint(1, 250), rd.randint(4, 10))
    Sport_Cars = Cars = Transport('Sport Car', rd.randint(1, 330), rd.randint(1, 250), rd.randint(4, 10))
    Estate_Cars = Cars = Transport('Estate Cars', rd.randint(1, 330), rd.randint(1, 250), rd.randint(4, 10))
    VANS = Cars = Transport("VANS", rd.randint(1, 359), rd.randint(1, 345),  rd.randint(4, 10))
    Convertible = Cars = Transport("Convertible", rd.randint(1, 359), rd.randint(1, 250), rd.randint(4, 10))
    # Bikes
    Pedal_bikes = Buses = Transport('Pedal bikes', rd.randint(1, 345), rd.randint(1, 567), rd.randint(2, 10))
    Motor_bikes = Buses = Transport('Motor bikes', rd.randint(1, 345), rd.randint(1, 567), rd.randint(2, 10))
    # Trucks
    Medium_trucks = Trucks = Transport('Medium_trucks', rd.randint(1, 348), rd.randint(1, 145), rd.randint(1, 10))
    Heavy_trucks = Trucks = Transport('Heavy_trucks', rd.randint(1, 300), rd.randint(1, 145), rd.randint(1, 10))


s = [hraf.Cars.Power, VBN.Pick_ups.Power, VBN.Sport_Cars.Power, VBN.Estate_Cars.Power, VBN.VANS.Power,
     VBN.Convertible.Power, VBN.Pedal_bikes.Power, VBN.Motor_bikes.Power, VBN.Medium_trucks.Power,
     VBN.Heavy_trucks.Power, hraf.Tales.Power, hraf.Buses.Power, hraf.Trucks.Power]
rt = [hraf.Cars.name, VBN.Pick_ups.name, VBN.Sport_Cars.name, VBN.Estate_Cars.name, VBN.VANS.name,
      VBN.Convertible.name, VBN.Pedal_bikes.name, VBN.Motor_bikes.name, VBN.Medium_trucks.name,
      VBN.Heavy_trucks.name, hraf.Tales.name, hraf.Buses.name, hraf.Trucks.name]
cols = ['darkorange', 'c', 'k', 'w', 'orange', 'maroon', 'tan', 'r', 'g', 'coral', 'olive', 'chartreuse', 'gold']

plt.pie(s, labels=rt, colors=cols, startangle=90, )

# plt.xlabel('x')
# plt.ylabel('y')
plt.title('Transport')
# plt.legend()
plt.show()

Name1 = ([hraf.Cars.name],
         [VBN.Pick_ups.name],
         [VBN.Sport_Cars.name],
         [VBN.Estate_Cars.name],
         [VBN.VANS.name],
         [VBN.Convertible.name],
         [VBN.Pedal_bikes.name],
         [VBN.Motor_bikes.name],
         [VBN.Medium_trucks.name],
         [VBN.Heavy_trucks.name],
         [hraf.Tales.name],
         [hraf.Buses.name],
         [hraf.Trucks.name])
Speed1 = ([hraf.Cars.Speed],
         [VBN.Pick_ups.Speed],
         [VBN.Sport_Cars.Speed],
         [VBN.Estate_Cars.Speed],
         [VBN.VANS.Speed],
         [VBN.Convertible.Speed],
         [VBN.Pedal_bikes.Speed],
         [VBN.Motor_bikes.Speed],
         [VBN.Medium_trucks.Speed],
         [VBN.Heavy_trucks.Speed],
         [hraf.Tales.Speed],
         [hraf.Buses.Speed],
         [hraf.Trucks.Speed])
Wheels1 = ([hraf.Cars.Wheels],
         [VBN.Pick_ups.Wheels],
         [VBN.Sport_Cars.Wheels],
         [VBN.Estate_Cars.Wheels],
         [VBN.VANS.Wheels],
         [VBN.Convertible.Wheels],
         [VBN.Pedal_bikes.Wheels],
         [VBN.Motor_bikes.Wheels],
         [VBN.Medium_trucks.Wheels],
         [VBN.Heavy_trucks.Wheels],
         [hraf.Tales.Wheels],
         [hraf.Buses.Wheels],
         [hraf.Trucks.Wheels])
vbo = 0
Name = Name1
Speed = Speed1
Wheels = Wheels1
with open('tecst1.csv', 'w', newline='') as csvfile:

    fisw = ['Number', 'Name', 'Speed', 'Wheels']

    ret = csv.DictWriter(csvfile, fieldnames=fisw)

    ret.writeheader()

    for vbsd in Name1:
        vbo += 1
        ret.writerow({'Number': vbo, 'Name': Name, 'Speed': Speed, 'Wheels': Wheels})
