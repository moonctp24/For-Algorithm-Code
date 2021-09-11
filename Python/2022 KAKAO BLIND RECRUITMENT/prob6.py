# hidden tc까지 다 맞음
# 효율성 테스트 전부 시간 초과

def solution(board, skill):
    for i in skill:
        if i[0] == 1: # 적 공격
            for x in range(i[1], i[3]+1):
                for y in range(i[2], i[4]+1):
                    board[x][y] -= i[5]

        if i[0] == 2: # 우리 힐
            for x in range(i[1], i[3]+1):
                for y in range(i[2], i[4]+1):
                    board[x][y] += i[5]
    
    count = 0
    for x in board:
        for y in x:
            if y > 0:
                count += 1

    return count

def main():
    board1 = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
    board2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    skill1 = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
    skill2 = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]

    result1 = 10
    result2 = 6


    if(solution(board1, skill1) == result1): print("RIGHT1")
    else: print('TRY AGAIN')
    if(solution(board2, skill2) == result2): print("RIGHT2")
    else: print('TRY AGAIN')


if __name__ == "__main__":
    main()