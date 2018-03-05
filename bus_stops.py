from math import cos, acos, sin, degrees, radians
import decimal, csv


RADIUS = int(6371221)
R = 500
DELTA = degrees(R / RADIUS)
decimal.getcontext().prec = 1
file_ms = 'data-397-2018-03-06.txt'
file_bs = 'data-398-2018-03-06.txt'


def read_csv(file):
    with open(file, newline='',) as csvfile:
        reader = csv.DictReader(csvfile, dialect='excel-tab')
        for row in reader:
            yield dict(name=row['Наименование'],lon=float(row['Долгота в WGS-84']), lat=float(row['Широта в WGS-84']))


def distance(ms, bs):

    def to_rad(point):
        return radians(point['lat']), radians(point['lon'])

    ms_lat, ms_lon = to_rad(ms)
    bs_lat, bs_lon = to_rad(bs)

    l = RADIUS * acos(sin(ms_lat)*sin(bs_lat) + cos(ms_lat)*cos(bs_lat) * cos(ms_lon - bs_lon))
    return True if l <= R else False


def bus_stations_filter(ms):

    global DELTA, RADIUS

    lon_min, lon_max = ms['lon'] - DELTA, ms['lon'] + DELTA
    lat_min, lat_max = ms['lat'] - DELTA, ms['lat'] + DELTA

    ms['bus'] = 0

    for item in read_csv(file_bs):
        if lat_min < item['lat'] < lat_max and lon_min < item['lon'] < lon_max:
            if True:
                ms['bus'] += 1


def iter_ms(ms):
    for item in ms:
        yield item['bus']


def find_stations(ms):
    max_stops = max(iter_ms(ms))
    max_stations = [x for x in ms if x['bus'] == max_stops]
    return max_stations


if __name__ == '__main__':
    metro_stations = [x for x in read_csv(file_ms)]

    for item in metro_stations:
        bus_stations_filter(item)

    print(find_stations(metro_stations))


