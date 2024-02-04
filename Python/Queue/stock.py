'''
https://programmers.co.kr/learn/courses/30/parts/12081
PROGRAMMERS STACK/QUEUE STOCK
'''

def solution(prices):
    answer = []

    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: count+=1
            else:
                count += 1
                break
        answer.append(count)
    
    return answer

def main():
    prices1 = [1, 2, 3, 2, 3]
    prices2 = [1, 2, 3, 2, 1]

    result1 = [4, 3, 1, 1, 0]
    result2 = [4, 3, 1, 1, 0]
    
    if solution(prices1) == result1: print("RIGHT1")
    if solution(prices2) == result2: print("RIGHT2")

if __name__=="__main__":
    main()