import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20 , 20, 200)
y = np.sin(x)
plt.plot(x, y, marker="o")
plt.show()

#%%
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [34, 56, 78, 21]
plt.plot(x, y)
plt.show()
