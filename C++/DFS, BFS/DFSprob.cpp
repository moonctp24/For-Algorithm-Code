/* 동빈나 이코테 2021 강의
    <문제> 음료수 얼려 먹기
    https://github.com/ndb796/python-for-coding-test/blob/master/5/10.cpp
    */

#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int graph[1001][1001] = {{0,0,1,1,0}, {0,0,0,1,1}, {1,1,1,1,1}, {0,0,0,0,0}};

bool search(int x, int y){
    if(x<0 || x>n-1 || y<0 || y>m-1) return false;

    if(!graph[x][y]){
        graph[x][y] = 1;
        search(x-1, y);
        search(x, y-1);
        search(x, y+1);
        search(x+1, y);
        return true;
    }

    return false;
}

int main(void){
    cin >> n >> m;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++){
            int a;
            cin >> a;
            graph[i][j] = a;
        }

    int count=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++){
            if(!graph[i][j]) if(search(i, j)) count++;
        }
    
    cout << count << endl;

}

/*
4 5
0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0

입력 시, 출력 3
*/