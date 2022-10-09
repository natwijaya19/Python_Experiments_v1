import matplotlib.pyplot as plt
import numpy as np

low = -40
high = 45
size = 1 * 10 ** 3
rand_num = np.random.randint(low, high, size)
daily_ret = rand_num / 1000
cum_ret = np.cumprod(daily_ret + 1).transpose()
plt.plot(cum_ret)
plt.show()
