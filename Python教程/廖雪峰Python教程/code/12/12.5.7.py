import itertools

for x in map(lambda x, y: x*y, [10, 20, 40], itertools.count(1)):
    print(x)