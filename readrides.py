from collections import abc, namedtuple
import csv


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class SlottedRow(Row):
    __slots__ = ['route', 'date', 'daytype', 'rides']


class RideData(abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        if (len(self.routes) == len(self.dates) == len(self.daytypes) == len(
                self.numrides)):
            return len(self.routes)
        raise ValueError('inconsistent column lengths')

    def __getitem__(self, index):
        return {
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


NamedTupleRow = namedtuple(
    'NamedTupleRow', ('route', 'date', 'daytype', 'rides'))


def as_tuple(route, date, daytype, rides):
    return (route, date, daytype, rides)


def as_dict(route, date, daytype, rides):
    return {
        'route': route,
        'date': date,
        'daytype': daytype,
        'rides': rides,
    }


def as_class(route, date, daytype, rides):
    return Row(route, date, daytype, rides)


def as_named_tuple(route, date, daytype, rides):
    return NamedTupleRow(route, date, daytype, rides)


def as_class_and_slots(route, date, daytype, rides):
    return SlottedRow(route, date, daytype, rides)


def read_rides(filename, helper):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            route, date, daytype, rides = row
            record = helper(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc

    tracemalloc.start()
    rows = read_rides('Data/ctabus.csv', as_dict)
    print('Memory Use: Current %d, Peak %d' %
          tracemalloc.get_traced_memory())
