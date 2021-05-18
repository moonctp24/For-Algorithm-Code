// target_number.cpp -> recursion을 이용한 DFS 개념으로 시간 복잡도 줄이기

// Programmers DFS/BFS Target Number
// https://programmers.co.kr/learn/courses/30/parts/12421

#include <vector>
#include <iostream>

using namespace std;

int count =0;

void dfs(vector<int> numbers, int target, int sum, int deep){
    if(deep == numbers.size()) {
        if(sum == target) count++;
        return;
    }

    dfs(numbers, target, sum + numbers[deep], deep+1); // DO NOT deep++ => 한 변수가 어떤 함수의 인자로 두 번 이상 사용될 경우에는 그 변수에 증감 연산자를 사용하지 않는다. 예: func(x*2, x++)
    dfs(numbers, target, sum - numbers[deep], deep+1);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    
    int answer = count;
    return answer;
}

int main(void){
    vector<int> numbers1{1, 1, 1, 1, 1};
    int target1 = 3;
    int return1 = 5;
    if(solution(numbers1, target1) == return1) cout << "right"<<endl;
}