
while(True):
    try:
        triL = list(map(int, input().split(' ')))
        if triL[0] == 0 and triL[1] == 0 and triL[2] == 0:
            break
        # print(triL)
        triL.sort()
        maxV, middleV, minV = triL[2], triL[1], triL[0]
        # print(triL)
            
        # print(maxV, middleV, minV)
        if middleV + minV <= maxV or maxV == 0 or middleV == 0 or minV == 0:
            print('Invalid')
            continue
        if maxV == middleV and maxV == minV:
            print('Equilateral')
        elif (maxV == middleV and maxV != minV) or (maxV == minV and maxV != middleV) or (middleV == minV and maxV != middleV):
            print('Isosceles')
        elif maxV != middleV and middleV != minV:
            print('Scalene')
        else:
            print('wrong')
    except EOFError:
        break
        
'''
7 7 7
6 5 4
3 2 5
6 2 6
0 0 0
'''