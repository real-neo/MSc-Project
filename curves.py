import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/neo/population-code.csv')
dfs = np.split(df, [2], axis=1)
population = dfs[0].copy()
# population.sort_values(by='Population', ascending=False, inplace=True)
code = dfs[1].dropna().copy()
code.sort_values(by='LOC', ascending=False, inplace=True)
code = code.reset_index()

x = []
y = []
x_code = []
y_code = []

for i, row in population.iterrows():
    x.append(i)
    y.append(int(row.Population))
plt.plot(x, y, color='red', label='Population')
plt.title("Population")
plt.xlabel("City_Index")
plt.ylabel("Population")

# for i, row in code.iterrows():
#     x_code.append(i)
#     y_code.append(int(row.LOC))
# plt.plot(x_code, y_code, color='blue', label='LOC')
# plt.title("Code")
# plt.xlabel("Code_Index")
# plt.ylabel("LOC")

# plt.rcParams['font.sans-serif'] = ['SimHei']

# plt.legend()

plt.show()
