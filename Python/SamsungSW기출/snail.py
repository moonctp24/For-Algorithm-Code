"""
SWEA 1954. 달팽이 숫자 D2
"""

t = int(input())
for q in range(1, t+1):
    n = int(input())

    rst = [0 for _ in range(n)]
    for i in range(n):
        rst[i] = [0 for _ in range(n)]
    # print(rst)

    x, y = 0, 0
    maxN = n-1
    minN = 0
    for i in range(1, n*n+1):
        rst[y][x] = i
        # print('in: ', x, y)
        # for a in range(n):
            # print(rst[a])

        if(x != maxN and y == minN): # go right
            if(rst[y][x+1] != 0):
                y += 1
            else:
                x += 1
        elif(x == maxN and y != maxN): # go down
            if(rst[y+1][x] != 0):
                x-=1
            else:
                y += 1
        elif(x > minN and y == maxN): # go left
            x -= 1
        elif(x == minN and y > minN): # go up
            if(rst[y-1][x] != 0):
                x += 1
                maxN -= 1
                minN += 1
            else:
                y -= 1

        # print('out: ', x, y)
    print('#'+str(q))
    for a in range(n):
        for b in range(n):
            print(rst[a][b], end=' ')
        print()

'''
1 2 3
8 9 4
7 6 5
'''