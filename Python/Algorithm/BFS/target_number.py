"""
https://programmers.co.kr/learn/courses/30/parts/12421
PROGRAMMERS DFS/BFS TARGET NUMBER
"""

count = 0

def dfs(numbers, target, total, deep):
    global count

    if deep == len(numbers):
        if total == target:
            count+=1
        return count
    
    dfs(numbers, target, total+numbers[deep], deep+1)
    dfs(numbers, target, total-numbers[deep], deep+1)
    return count

def solution(numbers, target):

    dfs(numbers, target, 0, 0)
        
    return count

def main():
    numbers = [1, 1, 1, 1, 1]
    target = 3
    result = 5

    if solution(numbers, target) == result: print("RIGHT")

if __name__=="__main__":
    main()
