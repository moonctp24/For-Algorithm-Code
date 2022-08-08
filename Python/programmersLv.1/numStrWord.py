"""
https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
PROGRAMMERS 숫자 문자열과 영단어
"""

def solution(s):
    words=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, num in enumerate(words):
        if num in words:
            s = s.replace(num, str(i))
    
    return int(s)

def main():
    s1 = "one4seveneight"
    s2 = "23four5six7"
    s3 = "2three45sixseven"
    s4 = "123"

    result1 = 1478
    result2 = 234567
    result3 = 234567
    result4 = 123

    if solution(s1) == result1: print("RIGHT1")
    if solution(s2) == result2: print("RIGHT2")
    if solution(s3) == result3: print("RIGHT3")
    if solution(s4) == result4: print("RIGHT4")

if __name__=="__main__":
    main()
