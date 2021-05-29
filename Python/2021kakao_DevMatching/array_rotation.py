"""
https://programmers.co.kr/learn/challenges
PROGRAMMERS 2021 KAKAO DEV-MATCHING ARRAY ROTATION
"""

def solution(rows, columns, queries):
    matrix = []

    matrix.append([0])
    for i in range(1, rows+1):
        matrix.append([])
        matrix[i].append(0)
        for j in range(1, columns+1):
            matrix[i].append((i-1)*columns + j)
    
    answer = []
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1] # x1, y1 값 임시 저장
        min_val = []
        min_val.append(tmp)

        # left
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i+1][y1]
            min_val.append(matrix[i][y1])

        # bottom
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i+1]
            min_val.append(matrix[x2][i])

        # right
        for i in range(x2-1, x1-1, -1):
            matrix[i+1][y2] = matrix[i][y2]
            min_val.append(matrix[i][y2])

        # ceil
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i-1]
            min_val.append(matrix[x1][i])
            
        matrix[x1][y1+1] = tmp
        answer.append(min(min_val))
    
    return answer

def main():
    rows1 = 6
    rows2 = 3
    rows3 = 100
    
    columns1 = 6
    columns2 = 3
    columns3 = 97
    
    queries1 = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
    queries2 = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
    queries3 = [[1, 1, 100, 97]]

    result1 = [8, 10, 25]
    result2 = [1, 1, 5, 3]
    result3 = [1]

    if solution(rows1, columns1, queries1) == result1: print("RIGHT1")
    if solution(rows2, columns2, queries2) == result2: print("RIGHT2")
    if solution(rows3, columns3, queries3) == result3: print("RIGHT3")

if __name__=="__main__":
    main()
    