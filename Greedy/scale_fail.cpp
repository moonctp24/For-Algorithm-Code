/*
BAEKKJOON 2437번 저울
https://www.acmicpc.net/problem/2437

*** time over *** O(N)으로 풀 수 있음
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
    return a>b; // descending sort
}

int main(void){
    int n=0;
    cin >> n;

    vector<int> scale_weight;
    for(int i=0;i<n;i++){
        int temp=0;
        cin >> temp;
        scale_weight.push_back(temp);
    }

    sort(scale_weight.begin(), scale_weight.end(), compare);

    int weight =1;
    while(true){
        int tmep_weight=weight;
        for(int i=0;i<n;i++){
            if(tmep_weight >= scale_weight[i] && tmep_weight >= 0){
                tmep_weight -= scale_weight[i];
            }
        }
        
        if(tmep_weight != 0) break;
        weight ++;
    }

    cout << weight;
}