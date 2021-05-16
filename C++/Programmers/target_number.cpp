// Programmers DFS/BFS Target Number
// https://programmers.co.kr/learn/courses/30/parts/12421

// O(2^n) 방법밖에 생각안나는데..
// bad alloc Error

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> numbers, int target) {
    vector<int> temp;
    
    temp.push_back(0);
    
    for(int i=0;i<numbers.size();i++){
        for(int j=(temp.size())/2;j<temp.size();j++){
            temp.push_back(temp[j] + numbers[i]);
            temp.push_back(temp[j] - numbers[i]);
        }
    }

    // for(int i=0;i<temp.size();i++)
    //     cout << temp[i]<<"  ";
        
    int n =0;
    int temp_size = temp.size();
    for(int i=temp_size/2; i<temp_size;i++)
        if(temp[i] == target) n++;
    
    
    int answer = 0;
    return answer;
}

int main(void){
    vector<int> numbers1{1, 1, 1};
    int target1 = 2;
    int return1 = 3;
    if(solution(numbers1, target1) == return1) cout << "right"<<endl;
}