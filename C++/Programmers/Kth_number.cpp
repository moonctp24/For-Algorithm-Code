/*
Programmers 코딩테스트 > 정렬 > K번째수
https://programmers.co.kr/learn/courses/30/lessons/42748?language=cpp
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for(int i=0;i<commands.size();i++) {
        vector<int> temp;
        for(int j=commands[i][0]; j<=commands[i][1]; j++) {
            temp.push_back(array[j-1]);
        }
        sort(temp.begin(), temp.end());
        answer.push_back(temp[commands[i][2]-1]);
    }

    return answer;
}

/* PREVIOUS SOLUTION
vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    //vector<vector<int>> array_temp;
    int total_number = commands.size();
    
    for (int i=0;i<total_number;i++){
        vector<int> array_temp;
        for(int j=commands[i][0]-1;j<commands[i][1];j++){
            array_temp.push_back(array[j]);
        }
        sort(array_temp.begin(),array_temp.end());
        answer.push_back(array_temp.at(commands[i][2]-1));
    }

    return answer;
}
*/

int main(void) {
    vector<int> tc1_array {1, 5, 2, 6, 3, 7, 4};
    vector<vector<int>> tc1_commands {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

    vector<int> tc1_answer{5, 6, 3};

    if(solution(tc1_array, tc1_commands) == tc1_answer) cout << "RIGHT" << endl;
}

// 히든 TC까지 전부 통과