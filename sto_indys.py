import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Transport:
    def __init__(self, name, Speed, Power, Wheels):
        self.name = name
        self.Speed = Speed
        self.Power = Power
        self.Wheels = Wheels


class hraf:
    Cars = Transport("Car", 218, 249, 4)
    Tales = Transport("Tales", 300, 34, 4)
    Buses = Transport("Buses", 129, 123, 2)
    Trucks = Transport("Trucks", 70, 145, 4)


class Graf:
    slices = [hraf.Cars.Power, hraf.Tales.Power, hraf.Buses.Power, hraf.Trucks.Power]
    activities = [hraf.Cars.name, hraf.Tales.name, hraf.Buses.name, hraf.Trucks.name]
    cols = ['c', 'm', 'r', 'b']

    plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow=True,
            explode=(0, 0, 0, 0),
            autopct='%1.1f%%')
    plt.title('Transport')
    plt.show()


class ERT:
    Graf()
    CAA = 'CVS.xlsx'
    CAA2 = 'CVS2.xlsx'

    df = pd.read_excel(CAA)

    values = df[['Transport', 'Wheels']]

    ax = values.plot.bar(x="Transport", y='Wheels', rot=0)

    plt.show()


ERT()
