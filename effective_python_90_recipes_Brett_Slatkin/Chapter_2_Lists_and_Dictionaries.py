#%% Chapter_2_Lists_and_Dictionaries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns   


#%% Item 11: Know How to Slice Sequences
a = 1

#%% Item 12: Avoid Striding and Slicing in a Single Expression
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = x[::2]
z = y[1:-1]
print(y)
print(z)


#%% Prefer catch-all unpacking over slicing
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second, *others = car_ages_descending
print(oldest, second, others)

oldest, *others, youngest = car_ages_descending
print(oldest, others, youngest)


