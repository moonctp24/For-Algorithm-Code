/*
BAEKJOON 10610번 30
https://www.acmicpc.net/problem/10610
*/

// *각 자릿수의 합이 3의 배수면 그 수는 3의 배수임을 이용*

#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
    return a>b; // descending sort
}

int main(void){
    string number;
    cin >> number;
    int sum=0;
    bool toggle = false; // Whether the number includes '0'

    for(int i=0;i<number.size();i++){
        sum += number[i]-48; // Subtract 48, because ASCII code of the number starts at 48
        if(number[i]=='0') toggle = true;
    }

    if(sum%3==0 && toggle){ // multiple of 3 && 0 in number
        sort(number.begin(), number.end(), compare);
        for(int i=0;i<number.size();i++)
            cout << number[i];
    } else cout << -1;
}