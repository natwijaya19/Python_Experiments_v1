# %%============================================================================
my_string = "hello world"
capitalize_string = my_string.capitalize()
print(capitalize_string)


# %%============================================================================
class Person:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.capitalize()


if __name__ == "__main__":
    person = Person("john")
    print(person.name)

import matplotlib.pyplot as plt
# %%============================================================================
import numpy as np

start = -1000
stop = 1000
step = 1
my_range = np.arange(start=start, stop=stop, step=step)

# %%============================================================================
plt.plot(my_range, my_range ** 3)
plt.show()

# %%============================================================================
my_second_range = my_range.copy()
# %%============================================================================
my_range[0] = 100

# %%============================================================================
print(my_second_range[0])
print(my_range[0])
