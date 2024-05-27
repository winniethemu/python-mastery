import readport
from decimal import Decimal


class Stock:
    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        if nshares <= self.shares:
            self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)


class DecimalStock(Stock):
    types = (str, int, Decimal)


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
