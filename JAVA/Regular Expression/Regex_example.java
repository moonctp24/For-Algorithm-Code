/* 
정규표현식은 유효성 검사 코드 작성 시 가장 효율적인 방법이다.
출처: https://coding-factory.tistory.com/529
*/

import java.util.regex.Pattern;

public class Regex_example {
    public static void main(String[] args)  {
        String name = "홍길동";
        String tel = "010-1234-5678";
        String email = "test@naver.com";
       
        //유효성 검사
        boolean name_check = Pattern.matches("^[가-힣]*$", name);
        boolean tel_check = Pattern.matches("^01(?:0|1|[6-9])-(?:\\d{3}|\\d{4})-\\d{4}$", tel);
        boolean email_check = Pattern.matches("\\w+@\\w+\\.\\w+(\\.\\w+)?", email);

        //출력
        System.out.println("이름 : " + name_check);
        System.out.println("전화번호 : " + tel_check);
        System.out.println("이메일 : " + email_check);
    }
}
