import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

var1 = np.arange(0, 10, 0.5)
var2 = var1 * 2
print(var2)

var2_df = pd.DataFrame(var2)
var2_df.to_csv('var2.csv')
var2_df.plot.line()
plt.show()

# %%============================================================================
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 2])
s.plot.line()
plt.show()
