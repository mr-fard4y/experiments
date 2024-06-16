import matplotlib.pyplot as plt
import numpy as np

BEG_DATA = 0
END_DATA = 50
POINTS_COUNT = 200


x_data = np.linspace(BEG_DATA, END_DATA, POINTS_COUNT)
y_data = np.cos(x_data)

figure, ax_obj = plt.subplots()
ax_obj.plot(x_data, y_data)

ax_obj.set_title("Cos plot")
ax_obj.set_xlabel("X axes")
ax_obj.set_ylabel("Y axes")

plt.show()

