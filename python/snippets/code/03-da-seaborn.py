import matplotlib.pyplot as plt
import pandas as pd
import seaborn

INPUT_FILE = "./data/data-1.csv"


data = pd.read_csv(INPUT_FILE)

seaborn.relplot(x="id", y="score", data=data)
plt.show()

