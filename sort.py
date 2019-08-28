import pandas as pd


def remove_useless_data(file) -> pd.DataFrame:
    original = pd.read_csv(file)

    new = pd.DataFrame(columns=['City', 'Population'])

    for index, row in original.iterrows():
        try:
            new_line = pd.Series([str(row.City), int(row.Population)], index=new.columns)
            new = new.append(new_line, ignore_index=True)
        except ValueError as e:
            pass

    return new


if __name__ == '__main__':
    result = remove_useless_data('/Users/neo/Downloads/test.csv')
    result.to_csv('data/US-Population.csv', index=False)
