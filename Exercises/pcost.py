total = 0

with open('../../Data/portfolio.dat') as f:
    for line in f:
        name, shares, price = line.split()
        total += int(shares) * float(price)

print(total)
