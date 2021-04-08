/*
programmers 탐욕법(Greedy) 체육복
https://programmers.co.kr/learn/courses/30/parts/12081
*/

public class gym {
    public static void main(String[] args){
        // Test Case 1
        // int n=5;
        // int[] lost = {2,4};
        // int[] reserve = {1,3,5};

        // My Test Case
        int n=10;
        int[] lost = {3,9,10};
        int[] reserve = {3,8,9};

        gym_Solution gym = new gym_Solution();
        int answer = gym.solution(n, lost, reserve);

        System.out.println(answer);
    }
}
class gym_Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        for(int i=0;i<lost.length;i++)
            for(int j=0;j<reserve.length;j++)
                if(lost[i] == reserve[j]){ // 여벌이 있는데 잃어버린 학생
                    lost[i] = -1;
                    reserve[j] = -1;
                    break;
                }
        
        for(int i=0;i<lost.length;i++)
            for(int j=0;j<reserve.length;j++)
                if(lost[i]-1 == reserve[j]){ // 잃어버렸는데 여벌이 있는 학생에게 빌림
                    lost[i] = -1;
                    reserve[j] = -1;
                    break;
                }else if(lost[i]+1 == reserve[j]){ // 잃어버렸는데 여벌이 있는 학생에게 빌림
                    lost[i] = -1;
                    reserve[j] = -1;
                    break;
                }

        // 잃어버렸는데 빌리지도 못한 학생 카운트
        int count=0;
        for(int i=0;i<lost.length;i++)
            if(lost[i] != -1) count++;
        
        int answer = n - count;
        return answer;
    }
}