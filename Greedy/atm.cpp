/*
BAEKJOON 11399번 ATM
https://www.acmicpc.net/problem/11399
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    int n;
    cin >> n;
    vector <int> v;

    for(int i=0;i<n;i++){
        int temp=0;
        cin >> temp;
        v.push_back(temp);
    }

    sort(v.begin(), v.end()); // ascending sort

    int result=0;
    for(int i=0;i<v.size();i++){
        for(int j=0;j<=i;j++){
            result += v[j];
        }
    }

    cout << result<<endl;
}