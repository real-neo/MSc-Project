import pandas as pd
import powerlaw


def create_mapping(population_file, code_file) -> pd.DataFrame:
    population = pd.read_csv(population_file)
    population.sort_values(by='Population', ascending=False, inplace=True)
    population = population.reset_index()

    code = pd.read_csv(code_file)
    code.sort_values(by='LOC', ascending=False, inplace=True)
    code = code.reset_index()

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

    result = ''

    print('xmin =', fit.xmin)
    print('alpha =', fit.power_law.alpha)
    print('sigma =', fit.power_law.sigma)
    print('D =', fit.power_law.D)

    result = result + 'xmin = ' + str(fit.xmin) + '\n\n'
    result = result + 'alpha = ' + str(fit.power_law.alpha) + '\n\n'
    result = result + 'sigma = ' + str(fit.power_law.sigma) + '\n\n'
    result = result + 'D = ' + str(fit.power_law.D) + '\n\n'

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

    result = result + 'power_law vs. exponential ' + str(R1) + ' ' + str(p1) + '\n\n'
    result = result + 'power_law vs. lognormal ' + str(R2) + ' ' + str(p2) + '\n\n'
    result = result + 'lognormal vs. exponential' + str(R21) + ' ' + str(p21) + '\n\n'
    result = result + 'power_law vs. stretched_exponential ' + str(R3) + ' ' + str(p3) + '\n\n'
    result = result + 'power_law vs. truncated_power_law ' + str(R4) + ' ' + str(p4) + '\n\n'
    result = result + 'exponential vs. truncated_power_law ' + str(R5) + ' ' + str(p5) + '\n\n'

    return result

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


def powerlaw_loc(file):
    code = pd.read_csv(file)
    code.sort_values(by='LOC', ascending=False, inplace=True)
    code = code.reset_index()
    return power_law(code.LOC)


def powerlaw_population(file):
    population = pd.read_csv(file)
    population.sort_values(by='Population', ascending=False, inplace=True)
    population = population.reset_index()
    return power_law(population.Population)


if __name__ == '__main__':
    powerlaw_result = powerlaw_loc('detail.csv')
    print(powerlaw_result)

    powerlaw_result = powerlaw_population('data/US-Population-Coordinate.csv')
    # powerlaw_result = powerlaw_population('data/China-Population-Coordinate.csv')
    print(powerlaw_result)

    df = create_mapping('data/US-Population-Coordinate.csv', 'detail.csv')
    df.to_csv('data/result-us.csv', index=False)
    # df = create_mapping('data/China-Population-Coordinate.csv', 'detail.csv')
    # df.to_csv('data/result-cn.csv', index=False)
