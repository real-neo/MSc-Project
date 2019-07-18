# file = open('/Users/neo/population-file.csv')
# write_file = open('/Users/neo/transformed.csv', mode="w")
# while True:
#     line = file.readline()
#     if not line:
#         break
#     line_arr = line.strip().split(',')
#     write_file.write("[\""+line_arr[0] + "\",\"" + line_arr[1] + "\",\"" + line_arr[2] + "\",\"" + line_arr[3] + "\",\"" + line_arr[4] + "\"],\n")
# file.close()
# write_file.close()


import pandas as pd
import numpy as np


def merge_sort(df0, df1):
    size0 = len(df0.index)
    size1 = len(df1.index)

    result = pd.DataFrame(columns=['City', 'Population', 'File', 'Size', 'LOC'])

    for index1, row1 in df1.iterrows():
        index0 = int(index1 / size1 * size0)
        # print(df0.iloc[index0].City, df0.iloc[index0].Population, row1.File, row1.Size, row1.LOC)
        new_line = pd.Series([df0.iloc[index0].City, df0.iloc[index0].Population, row1.File, row1.Size, row1.LOC],
                             index=result.columns)
        result = result.append(new_line, ignore_index=True)

    return result


df = pd.read_csv('/Users/neo/population-code.csv')

dfs = np.split(df, [2], axis=1)
population = dfs[0].copy()
code = dfs[1].dropna().copy()

size_p = len(population.index)
size_c = len(code.index)

if size_p == size_c:
    pass
else:
    df = merge_sort(population, code)

print(df)
df.to_csv('/Users/neo/result2.csv', index=False)
