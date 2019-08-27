import matplotlib.pyplot as plt
import pandas as pd
import powerlaw


def create_mapping(population, code) -> pd.DataFrame:
    size_population = len(population.index)
    size_code = len(code.index)

    result = pd.DataFrame(columns=['City', 'Population', 'Latitude', 'Longitude', 'File', 'Size', 'LOC'])

    for code_index, code_row in code.iterrows():
        index0 = int(code_index / size_code * size_population)
        new_line = pd.Series([population.iloc[index0].City, population.iloc[index0].Population,
                              population.iloc[index0].Latitude, population.iloc[index0].Longitude,
                              code_row.File, code_row.Size, code_row.LOC], index=result.columns)
        result = result.append(new_line, ignore_index=True)

    return result


def power_law(dataset):
    fit = powerlaw.Fit(dataset, discrete=True)

    print('xmin =', fit.xmin)
    print('alpha =', fit.power_law.alpha)
    print('sigma =', fit.power_law.sigma)
    print('D =', fit.power_law.D)

    R1, p1 = fit.distribution_compare('power_law', 'exponential')
    R2, p2 = fit.distribution_compare('power_law', 'lognormal')
    R21, p21 = fit.distribution_compare('lognormal', 'exponential')
    R3, p3 = fit.distribution_compare('power_law', 'stretched_exponential')
    R4, p4 = fit.distribution_compare('power_law', 'truncated_power_law')
    R5, p5 = fit.distribution_compare('exponential', 'truncated_power_law')

    print('power_law vs. exponential', R1, p1)
    print('power_law vs. lognormal', R2, p2)
    print('lognormal vs. exponential', R21, p21)
    print('power_law vs. stretched_exponential', R3, p3)
    print('power_law vs. truncated_power_law', R4, p4)
    print('exponential vs. truncated_power_law', R5, p5)

    # Code LOC
    # xmin = 197.0
    # alpha = 2.671186377598983
    # sigma = 0.21574923362831866
    # D = 0.06585740668136375
    # power_law vs. exponential 3.5140446966013714 0.33527740656366367
    # power_law vs. lognormal -0.49863380141864244 0.5076468856854401
    # lognormal vs. exponential 4.012678498020013 0.17159340213833318
    # power_law vs. stretched_exponential -0.5703159204901276 0.49175349062272455
    # power_law vs. truncated_power_law -0.7431859717454934 0.22278022761909655
    # exponential vs. truncated_power_law -4.257230668346864 0.14251968288436617

    # US population
    # xmin = 55156.0
    # alpha = 2.3930585013739165
    # sigma = 0.055194987433238224
    # D = 0.024005835264173936
    # power_law vs. exponential 241.10789216848946 0.00027509383674743855
    # power_law vs. lognormal -0.049318764089182565 0.8615305232852399
    # lognormal vs. exponential 241.1572109325785 0.00026093549036197553
    # power_law vs. stretched_exponential 2.3915436326631134 0.3513751129818755
    # power_law vs. truncated_power_law -0.15332502843597773 0.5797431565299043
    # exponential vs. truncated_power_law -241.2612171969255 0.00025414171564295564


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


if __name__ == '__main__':
    population = pd.read_csv('data/US-Population-Coordinate.csv')
    # population = pd.read_csv('data/China-Population-Coordinate.csv')
    population.sort_values(by='Population', ascending=False, inplace=True)
    population = population.reset_index()

    code = pd.read_csv('detail.csv')
    code.sort_values(by='LOC', ascending=False, inplace=True)
    code = code.reset_index()

    df = create_mapping(population, code)
    df.to_csv('data/result-us.csv', index=False)
    # df.to_csv('data/result-cn.csv', index=False)

    draw_pdf(population.Population, 'Population')
    draw_pdf(code.LOC, 'LOC')

    draw_ccdf(population.Population, 'Population')
    draw_ccdf(code.LOC, 'LOC')

    power_law(population.Population)
    power_law(code.LOC)
