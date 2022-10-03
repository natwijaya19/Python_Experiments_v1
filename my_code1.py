import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# %%============================================================================
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# %%============================================================================
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()

# %%============================================================================
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
plt.plot(t, s)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()

# %%============================================================================
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

# %%%============================================================================
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

# %%============================================================================
import pandas as pd

# import numpy as np

df = pd.DataFrame({
    'pig': [20, 18, 489, 675, 1776],
    'horse': [4, 25, 281, 600, 1900]
}, index=[1990, 1997, 2003, 2009, 2014])
lines = df.plot.line()
plt.show()

# %%============================================================================
axes = df.plot.line(subplots=True)
type(axes)
axes[0].set_ylabel('weight')
plt.show()

# %%============================================================================
# import scipy.stats as s
#
# s = pd.Series([1, 2, 2.5, 3, 3.5, 4, 5])
# ax = s.plot.kde()
# plt.show()
#

# %%============================================================================
df = pd.DataFrame({'mass': [0.330, 4.87, 5.97],
                   'radius': [2439.7, 6051.8, 6378.1]},
                  index=['Mercury', 'Venus', 'Earth'])
plot = df.plot.pie(y='mass', figsize=(5, 5))
plt.show()

# %%============================================================================
# import matplotlib.pyplot as plt
# plt.close("all")

plt.close("all")
plt.clf()

# %%============================================================================
import numpy as np
import matplotlib.pyplot as plt

low = -50
high = 55
size = 1000
rand_num = np.random.randint(low, high, size)
daily_ret = rand_num / 1000
cum_ret = np.cumprod(daily_ret + 1).transpose()
plt.plot(cum_ret)
plt.show()
