/*
https://level.goorm.io/exam/43263/%ED%8A%B9%EC%A0%95-%EA%B5%AC%EA%B0%84%EC%9D%98-%ED%95%A9/quiz/1
GOORM SLICE SUM
*/

#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int array[n];
	for (int i=0;i<n;i++)
		cin >> array[i];
	int slice[2];
	cin >> slice[0] >> slice[1];
	
	int sum = 0;
	for(int i=slice[0]-1; i<slice[1]; i++){
		sum += array[i];
	}
	cout << sum <<endl;
	return 0;
}

/*
TC1
5
2 6 8 9 10
2 4
=> 23

TC2
4
555 392 1823 234951
2 4
=> 237166
*/