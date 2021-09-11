import math

def is_prime_number(x):
    if x == 1 or x == 0:
        return 0
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1

def solution(n, k):
    num = []
    while n >= k:
        num.append(str(n%k))
        n = math.floor(n/k)
    num.append(str(n))
    
    num2 = []
    for i in range(len(num)-1, -1, -1):
        num2.append(num[i])

    num_list = ''
    count = 0
    for i in num2:
        if i == '0':
            if len(num_list) > 0:
                if is_prime_number(int(num_list)) == 1:
                    count += 1
            num_list = ''
        else:
            num_list += i

    if len(num_list) != 0:
        if is_prime_number(int(num_list)) == 1:
            count += 1
    return count

def main():
    n1 = 437674
    n2 = 110011

    k1 = 3
    k2 = 10

    result1 = 3
    result2 = 2


    if(solution(n1, k1) == result1): print("RIGHT1")
    else: print('TRY AGAIN')
    if(solution(n2, k2) == result2): print("RIGHT2")
    else: print('TRY AGAIN')


if __name__ == "__main__":
    main()