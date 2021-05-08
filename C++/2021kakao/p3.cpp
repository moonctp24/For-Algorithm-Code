#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

string solution(int n, int k, vector<string> cmd) {
    string com(n, 'O');
    
    stack<int> stack;
    
    for(int i=0;i<cmd.size();i++){
        if(cmd[i][0] == 'D') {
            for(int j=0;j<stoi(cmd[i].substr(2));j++){
                k++;
                if(com[k] == 'X') k++;
                if(k>=n) k--;
            } while(com[k] == 'X') k--;
        }
        if(cmd[i] == "C") {
            com.replace(k, 1, "X");
            stack.push(k);
            k++;
            while(com[k] == 'X'|| k>=n) k--;
        }
        if(cmd[i][0] == 'U') {
            for(int j=0;j<stoi(cmd[i].substr(2));j++){
                k--;
                if(com[k] == 'X') k--;
                if(k<0) k=0;
            }
            while(com[k] == 'X') k++;
        }
        if(cmd[i] == "Z") {
            com.replace(stack.top(), 1, "O");
            stack.pop();
        }
        // for(int i=0;i<len;i++)
        //     cout << com[i] << " ";
        // cout << endl << k << endl;
    }

    return com;
}