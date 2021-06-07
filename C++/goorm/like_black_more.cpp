/*
https://level.goorm.io/exam/47881/%EA%B7%BC%EB%AC%B5%EC%9E%90%ED%9D%91/quiz/1
GOORM BECOME BLACK UPGRADE
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
	int n, k;
	cin >> n >> k;
    vector<int> array = {2, 1, 1, 1};
	// int array[4];
	// for (int i=0; i<n; i++){
	// 	cin >> array[i];
	// }
	
    int minval = *min_element(array.begin(), array.end());

    cout<< minval<<endl;
	n -= k;
	if (n%(k-1)==0) n = n/(k-1);
	else n = n/(k-1) +1;
	cout << n+1 << endl;
	return 0;
}


/*
단순히 n = n-k -> n = n/(k-1) +1 만하면 TC는 전부 통과 된다.
하지만 히든테케에서 걸려야하는데 그냥 정답입니다. 뜬다. TC를 바꿔서 해보자
minval의 인덱스를 찾아서 좌우로 k개를 묶고 시작해야해서 개복잡해지네 나중에하자 레벨2인거 보니 원래 n,k값만 가지로 푸는 문제는 맞는 것 같다.

TC1
4 3
2 3 1 4
=> 2

+ TC
4 3
2 1 1 1
=> 1

TC2
8 3
7 3 1 8 4 6 2 5
=> 4

TC3
37 4
31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
=> 12
*/