# Combat Ship Reversing Exam 2: Tracing

### Problem
    This old Combat Ship software has some weird validation question you need the answers for to get access. Can you find the answers?

    Combat Ship Reversing Exam 2 binary.
    
    When you have reversed the binary and is ready for the real deal, please connect to the remote with the netcat command:

    nc combatship2.tghack.no 5000

### Solution
1. 이번 문제는 해당파일을 분석하여 어떠한 답을 찾아서 결과를 얻는 것 같다.

2. 그럼 먼저 파일을 툴에 오픈하자.

![image](https://user-images.githubusercontent.com/53170968/94999958-f4f9ba80-05f7-11eb-9ff6-f2fd359279c5.png)

3. 그리고 아직 질문이 뭔지를 모르니 질문도 한번 알아보자.

![image](https://user-images.githubusercontent.com/53170968/95000021-3d18dd00-05f8-11eb-87be-6ab9c3390157.png)

4. captain 이름이 뭔지 물어본다.

5. 다시 분석도구로 돌아가서

6. 코드를 순서대로보니 위에서 nc로 접속한 문제의 질문들이 표시되어 있다.

7. 그러면 Give me the captain's name?이 있는 곳을 찾아보자

![image](https://user-images.githubusercontent.com/53170968/95000048-65084080-05f8-11eb-877f-fd12382307be.png)

8. 함수 q1에 해당하는 내용을 보니 해당내용이 있다. 나오는 결과를 보니 answer_captain42 값인 것 같다.

![image](https://user-images.githubusercontent.com/53170968/95000052-6f2a3f00-05f8-11eb-9a32-d40adc02367b.png)

9. 해당 값과 일치하는 captain이름을 보니 captain bolbz이다.

10. 한번 nc에 연결한 질문에 답을 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/95000135-33dc4000-05f9-11eb-9131-267d00ded3c6.png)

11. 질문의 답을 입력하니 바로 다음 질문이 나왔다.

12. 다시 코드들을 보니 함수 q1, q2, q3, q4가 질문들인 것 같다.

13. 즉 각각에 해당하는 답을 다 찾아서 다입력하면 마지막으로 print_flag함수로 FLAG가 나오는 것 같다.

14.  그러면 바로 각각의 답을 다 찾아보자.

15.  먼저 q2부터 알아보겠다.

![image](https://user-images.githubusercontent.com/53170968/95000169-8ddd0580-05f9-11eb-97c1-0b70856b7f21.png)

16. 질문은 how much starpower does the starfleet haver? 이다. answer_starpower5의 값을 보자.

![image](https://user-images.githubusercontent.com/53170968/95000174-95041380-05f9-11eb-9cba-d7ef3ceed62f.png)

17. answer_starpower5 = 4200000000^42이다.

18. 다음은 q3이다. 질문은 What year is this?이다.

![image](https://user-images.githubusercontent.com/53170968/95000180-a0573f00-05f9-11eb-80f0-397464e71761.png)

19. q3의 답도 알아보자.

![image](https://user-images.githubusercontent.com/53170968/95000184-a5b48980-05f9-11eb-80d3-363c55c44ec2.png)

20. 2820이다.

21. 마지막으로 q4이다. 

![image](https://user-images.githubusercontent.com/53170968/95000187-abaa6a80-05f9-11eb-878b-18500fad1149.png)

22. q4의 질문은 How many tonnes of cyber weapon is onboard on the main Starfleet?이다.

![image](https://user-images.githubusercontent.com/53170968/95000190-b06f1e80-05f9-11eb-9621-7d8cc98a048d.png)

23. 질문에 해당하는 답은 133700이다.

24. 그럼 질문도 알고 질문에 해당하는 답들도 전부다 알았으니 바로 전부 다 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/95000343-f24c9480-05fa-11eb-9269-4cfba23591af.png)

25. 질문에 해당하는 답을 다 입력했더니 FLAG가 나왔다. FLAG를 입력해보자.
26. 
![image](https://user-images.githubusercontent.com/53170968/95000376-317ae580-05fb-11eb-9abf-ce90bd1313c8.png)

26. 정답이다!! 이번 문제를 풀면서 리버싱툴이 어떠한 툴인지 어떠한 방법으로 사용을 할 수 있는지 알게 되었다.