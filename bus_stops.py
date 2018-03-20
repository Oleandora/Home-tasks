from math import cos, acos, sin, degrees, radians
import decimal
import csv


decimal.getcontext().prec = 1
file_with_metro_stations = 'data-397-2018-03-06.txt'
file_with_bus_stations = 'data-398-2018-03-06.txt'


def read_csv(file):
    with open(file, newline='',) as csv_file:
        reader = csv.DictReader(csv_file, dialect='excel-tab')
        for row in reader:
            yield dict(name=row['Наименование'],lon=float(row['Долгота в WGS-84']), lat=float(row['Широта в WGS-84']))


def to_radians(point):
    return radians(point['lat']), radians(point['lon'])


def distance(metro_station, bus_station):
    radius = int(6371221)
    needed_radius = 500

    metro_station_latitude, metro_station_longitude = to_radians(metro_station)
    bus_station_latitude, bus_station_longitude = to_radians(bus_station)

    length = radius * acos(sin(metro_station_latitude)*sin(bus_station_latitude) +
                           cos(metro_station_latitude)*cos(bus_station_latitude) *
                           cos(metro_station_longitude - bus_station_longitude)
                           )
    return length <= needed_radius


def bus_stations_filter(metro_station):
    radius = int(6371221)
    needed_radius = 500
    delta = degrees(needed_radius / radius)

    longitude_min, longitude_max = metro_station['lon'] - delta, metro_station['lon'] + delta
    latitude_min, latitude_max = metro_station['lat'] - delta, metro_station['lat'] + delta

    metro_station['bus'] = 0

    for bus_stop in read_csv(file_with_bus_stations):
        if latitude_min < bus_stop['lat'] < latitude_max and longitude_min < bus_stop['lon'] < longitude_max:
            if distance(metro_station, bus_stop):
                metro_station['bus'] += 1


def iter_stations(metro_stations):
    for station in metro_stations:
        yield station['bus']


def find_stations(metro_stations):
    max_stops = max(iter_stations(metro_stations))
    max_stations = [x for x in metro_stations if x['bus'] == max_stops]
    return max_stations


if __name__ == '__main__':
    metro_stations = [x for x in read_csv(file_with_metro_stations)]

    for item in metro_stations:
        bus_stations_filter(item)

    print(find_stations(metro_stations))


