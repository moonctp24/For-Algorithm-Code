/*
정규 표현식을 작성하는 방법은 자바 API java.util.regex 패키지를 사용
자바에서 정규표현식을 사용할때에는 java.util.regex 패키지 안에 있는 Pattern클래스와 Matcher클래스를 주로 사용

1. Pattern 클래스
정규 표현식에 대상 문자열을 검증하는 기능은 java.util.rege.Pattern 클래스의 matches()메소드를 활용하여 검증
matches() 메서드의 첫번째 매개값은 정규표현식이고 두번째 매개값은 검증 대상 문자열
검증 후 대상문자열이 정규표현식과 일치하면 true, 그렇지 않다면 false값을 리턴
 */

import java.util.regex.Pattern;

public class Using_pattern {
	public static void main(String[] args)  {
    
            String pattern = "^[0-9]*$"; //숫자만
            String val = "123456789"; //대상문자열
        
            boolean regex = Pattern.matches(pattern, val);
            System.out.println(regex);
    }
}