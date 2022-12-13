import os

with open('input.txt', "r") as f:
    lines = f.read()

data = lines.split('\n\n')

datalist = list(map(str.splitlines, data))

calslist = []

for eacharray in datalist:
    calories = [int(x) for x in eacharray]
    calslist.append(sum(calories))
    totalcals = sum(calories)

print(calslist)
print(max(calslist))

sortlist = sorted(calslist, reverse=True)

print(sortlist[:3])
print(sum(sortlist[:3]))