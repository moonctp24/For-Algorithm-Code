/*
programmers 정렬 H-Index
https://programmers.co.kr/learn/courses/30/parts/12198
*/


import java.util.Arrays;

class Hindex_Solution {
    public int solution(int[] citations) {
        // 과학자가 발표한 논문의 수 오름차순 정렬
        Arrays.sort(citations);
        
        int leng = citations.length;
        
        int answer =0;
        for(int i=leng-1;i>=0;i--)
            if(i+1 <= citations[leng-i-1]){
                answer = i+1;
                break;
            }
        
        return answer;
    }
}

public class Hindex {
    public static void main(String[] args){
        // Test Case 1
        // int[] citations = {3, 0, 6, 1, 5};

        // My Test Case 1
        int[] citations = {8, 9, 5, 6, 0, 2, 10};

        // My Test Case 2
        // int[] citations = {5, 5, 5, 5};

        Hindex_Solution hindex = new Hindex_Solution();
        int answer = hindex.solution(citations);

        System.out.println(answer);
    }
}
