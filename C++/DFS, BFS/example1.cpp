// 최대공약수 계산 (유클리드 호제법) 예제


#include <iostream>

using namespace std;

int gcd(int a, int b){
    if(a%b == 0) return b;
    else return gcd(b, a%b);
}

int main(){
    cout<< gcd(192,162) << endl;
}
