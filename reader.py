import csv
from collections import abc, defaultdict


def read_csv_as_dicts(filename, types):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    return list({name: func(value) for name, value, func in zip(
        headers, row, types)} for row in rows)


def read_csv_as_columns(filename, types):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    data = DataCollection()
    for row in rows:
        data.append({name: func(value)
                    for name, func, value in zip(headers, types, row)})
    return data


class DataCollection(abc.Sequence):
    def __init__(self):
        self.data = defaultdict(list)

    def __len__(self):
        keys = list(self.data.keys())
        if not keys:
            return 0
        return len(self.data[keys[0]])

    def __getitem__(self, index):
        return {k: self.data[k][index] for k in self.data}

    def append(self, d):
        for k, v in d.items():
            self.data[k].append(v)
