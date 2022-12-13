# a = rock
# b = paper
# c = scissor

# x = rock 1
# y = paper 2
# z = scissor 3

# x = lose
# y = draw
# z = win

# loss = 0
# draw = 3
# win = 6

ax = 3
ay = 4
az = 8
bx = 1
by = 5
bz = 9
cx = 2
cy = 6
cz = 7

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