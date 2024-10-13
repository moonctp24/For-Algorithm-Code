t = int(input())
for tt in range(t):
    n, m = map(int, input().split(' '))
    nL = list(map(str, input().split(' ')))
    mL = list(map(str, input().split(' ')))
    
    q = int(input())
    rst = '#'+str(tt+1)+' '
    for qq in range(q):
        c = int(input())
        n1 = nL[c%n-1]
        m1 = mL[c%m-1]
        # print(n1+m1)
        rst += n1+m1 + ' '
    print(rst[:len(rst)-1])
'''
2
10 12
sin im gye gap eul byeong jeong mu gi gyeong
yu sul hae ja chuk in myo jin sa o mi sin
7
1
2
3
4
2018
2019
2020
10 12
sin im gye gap eul byeong jeong mu gi gyeong
yu sul hae ja chuk in myo jin sa o mi sin
7
1
2
3
4
2018
2019
2020

1
10 12
sin im gye gap eul byeong jeong mu gi gyeong
yu sul hae ja chuk in myo jin sa o mi sin
1
12
'''