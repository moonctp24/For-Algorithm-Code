#include <iostream>
#include <vector>
using namespace std;
int main() {
	vector<char> stk;
	string str;
	cin >> str;

	for(int i=0;i<str.length();i++){
		if(str[i] == ')')
			if(stk.back() == '(')
				stk.pop_back();
			else {
				cout << "False"<<endl;
				break;}
		else if (str[i] == '}')
			if(stk.back() == '{')
				stk.pop_back();
			else {
				cout << "False"<<endl;
				break;}
		else if (str[i] == ']')
			if(stk.back() == '[')
				stk.pop_back();
			else {
				cout << "False"<<endl;
				break;}
		else
			stk.push_back(str[i]);
	}
	
	if(stk.size() == 0) cout << "True"<<endl;
}