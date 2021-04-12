#include <iostream>
#include <regex>
#include <vector>

using namespace std;

int main(void){
    vector<string> phone_numbers = {"010-1234-5678", "010-123-4567", "011-1234-5567", "010-12345-6789", "123-4567-8901", "010-123-467"};

    // [01]{3} : 0 또는 1이 3번 반복
    regex re("[01]{3}-\\d{3,4}-\\d{4}");

    for(const auto &number : phone_numbers){
        cout << number << " : " << boolalpha << regex_match(number, re) << endl;
        // regex_match(str, re) : 검사할 형식으로 초기화한 regex 타입의 인스턴스인 re, str을 비교하여 올바른 형식인지 검사 후 true, false 리텀
    }
}

/*
\\d : 숫자 1개만 받아야 OK
\\d+ : 숫자 1개 이상이면 OK
\\d* : 숫자 0개 이상이면 OK
\\d? : 숫자 0개 혹은 1개여야 OK

regex re("[ab]")
a나 b만 된다. 각 1개씩만.
a : OK
b : OK
ab : not OK
c : not OK

regex re("[A-Z]+");
‘A’ 부터 ‘Z’ 까지의 문자가 1개 이상이면 OK
regex re("[A-Z]{1,5}");
‘A’ 부터 ‘Z’ 까지의 문자가 최소 1개 최대 5개면 OK
*/