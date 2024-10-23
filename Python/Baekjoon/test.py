print(15**8)


'''
170,859,375
2,562,890,625
'''

n=10
t = 10
print(t%n)

# 0 1 2 3 4 5 6 7 8 9

aa = [1, 1]
map = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

print(map)
map[aa[0]][aa[1]] = 1
print(map)

x, y = 1, 1
initH = [x, y] # init head
initT = [x, y] # init tail
snkTrc = []
snkTrc.append(initH)
print(snkTrc)

lll = [[0,0],[1,1],[2,2]]
print(lll)
rm = [1,1]
lll.remove(rm)
print(lll)