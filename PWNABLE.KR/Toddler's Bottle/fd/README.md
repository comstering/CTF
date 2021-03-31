# Toddler's Bottle - fd

### Problem
![image](https://user-images.githubusercontent.com/53170968/113148211-8dea5500-926c-11eb-85b0-06ac3fe8afe9.png)

### Solution
1. shh로 해당 host에 접속해서 문제를 풀어보도록 하자.

![image](https://user-images.githubusercontent.com/53170968/113148424-c853f200-926c-11eb-8eb5-5c8ad957efb7.png)

2. shh로 host에 접속했다.

![image](https://user-images.githubusercontent.com/53170968/113148543-e91c4780-926c-11eb-94bc-5f1c6a2957cb.png)

3. 존재는 파일을 확인했다.

4. flag라는 파일이 존재하지만 실행할 수 있는 권한이 없다. 아마 fd를 실행해서 저 flag를 실행시켜야 될 것 같다.

5. fd파일의 소스파일인 fd.c파일을 분석해보자.

![image](https://user-images.githubusercontent.com/53170968/113148836-4ca67500-926d-11eb-8a2c-bac5fd2d05fe.png)

6. 소스코드를 확인해보면 첫 if문에 argc가 2보다 작으면 바로 return되는 것을 볼 수 있다. 즉 실행할 때 매개변수와 함께 실행해야한다.

![image](https://user-images.githubusercontent.com/53170968/113148975-7790c900-926d-11eb-9303-22b51a8cc5ee.png)

7. 그리고 다음 코드를 보면 atoi를 통해서 입력받은 문자열을 정수로 변환하고 그 정수를 0x1234로 뺀다.

8. 그리고 그 결과를 fd변수에 저장한다. 즉, 우리는 매개변수로 정수값을 입력해야한다.

![image](https://user-images.githubusercontent.com/53170968/113149507-0dc4ef00-926e-11eb-9b5b-39cf3bd519b3.png)

9. 다음 코드를 보면 len에 read함수의 결과를 저장한다. read함수에서는 buf에 32Byte만큼의 데이터를 저장한다.

10. fd는 위에서 우리가 입력한 매개변수와 0x1234를 뺀 데이터가 저장되어 있다.

11. 여기서 read함수에 fd의 값이 0으로 입력되면 표준입력을 진행한다.

12. 즉, fd의 값을 0으로 만들어서 표준입력을 진행할 수 있게 해야한다.

![image](https://user-images.githubusercontent.com/53170968/113150168-becb8980-926e-11eb-80c3-1d57784235e7.png)

13. 그리고 다음 if문을 확인해보면 buf와 'LETMEWIN'을 비교한다. 비교 결과가 같으면 해당 if문이 실행된다.

14. 그리고 if문 내부를 보면 system함수로 flag파일의 내용을 출력해준다.

15. 즉, read를 표준입력으로 하도록 하여 buf에 LETMEWIN을 넣으면 flag 파일이 실행되어 FLAG를 얻을 수 있게 되는 것이다.

16. 그렇다면 실행해보도록 하자.

17. 먼저 0x1234를 10진수로 바꾸면 4660이다. fd파일을 실행할 때 4660을 같이 입력하고 실행하자.

18. 그리고 표준입력이 되면 LETMEWIN을 입력하도록 하자.

![image](https://user-images.githubusercontent.com/53170968/113150766-61840800-926f-11eb-91a1-6cc779209fe7.png)

19. 이렇게 FLAG를 얻을 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113150856-7791c880-926f-11eb-9ba0-292871f1fff3.png)

![image](https://user-images.githubusercontent.com/53170968/113150867-795b8c00-926f-11eb-9154-896baf7c1b4b.png)

20. 이렇게 정답처리가 되었다.