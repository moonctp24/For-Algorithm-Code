#include <iostream>
#include <vector>
using namespace std;
int main(void) {
	int n;
	cin >> n;
	vector<string> stk;
	for(int i=0;i<n;i++){
		int tmp;
		cin >> tmp;
		
		if(tmp == 0){
			if (stk.size()==10) cout << "overflow"<<endl;
			else{
				int tmp2;
				cin >> tmp2;
				stk.push_back(to_string(tmp2));
			}
		}
		else if (tmp == 1){
			if (stk.size()==0) cout << "underflow"<<endl;
			else stk.pop_back();
		}
        else break;
	}
	for(int i=0;i<stk.size();i++){
        cout << stk[i]<<" ";
	}
}