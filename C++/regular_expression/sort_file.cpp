/*
Programmers 2018 KAKAO BLIND RECRUITMENT [3차] 파일명 정렬
https://programmers.co.kr/learn/courses/30/lessons/17686?language=cpp
*/

// stable_sort() 함수 활용 - sort()와 큰 차이점은 정렬시 기준에 동일하게 부합하는 원소 두 개가 있을 때, 랜덤하게 정렬하느냐 원본 위치를 유지하느냐 입니다. stable_sort()는 원본 위치를 유지합니다.

/*
문자열 조건 => HEAD + NUMBER + TAIL
- HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
- NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
- TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.
*/

#include <string>
#include <vector>
#include <regex>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> files) {
    regex re("(\\D+)([0-9]{0,5})(.*)");
    
    for(const auto &number : files){
        cout << number << " : " << boolalpha << regex_match(number, re) << endl;
    }
    
    vector<string> answer;
    return answer;
}

int main(void){
    vector<string> tc1 = {"img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"};
    vector<string> tc2 =  {"F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"};
    solution(tc1);
}

/*
어려워서 포기
간단한 정답 (다들 regex 안써서 푸시네)
https://codingwell.tistory.com/43?category=917768
*/
