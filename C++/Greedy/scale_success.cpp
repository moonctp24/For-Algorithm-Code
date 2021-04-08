/*
BAEKKJOON 2437번 저울
https://www.acmicpc.net/problem/2437
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    int n=0;
    cin >> n;

    vector<int> scale_weight;
    for(int i=0;i<n;i++){
        int temp=0;
        cin >> temp;
        scale_weight.push_back(temp);
    }

    sort(scale_weight.begin(), scale_weight.end());

    int weight =1;
    for(int i=0;i<n;i++){
        if (weight < scale_weight[i]) break;
        weight += scale_weight[i];
    }

    cout << weight;
}

// reference; https://blog.naver.com/ndb796/221247616094