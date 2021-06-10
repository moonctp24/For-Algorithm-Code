/*
되는데 제출이 안 됨...
1535A fair_playoff
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int main(void){
    int n;
    cin >> n;
    vector<vector<int>> array;
    for (int i=0;i<n;i++){
        for (int j=0;j<4;j++){
            int tmp;
            cin >> tmp;
            array[i].push_back(tmp);
        }
    }
    // int n = 4;
    // vector<vector<int>> array = {{3, 7, 9, 5}, {4, 5, 6, 9}, {5, 3, 8, 1}, {6, 5, 3, 2}};

    for (int i=0;i<n;i++){
        int left_win = max(array[i][0], array[i][1]);
        int right_win = max(array[i][2], array[i][3]);

        sort(array[i].begin(), array[i].end());
        int bigest1 = array[i][3];
        int bigest2 = array[i][2];

        if ((left_win == bigest1 && right_win == bigest2) || (left_win == bigest2 && right_win == bigest1)) cout << "YES"<<endl;
        else cout << "NO"<<endl;
    }
}