n = int(input())
build = list(map(int, input().split(' ')))
view = [0 for _ in range(n)]

def incliVal(a, b, x, y):
    if a-x == 0:
        return 's'
    else:
        return (b-y)/(a-x)
# print(incliVal(-2, 7, 1, 2))

for i in range(n):
    prevC = 0
    nextC = 0
    
    maxV = 1000000000
    for j in range(i-1, -1, -1): # j < i
        # print(i, j)
        nowIncli = incliVal(j, build[j], i, build[i])
        if incliVal == 's' and i-j == 1:
            prevC += 1
            break
        if maxV > nowIncli:
            prevC += 1
            maxV = nowIncli
        else:
            continue
    maxV = -1000000000
    for j in range(i+1, n):
        nowIncli = incliVal(i, build[i], j, build[j])
        if incliVal == 's' and j-i == 1:
            nextC += 1
            break
        if maxV < nowIncli:
            nextC += 1
            maxV = nowIncli
        else:
            continue
    view[i] = prevC + nextC
print(max(view))

'''5
1 2 4 3 2
    |
    | |
  | | | |
| | | | |
'''