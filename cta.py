from collections import defaultdict
from readrides import read_rides, as_dict

rows = read_rides('Data/ctabus.csv', as_dict)

data = defaultdict(dict)

for row in rows:
    route = row['route']
    date = row['date']
    daytype = row['daytype']
    rides = row['rides']
    data[route][date] = rides


print(f'number of routes: {len(data)}\n')

print(
    f"number of people rode Route 22 on 02/02/2011: {data['22']['02/02/2011']}\n")

print('total number of rides for each route:')
for route in data:
    subtotal = sum(int(value) for value in data[route].values())
    print(f'Route {route}: {subtotal}')

print()
print('top 5 ridership increase:')
routes = []
for route in data:
    ridership_2001 = sum(
        int(item[1]) for item in data[route].items() if item[0].endswith('2001'))
    ridership_2011 = sum(
        int(item[1]) for item in data[route].items() if item[0].endswith('2011'))
    routes.append((route, ridership_2011 - ridership_2001))
routes.sort(key=lambda r: r[1], reverse=True)
print(routes[:5])
