import readport
from decimal import Decimal


class Stock:
    _types = (str, int, float)
    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if value < 0 or not isinstance(value, self._types[1]):
            raise ValueError(
                    f'Shares must be a positive {self._types[1].__name__}')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0 or not isinstance(value, self._types[2]):
            raise ValueError(
                    f'Price must be a positive {self._types[2].__name__}')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        if nshares <= self.shares:
            self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)


class DecimalStock(Stock):
    _types = (str, int, Decimal)


def read_portfolio(filename, klass=Stock):
    portfolio = readport.read_portfolio(filename)
    return [klass(s['name'], s['shares'], s['price']) for s in portfolio]


def print_portfolio(portfolio, show_header=True):
    if show_header:
        print(f'{"name":>10s} {"shares":>10s} {"price":>10s}')
        divider = ''
        for i in range(3):
            divider += '-' * 10
            if i < 3:
                divider += ' '
        print(divider)
    for stock in portfolio:
        print(f'{stock.name:>10s} {stock.shares:>10d} {stock.price:>10.2f}')
