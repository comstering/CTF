# Combat Ship Reversing Exam 3: Tracing strings

### Problem
    It is time for the third exam of the Combat Ship Reversing Programme. Take the following binary file. It is a patched version of the previous one. Good luck!

    Combat Ship Reversing Exam 3 binary.
    
    When you have reversed the binary and is ready for the real deal, please connect to the remote with the netcat command:

    nc combatship3.tghack.no 5001

### Solution
1. 이번 문제는 앞선 Reversing Exam 2 파일의 패치버전을 똑같이 리버싱해서 답을 도출하는 것 같다.

2. 역시나 파일을 툴에 오픈하자.

![image](https://user-images.githubusercontent.com/53170968/95325436-2c0fea80-08dc-11eb-8541-94420d301137.png)

![image](https://user-images.githubusercontent.com/53170968/95325501-40ec7e00-08dc-11eb-820e-5900be742b72.png)

3. 파일 내용을 보니 앞선 문제와 똑같은 것 같다.

4. 질문 4개를 알아보고 4개의 답을 구하면 FLAG를 주는 것 같다.

5. 그럼 바로 4개의 질문과 답을 구해보자

6. q1의 질문은 Give me the captain's name? 이다 앞선 문제와 같다.

![image](https://user-images.githubusercontent.com/53170968/95325722-92950880-08dc-11eb-87ec-68465228aa27.png)

7. 답을 보자.

![image](https://user-images.githubusercontent.com/53170968/95325739-97f25300-08dc-11eb-95a5-4d66fd63b6a8.png)

8. Captain noco라고 한다. 바로 q2로 가보자

![image](https://user-images.githubusercontent.com/53170968/95326031-f0295500-08dc-11eb-9651-b2824bda5ad4.png)

9. 질문이 How much starpower does the Starfleet have? 이다. 답도 바로 확인하자.

![image](https://user-images.githubusercontent.com/53170968/95326189-2666d480-08dd-11eb-8d7b-0f224796a31b.png)

10. 답이 3205076259^42이다. 다음은 q3~~~

![image](https://user-images.githubusercontent.com/53170968/95326243-3a123b00-08dd-11eb-9224-034d3da62f08.png)

![image](https://user-images.githubusercontent.com/53170968/95326271-472f2a00-08dd-11eb-8177-67cfeaa1b31f.png)

11. 질문은 What year is this?이고 그에 해당하는 답은 4113이다.

12. 마지막으로 q4!!

![image](https://user-images.githubusercontent.com/53170968/95326411-8198c700-08dd-11eb-8e54-5b46220e37a4.png)

![image](https://user-images.githubusercontent.com/53170968/95326332-5e6e1780-08dd-11eb-81fc-eea7a699afcc.png)

13. 질문은 How many tonnes of cyber weapon is onboard on the main Starfleet?이고 답은 701710아다.

14.  앞선 Reversing Exam 2에서 질문은 그대로고 그에 해당하는 답만 다른 것 같다.

15.  해당 문제 네트워크에 접속해서 FLAG를 얻어보자!!

![image](https://user-images.githubusercontent.com/53170968/95326726-fbc94b80-08dd-11eb-97f3-7f738ab66e0c.png)

16. 첫 질문이 나왔다. 입력하고 나머지 3개의 질문에도 답을 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/95327106-8447ec00-08de-11eb-9ef5-22454a805277.png)

17. FLAG가 나왔다. Reversing Exam 2의 문제를 똑같이 해봐서 손에 익숙해지게하는 문제였던 것 같다.

18. FLAG가 나왔으니 바로 답을 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/95327334-d5f07680-08de-11eb-8721-20465851dad7.png)

19. 정답처리 되었다!!!