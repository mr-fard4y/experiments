from random import randint

import numpy as np

data = list(range(1, 11))
array = np.array(data)
array_m5 = array * 5

print(f"Array: {array}")
print(f"Array mult by 5: {array_m5}")


array_sqr3 = array ** 3
array_sin = np.sin(array)
print(f"Array squared-3: {array_sqr3}")
print(f"Array sine vals: {array_sin}")


data = [[randint(10, 50) for jdx in range(5)] for idx in range(3)]
array_2d = np.array(data)
sub_array = array_2d[:2, 2:]
print(f"Array 2d:\n {array_2d}")
print(f"Sub-array 2d:\n {sub_array}")

