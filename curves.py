import matplotlib.pyplot as plt
import pandas as pd
import powerlaw


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


def draw_pdf(dataset, x_label):
    fig, ax = plt.subplots()

    figPDF = powerlaw.plot_pdf(dataset, ax, color='b')
    powerlaw.plot_pdf(dataset, linear_bins=True, color='r', ax=figPDF)

    figPDF.set_title(x_label + ' PDF')
    figPDF.set_xlabel(x_label)
    figPDF.set_ylabel("p(X)")
    figname = 'FigPDF'
    fig.show()


def draw_ccdf(dataset, x_label):
    fit = powerlaw.Fit(dataset, discrete=True)

    fig, ax = plt.subplots()

    figCCDF = fit.plot_pdf(ax, color='b', linewidth=2)
    fit.power_law.plot_pdf(color='b', linestyle='--', ax=figCCDF)
    fit.plot_ccdf(color='r', linewidth=2, ax=figCCDF)
    fit.power_law.plot_ccdf(color='r', linestyle='--', ax=figCCDF)

    figCCDF.set_title(x_label + ' CCDF')
    figCCDF.set_xlabel(x_label)
    figCCDF.set_ylabel(u"p(X),  p(X≥x)")

    figname = 'FigCCDF'
    fig.show()


def draw_population(file):
    population = pd.read_csv(file)
    population.sort_values(by='Population', ascending=False, inplace=True)
    population = population.reset_index()
    draw_pdf(population.Population, 'Population')
    draw_ccdf(population.Population, 'Population')


def draw_loc(file):
    code = pd.read_csv(file)
    code.sort_values(by='LOC', ascending=False, inplace=True)
    code = code.reset_index()
    draw_pdf(code.LOC, 'LOC')
    draw_ccdf(code.LOC, 'LOC')


if __name__ == '__main__':
    draw_population_curve('data/US-Population.csv')
    draw_loc_curve('data/software-detail.csv')

    draw_population('data/US-Population-Coordinate.csv')
    # 'data/US-Population-Coordinate.csv' 'data/China-Population-Coordinate.csv'

    draw_loc('data/software-detail.csv')
