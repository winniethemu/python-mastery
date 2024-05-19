import csv


def read_csv_as_dicts(filename, types):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    return list({name: func(value) for name, value, func in zip(
        headers, row, types)} for row in rows)
