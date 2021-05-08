#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
    // 1 단계
    for(int i = 0; i < new_id.length(); i++)
        new_id[i] = tolower(new_id[i]);
    
    // 2 단계
    for(int i = 0; i < new_id.length(); ) {
        if ((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9')
              || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.')
        {
            i++;
            continue;
        }
        
        new_id.erase(new_id.begin() + i);
    }
    
    // 3 단계
    for(int i = 1; i < new_id.length(); ){
        if (new_id[i] == '.' && new_id[i - 1] == '.'){
            new_id.erase(new_id.begin() + i);
            continue;
        }
        else i++;
    }
    
    // 4단계
    if(new_id.front() == '.') new_id.erase(new_id.begin());
    if(new_id.back() == '.') new_id.erase(new_id.end()-1);
    
    // 5단계
    if(new_id.length() == 0) new_id = "aaa";
    
    // 6단계
    while(new_id.length() >= 16) new_id.erase(new_id.begin()+15);
    if(new_id.back() == '.') new_id.erase(new_id.end()-1);
    
    // 7단계
    if (new_id.length() <= 2)
    while(new_id.length() <3) new_id += new_id.back();
    
    
    return new_id;
}

int main(void){
    string prob1 = "...!@BaT#*..y.abcdefghijklm";
    string prob2 = "z-+.^.";
    string prob3 = "=.=";
    string prob4 = "123_.def";
    string prob5 = "abcdefghijklmn.p";

    if(solution(prob1) == "bat.y.abcdefghi") cout << "rignt"<<endl;
    if(solution(prob2) == "z--") cout << "right" << endl;
    if(solution(prob3) == "aaa") cout << "right" << endl;;
    if(solution(prob4) == "123_.def") cout << "right" << endl;;
    if(solution(prob5) == "abcdefghijklmn") cout << "right" << endl;;
}