/*
https://programmers.co.kr/learn/courses/30/parts/12077
PROGRAMMERS HASH DISGUISE
*/

#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

bool search(vector<string> cloth_type, string name){
    for (int i=0; i<cloth_type.size(); i++)
        if(name == cloth_type[i]) return true;
    return false;
}

int solution(vector<vector<string>> clothes) {
    map<string, int> map1;
    
    for (int i=0; i<clothes.size(); i++)
        map1[clothes[i][1]] += 1;
    
    // map 확인 코드
    // for(pair<string, int> m:map1)
    //     cout<< m.first << ", "<< m.second<<endl;
    
    int answer = 1;
    for (pair<string, int> m:map1)
        answer *= m.second+1;
    return answer-1;
}

int main(void){
    vector<vector<string>> clothes1{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
    vector<vector<string>> clothes2{{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
    vector<vector<string>> clothes3{{"round_glasses", "eyewear"}, {"black_sunglasses", "eyewear"}, {"blue_shirts", "top"}, {"jean", "bottom"}};

    int result1 = 5;
    int result2 = 3;
    int result3 = 11;

    if(solution(clothes1) == result1) cout <<"RIGHT1"<<endl;
    if(solution(clothes2) == result2) cout <<"RIGHT2"<<endl;
    if(solution(clothes3) == result3) cout <<"RIGHT3"<<endl;
}