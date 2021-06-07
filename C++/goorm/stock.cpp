/*
https://level.goorm.io/exam/100817/15%ED%9A%8C-e-pper-3%EB%B2%88/quiz/1
GOORM THE OUT OF STOCK
*/

#include <iostream>
using namespace std;
int main() {
	int n;
	int m;
	cin >> n >> m;
	// 무조건 재고가 0이되는 날이 있을 경우 써야함
	int day = 0;
	while (true){
		// terminal condition
		if (n==0) break;
		day++;
		n--; // 1day 1sell
		if (day%m == 0)
		 n++;
	}
	cout << day << endl;
	return 0;
}

/*
TC1
2 2 => 3

TC2
9 3 => 13

TC3
7 2 => 13
*/