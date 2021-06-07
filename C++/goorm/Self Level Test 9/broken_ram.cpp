/*
https://level.goorm.io/exam/58258/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%9E%88%EC%96%B4%EB%A1%9C%EC%A6%88-%EC%85%80%ED%94%84%EB%A0%88%EB%B2%A8%ED%85%8C%EC%8A%A4%ED%8A%B8-9%EC%B0%A8/quiz/1
GOORM ALGORITHM HEROES SELF LEVEL TEST 9 BROKEN RAM
여기는 레벨테스트 문제가 좀 괜찮은 것 같다.
*/

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

// 2의 제곱수인지 체크
bool check(int a){
	for(int i=7;i<31;i++)
		if (a == pow(2,i)) return true;
	return false;
}
int main() {
	int n;
	cin >> n;
	int m[n];
	for(int i=0;i<n;i++)
		cin >> m[i];
	
	vector<int> answer;
	for(int i=0;i<n;i++){
		if(check(m[i])) continue;
		else answer.push_back(i+1);
	}
	
	cout << answer.size() <<endl;
	for (int i=0;i<answer.size();i++)
		cout << answer[i]<< " ";
	return 0;
}

/*
TC1
3
256 274 512
=>
1
2

TC2
5
128 256 512 1024 2048
=> 0

TC3
10
1048576 16384 131072 8388608 834814 67108864 8192 1267650 128 129
=>
3
5 8 10
*/