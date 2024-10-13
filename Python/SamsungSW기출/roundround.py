t = int(input())
def checkRoundRound(s):
    if s == s[::-1]:
        return True
    else:
        return False
for tt in range(t):
    strr = input()
    if len(strr)%2 == 0:
        if strr == strr[::-1]:
            print('#'+str(tt+1), 'YES')
        else:
            print('#'+str(tt+1), 'NO')
    else:
        s1 = strr[:(len(strr)-1)//2]
        s2 = strr[(len(strr)-1)//2+1:]
        if checkRoundRound(strr) and checkRoundRound(s1) and checkRoundRound(s2):
            print('#'+str(tt+1), 'YES')
        else:
            print('#'+str(tt+1), 'NO')
'''
3
hello
abcba
abacaba

2
hhaall
hlaalh
'''

# s = '123'
# s[::-1]
# print(s[::-1])