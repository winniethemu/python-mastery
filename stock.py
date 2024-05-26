import readport


def read_portfolio(filename):
    portfolio = readport.read_portfolio(filename)
    return [Stock(s['name'], s['shares'], s['price']) for s in portfolio]


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


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        if nshares <= self.shares:
            self.shares -= nshares
