import matplotlib.pyplot as plt
import pandas as pd


def draw_curve(dataset, label, x_label, y_label, color='red'):
    x = []
    y = []

    for i, value in dataset.items():
        x.append(i)
        y.append(int(value))
    plt.plot(x, y, color=color, label=label)
    plt.title(label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.legend()
    plt.show()


def draw_population_curve(file):
    population = pd.read_csv(file)
    population.sort_values(by='Population', ascending=False, inplace=True)
    population = population.reset_index()
    draw_curve(population.Population, 'Population', 'City_Index', 'Population')


def draw_loc_curve(file):
    code = pd.read_csv(file)
    code.sort_values(by='LOC', ascending=False, inplace=True)
    code = code.reset_index()
    draw_curve(code.LOC, 'LOC', 'Code_Index', 'LOC', color='blue')


if __name__ == '__main__':
    draw_population_curve('data/US-Population.csv')
    draw_loc_curve('detail.csv')
