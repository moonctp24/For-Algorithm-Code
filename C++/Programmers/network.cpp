/*
Programmers DFS/BFS Network
https://programmers.co.kr/learn/courses/30/parts/12421
*/

#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool visited[200];
int count =0;

bool dfs(int x, vector<vector<int>> computers){
    // mark visited node
    if(visited[x] == false) visited[x] = true;
    else return false;

    // cout << x << ' '; // print visited node
    for(int i=0;i<computers[x].size();i++){
        // if node visit itself, change visited is true and continue
        if(i == x) continue;
        if(computers[x][i] == 1)
            if(!visited[i]) dfs(i, computers);
    }
    return true;
}

int solution(int n, vector<vector<int>> computers) {
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(computers[i][j]) if(dfs(i, computers)) count++;

    int answer = count;
    return answer;
}

int main(void){
    vector<vector<int>> computers1{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
    vector<vector<int>> computers2{{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};
    vector<vector<int>> computers3{{1, 1, 0, 0, 0, 0}, {1, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 0, 0}, {0, 0, 0, 1, 0, 1}, {0, 0, 0, 0, 1, 0}, {0, 0, 0, 1, 0, 1}};
    vector<vector<int>> computers4{{1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 1, 0}};

    // cout << endl << "TC1: " << solution(computers1.size(), computers1) << endl;
    // cout << endl << "TC2: " << solution(computers2.size(), computers2) << endl;
    // cout << endl << "TC3: " << solution(computers3.size(), computers3) << endl;
    cout << endl << "TC4: " << solution(computers4.size(), computers4) << endl;
}