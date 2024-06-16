import pandas as pd

INPUT_FILE = "./data/data.csv"


data = pd.read_csv(INPUT_FILE)
print(data.head())

d_m_50 = data[data["score"] > 50]
d_m_50["average"] = (d_m_50["score"] + d_m_50["time"]) / 2
d_m_50.to_csv("filtered_data.csv", index=False)

