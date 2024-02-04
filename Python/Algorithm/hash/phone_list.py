"""
https://programmers.co.kr/learn/courses/30/parts/12077
PROGRAMMERS HASH Phone Book
"""

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        len_index = len(phone_book[i])
        if phone_book[i] in phone_book[i+1][:len_index]:
            return False
    return True

def main():
    phone_book1 = ["119", "97674223", "1195524421"]
    phone_book2 = ["123", "456", "789"]
    phone_book3 = ["12", "123", "1235", "567", "88"]
    phone_book4 = ["113333", "115555", "345555", "555555", "345444"]

    result1 = False
    result2 = True
    result3 = False
    result4 = True

    if(solution(phone_book1) == result1): print("RIGHT1")
    if(solution(phone_book2) == result2): print("RIGHT2")
    if(solution(phone_book3) == result3): print("RIGHT3")
    if(solution(phone_book4) == result4): print("RIGHT4")

if __name__ == "__main__":
    main()


'''
# 다른사람이 쓴 매우 간결한 코드
# startswith() 함수 사용
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
'''