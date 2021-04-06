/*
BAEKJOON 2217번 ROPE
https://www.acmicpc.net/problem/2217
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
    return a>b; // descending
}

int main(void){
    int n=0;
    vector<int> v, result;

    cin >> n;
    for(int i=0;i<n;i++){
        int temp=0;
        cin>>temp;
        v.push_back(temp);
    }

    sort(v.begin(), v.end()); // ascending sort

    for(int i=0;i<n;i++){
        result.push_back(v[i]*(n-i));
    }

    sort(result.begin(), result.end(), compare); // descending sort
    
    cout << result.front();
}