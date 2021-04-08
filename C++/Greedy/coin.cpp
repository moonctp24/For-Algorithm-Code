/*
BAEKJOON 11047번 동전 0
https://www.acmicpc.net/problem/11047
*/

#include <iostream>
#include <vector>

using namespace std;

int main(void){
    int n, k;
    cin >> n >> k;
    vector <int> v;
    for(int i=0;i<n;i++){
        int temp=0;
        cin >> temp;
        v.push_back(temp);
    }

    int count=0;
    int num = v.size(); // 밑에 for문에 i<v.back() 바로 넣었더니 v의 마지막 원소를 꺼낼 때마다 사이즈가 줄어들어서 반복 횟수에 영향을 미침

    for(int i=0;i<num;i++){
        count += k/v.back();
        k = k%v.back();
        v.pop_back();
    }
    cout << count<<endl;
}