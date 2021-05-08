#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string s) {
    string str0 = "zero";
    string str1 = "one";
    string str2 = "two";
    string str3 = "three";
    string str4 = "four";
    string str5 = "five";
    string str6 = "six";
    string str7 = "seven";
    string str8 = "eight";
    string str9 = "nine";
    
    int n=0;
    // one two three ... 계속 비교해서 숫자 치환
    while(n<50){
        n++;
        int location0 = s.find(str0);
        
        if(location0 != std::string::npos)
            s.replace(location0, str0.length(), "0");
        
        int location1 = s.find(str1);

        if(location1 != std::string::npos)
            s.replace(location1, str1.length(), "1");
        
        int location2 = s.find(str2);

        if(location2 != std::string::npos)
            s.replace(location2, str2.length(), "2");
        
        int location3 = s.find(str3);

        if(location3 != std::string::npos)
            s.replace(location3, str3.length(), "3");
        
        int location4 = s.find(str4);

        if(location4 != std::string::npos)
            s.replace(location4, str4.length(), "4");
        
        int location5 = s.find(str5);

        if(location5 != std::string::npos)
            s.replace(location5, str5.length(), "5");
        
        int location6 = s.find(str6);

        if(location6 != std::string::npos)
            s.replace(location6, str6.length(), "6");
        
        int location7 = s.find(str7);

        if(location7 != std::string::npos)
            s.replace(location7, str7.length(), "7");
        
        int location8 = s.find(str8);

        if(location8 != std::string::npos)
            s.replace(location8, str8.length(), "8");
        
        int location9 = s.find(str9);

        if(location9 != std::string::npos)
            s.replace(location9, str9.length(), "9");
    }
 
    
    int answer = 0;
    
    answer = stoi(s);

    return answer;
}