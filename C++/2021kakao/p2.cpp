#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer(places.size(), -1);

    for(int i=0;i<places.size();i++){
        for(int j=0;j<places[i].size();j++){
            for(int z=0;z<places[i][j].size();j++){
                if(places[i][j][z] == 'P'){
                    if(j>0 && z>0 && places[i][j-1][z-1] == 'X' || places[i][j-1][z-1] == 'P') {answer[i] = 0; break;}
                    if(z>0 && places[i][j-1][z] == 'X' || places[i][j-1][z] == 'P') {answer[i] = 0; break;}
                    if(j>0 && z<places[i].size() -1 && places[i][j-1][z+1] == 'X' || places[i][j-1][z+1] == 'P') {answer[i] = 0; break;}
                    if(j>0 && places[i][j][z-1] == 'X' || places[i][j][z-1] == 'P') {answer[i] = 0; break;}
                    if(j<places[i].size()-1 && places[i][j][z+1] == 'X' || places[i][j][z+1] == 'P') {answer[i] = 0; break;}
                    if(j<places[i].size()-1 && z>0 && places[i][j+1][z-1] == 'X' || places[i][j+1][z-1] == 'P') {answer[i] = 0; break;}
                    if(j<places[i].size()-1 && places[i][j+1][z] == 'X' || places[i][j+1][z] == 'P') {answer[i] = 0; break;}
                    if(j<places[i].size()-1 && z<places[i].size()-1 && places[i][j+1][z+1] == 'X' || places[i][j+1][z+1] == 'P') {answer[i] = 0; break;}
                } 
            } if(answer[i] == 0) break;
        } if(answer[i] == -1) answer[i] = 1;
    }
    
    return answer;
}

// TEST CASE부터 통과 못함