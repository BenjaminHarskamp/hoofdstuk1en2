ICOR = 8
PROG = 6
CSN = 6


list = [ICOR, PROG, CSN]
avg = sum(list)/len(list)
print(avg)

bel = 30
totbel = 30 * avg * 3
print(totbel)

print ('mijn cijfers', round(avg, 1), 'leveren een beloning van', (totbel))
