/*
https://level.goorm.io/exam/43266/%ED%99%A9%EC%A0%9C%EC%9D%98-%EB%AA%B0%EB%9D%BD/quiz/1
GOORM THE FALL OF THE EMPEROR
*/

#include <iostream>
#include <vector>

using namespace std;
int main() {
	int n;
	int k;
	cin >> n >> k;
	vector<int> live;
	
	// 전부 살아있음(1)으로 초기회
	for(int i =0; i<n; i++)
		live.push_back(1);

	// 첫번째(index 0)부터 k번째만큼 죽음(-1)으로 바꿈
	// 두 사람이 남을 때까지 (n-2) 반복
	int index = 0;
	int fork = 0;
	int i = 1;
	while(true){
		// terminal contition
		if (i == n-2) break;
		// 죽은 사람의 index면 다음 사람으로 건너감
		if (live[(index+fork)%live.size()] == -1){
			index++;
			continue;
		}

		live[0] = -1;
		// fork값이 k가 되지 않으면 다음 사람으로 넘어감
		if (fork == k){
			// 차례 = k번째 사람 + 죽어서 건너 뛴 사람 수
			index += fork;
			// index가 배열의 사이즈를 넘어서면 0부터 다시 셈
			index %= live.size();
			// 차례인 사람 자살
			live[index] = -1;

			// 한 명 자살했으면 k값 리셋하고, 다음 사람 진행
			fork = 0;
			i++;
		}
		fork++;
	}

	// 살아있는 사람의 인덱스+1 출력
	vector<int> answer;
	for (int j=0; j<live.size(); j++){
		if (live[j] == 1)
			answer.push_back(j+1);
	}
	cout << answer[0] << " "<< answer[1] << endl;
	return 0;
}

/*
TC1
19 6 => 9 10

TC2
6 3 => 3 5

TC3
12 3 => 3 8
*/