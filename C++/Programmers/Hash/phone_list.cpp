/*
https://programmers.co.kr/learn/courses/30/parts/12077
PROGRAMMERS HASH Phone Book
*/

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());

    for(int i=0; i< phone_book.size()-1; i++)
        if(phone_book[i] == phone_book[i+1].substr(0, phone_book[i].size())) return false;
    
    return true;
}

/*
// 히든테케 다 통과하는데 효율성 반만 통과해서 구글링한 결과 길이 순으로 정렬하지 않고, 사전 순으로 정렬하면 인접 인덱스만 비교하면 된다는 것을 알게되었다.
bool compare (string a, string b) {
    return a.size() < b.size();
}
bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end(), compare);
    
    for (int i=0;i<phone_book.size()-1;i++){
        for(int j=i+1;j<phone_book.size();j++){
            if (phone_book[i] == phone_book[j].substr(0, phone_book[i].size()))
                return false;
        }
    }
  
    return true;
}*/

int main(void){
    vector<string> phone_book1{"119", "97674223", "1195524421"};
    vector<string> phone_book2{"123", "456", "789"};
    vector<string> phone_book3{"12", "123", "1235", "567", "88"};
    vector<string> phone_book4{"113333", "115555", "345555", "555555", "345444"};

    if(solution(phone_book1)==false) cout<<"RIGHT1"<<endl;
    if(solution(phone_book2)==true) cout<<"RIGHT2"<<endl;
    if(solution(phone_book3)==false) cout<<"RIGHT3"<<endl;
    if(solution(phone_book4)==true) cout<<"RIGHT4"<<endl;
}