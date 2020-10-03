# Combat Ship Reversing Exam 1: Strings

### Problem
    We found this old, stranded combat ship. Can you help us reverse engineer this binary file to find some juicy stuff? Combat Ship Reversing Exam 1 binary.

### Solution
1. 이번 문제는 처음으로 해보는 리버스엔지니어링이다. 문제에서 리버스엔지니어링을 해서 FLAG를 얻으라고 한다.

2. 그럼 필요한 툴부터 구해보자.

![image](https://user-images.githubusercontent.com/53170968/94998893-4bfb9180-05f0-11eb-87bd-4ed86a3dd888.png)

3. 리버싱 툴 중에서 가장 많이 알려진 IDA를 다운받았다.

4. 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/94998994-0f7c6580-05f1-11eb-9317-49b4032912ea.png)

5. 문제이 있던 파일을 다운 받아서 IDA에 파일을 오픈한다.

![image](https://user-images.githubusercontent.com/53170968/94999026-48b4d580-05f1-11eb-9344-3c8641145b31.png)

6. 모르는 화면이 나왔다. 일단 처음 리버스엔지니어링을 하니 ok버튼을 눌러서 일단 디버깅분석을 해보겠다.

![image](https://user-images.githubusercontent.com/53170968/94999053-7732b080-05f1-11eb-9423-5019d8995bd2.png)

7. 가장 메인인 것 같은 화면에 해당 파일의 메인 함수 동작이 어셈블리어로 적혀있다.

8. 그리고 여러 창이 있는데 2번째 Hex View-1화면을 보자

![image](https://user-images.githubusercontent.com/53170968/94999095-ec9e8100-05f1-11eb-911e-8fe03bbe65c2.png)

9. 처음에는 그냥 코드들이 16진수로 표현되어있는 형태인 줄로만 알았는데 오른쪽에 파란글씨로 16진수를 번역해서 적어놓은 것 같다.

10. 번역해서 적어놓은 곳에 TG20이라고 현재까지 FLAG를 입력하기 위해 필요했던 선언문이 적혀있다.

11. 이번 문제는 정말 리버스엔지니어링 입문으로 툴에 오픈만하면 답이 나오는 문제인가보다.

12. FLAG가 눈에 보이니 바로 답을 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/94999185-bc0b1700-05f2-11eb-893a-55aaa36d82a0.png)

13. 정답이다!! 이 문제는 정말 입문과정으로 리버싱툴을 써보도록 하는 문제인 것 같다.

14.  처음 해보는 리버스엔지니어링인데 많이 신기하다. 다른 문제들도 한번 많이 풀어봐야겠다.