"""
삼성SDS 입과테스트 1번
"""

def main():
    tc = []
    tcn = int(input())
    for i in range(tcn):
        n = int(input())
        fortc = list(map(int, input().split(' ')))
        tc.append(fortc)
    print(tc)

    result = []
    for i in tc:
        print(len(i))
        if len(i) <=2:
            result.append(max(i))
        else:
            min_time = min(i)
            min_index = i.index(min_time)
            print(min_index)
            sum = 0
            for j in range(len(i)):
                if j == min_index:
                    continue
                else:
                    sum += i[j]
            sum += min_time*(len(i)-1)
            result.append(sum)
    for i in range(len(result)):
        print('#{} {}'.format(i+1, result[i]))
main()