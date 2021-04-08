/*
programmers 스택/큐 기능개발
https://programmers.co.kr/learn/courses/30/parts/12081
*/

import java.util.LinkedList;
import java.util.Queue;

class functionDvel_Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int data_size = progresses.length;
        Queue<Integer> queue = new LinkedList<>();
        
        // 각 작업의 남은 일수 큐에 저장
        for(int i=0;i<data_size;i++){
            if((100 - progresses[i])%speeds[i] > 0){
                queue.add((100 - progresses[i])/speeds[i] + 1);
            } else{
                queue.add((100 - progresses[i])/speeds[i]);
            }
        }

        int[] temp = new int[queue.size()];

        int i=0;
        while(!queue.isEmpty()){
            int count = 1;
            int front_data = queue.poll();
            
            while(!queue.isEmpty())
                if(front_data >= queue.peek()) {
                    count++;
                    queue.remove();
                } else break;
            temp[i] = count;
            i++;
        }

        int[] answer = new int[i];
        for(int j=0;j<i;j++)
            answer[j] = temp[j];
        return answer;
    }
}

public class functionDvel {
    public static void main(String[] args){
        // Test Case 1
        // int[] progresses = {93, 30, 55};
        // int[] speeds = {1,30,5};

        // Test Case 2
        int[] progresses = {95, 90, 99, 99, 80, 99};
        int[] speeds = {1, 1, 1, 1, 1, 1};

        functionDvel_Solution function = new functionDvel_Solution();
        int[] answer = function.solution(progresses, speeds);

        for(int i=0;i<answer.length;i++)
            System.out.println(answer[i]);
    }    
}