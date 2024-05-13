def portfolio_cost(filename: str) -> float:
    total = 0.0
    with open(filename) as f:
        for line in f:
            try:
                name, shares, price = line.split()
                total += int(shares) * float(price)
            except ValueError as e:
                print(f'Couldn\'t parse: {line}Reason: {e}')
    return total


print(portfolio_cost('../Data/portfolio3.dat'))
