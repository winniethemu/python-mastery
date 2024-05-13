from collections import namedtuple
import csv


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class SlottedRow(Row):
    __slots__ = ['route', 'date', 'daytype', 'rides']


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
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route, date, daytype, rides = row
            record = helper(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc

    helpers = (as_tuple, as_dict, as_class, as_named_tuple, as_class_and_slots)
    tracemalloc.start()
    for helper in helpers:
        rows = read_rides('Data/ctabus.csv', helper)
        print('Memory Use: Current %d, Peak %d' %
              tracemalloc.get_traced_memory())
