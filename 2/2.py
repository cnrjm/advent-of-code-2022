# a = rock
# b = paper
# c = scissor

# x = rock
# y = paper
# z = scissor

# x = 1
# y = 2
# z = 3

# loss = 0
# draw = 3
# win = 6

ax = 4
ay = 8
az = 3
bx = 1
by = 5
bz = 9
cx = 7
cy = 2
cz = 6

with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

axcount = (lines.count('A X'))
aycount = (lines.count('A Y'))
azcount = (lines.count('A Z'))
bxcount = (lines.count('B X'))
bycount = (lines.count('B Y'))
bzcount = (lines.count('B Z'))
cxcount = (lines.count('C X'))
cycount = (lines.count('C Y'))
czcount = (lines.count('C Z'))

totalax = axcount * ax
totalay = aycount * ay
totalaz = azcount * az
totalbx = bxcount * bx
totalby = bycount * by
totalbz = bzcount * bz
totalcx = cxcount * cx
totalcy = cycount * cy
totalcz = czcount * cz

totallist = [totalax,totalay,totalaz,totalbx,totalby,totalbz,totalcx,totalcy,totalcz]
print(sum(totallist))