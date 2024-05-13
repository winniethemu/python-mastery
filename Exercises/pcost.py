def portfolio_cost(filename: str) -> float:
    total = 0.0
    with open(filename) as f:
        for line in f:
            name, shares, price = line.split()
            total += int(shares) * float(price)
    return total


print(portfolio_cost('../Data/portfolio.dat'))
