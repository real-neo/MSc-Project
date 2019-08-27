import gmaps
import pandas as pd
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import GoogleV3


def add_coordinate(dataset: pd.DataFrame) -> pd.DataFrame:
    API_KEY = 'AIzaSyBIzyBqDeJ7noegKeFdSKNSncOU56onBo4'

    gmaps.configure(api_key=API_KEY)
    geo_locator = GoogleV3(api_key=API_KEY)

    new_data = pd.DataFrame(columns=['City', 'Population', 'Latitude', 'Longitude'])

    for index, data in dataset.iterrows():
        while True:
            print(index, 'Querying', data.City, end=" ")
            try:
                location = geo_locator.geocode(data.City)
                print('Latitude', location.latitude, 'Longitude', location.longitude)
                new_line = pd.Series([data.City, data.Population, location.latitude, location.longitude], index=new_data.columns)
                break
            except GeocoderTimedOut as e:
                print('Service time out')
            except GeocoderUnavailable as e:
                print('Service not available')
        new_data = new_data.append(new_line, ignore_index=True)

    return new_data


if __name__ == '__main__':
    population = pd.read_csv('data/US-Population.csv')
    # population = pd.read_csv('data/China-Population.csv')

    add_coordinate(population).to_csv('data/US-Population-Coordinate.csv', index=False)
    # add_coordinate(population).to_csv('data/China-Population-Coordinate.csv', index=False)
