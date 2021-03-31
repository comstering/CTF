# Toddler's Bottle - bof

### Problem
![image](https://user-images.githubusercontent.com/53170968/113155335-e2450300-9273-11eb-8c4c-f15c3a167658.png)

### Solution
1. 앞쪽 문제와 다르게 파일을 다운받아서 진행해야한다. 진행해보자.

![image](https://user-images.githubusercontent.com/53170968/113155456-ff79d180-9273-11eb-8936-7a2e1836b165.png)

![image](https://user-images.githubusercontent.com/53170968/113155465-030d5880-9274-11eb-82a9-37552397b29d.png)

2. wget으로 파일을 다운 받자.

![image](https://user-images.githubusercontent.com/53170968/113155529-128ca180-9274-11eb-84bc-efaae0e59f10.png)

3. 그리고 소스파일을 확인해보자.

4. 소스코드의 내용은 정말 간단하다. key의 값이 0xcafebabe와 동일하면 쉘권한을 획득할 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113155652-3b149b80-9274-11eb-8824-9500366d458d.png)

5. 실행파일인 bof의 권한을 변경해주자.

![image](https://user-images.githubusercontent.com/53170968/113155722-4b2c7b00-9274-11eb-99dd-964d5b586983.png)

6. 그리고 gdb로 실행해서 분석해보자.

![image](https://user-images.githubusercontent.com/53170968/113155852-7020ee00-9274-11eb-8eff-1ee1669c6920.png)

7. main함수는 별다른 것 없다. func함수를 호출하는데 매개변수로 0xdeadbeef를 주는 것 뿐이다. func함수를 살펴보자.

![image](https://user-images.githubusercontent.com/53170968/113155955-875fdb80-9274-11eb-88af-41ddfb689fee.png)

![image](https://user-images.githubusercontent.com/53170968/113155962-89299f00-9274-11eb-8456-bef4efe111a7.png)

8. 여러 함수들이 존재한다. 소스코드와 비교해서 보면 첫 func+25는 printf함수이다.

9. 두번째 func+36은 gets함수로 우리는 저 함수에서 데이터를 입력한다.

10. 세번째 func+63은 if문으로 보인다.  

11. 우리는 저 두번째 func+36의 gets함수를 통해서 BOF를 일으켜서 key의 데이터를 바꿔야한다.

12. overflowme변수의 메모리를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113156375-e45b9180-9274-11eb-8643-a1847be4ab5a.png)

13. 메모리를 보는데 익숙한 데이터가 보인다. 바로 key에 저장되었던 deadbeef이다. 바로 저 위치가 key변수의 메모리 위치이다.

![image](https://user-images.githubusercontent.com/53170968/113156486-01906000-9275-11eb-95d3-14affffb7435.png)

14. A를 20개 입력해보았다. 메모리에 저장된 데이터가 바뀐 것을 볼 수 있다.

15. key의 메모리 위치까지는 52Byte가 필요하다. 즉, 52Byte를 다른 데이터로 입력하고 key의 위치에 들어갈 0xcafebabe를 추가해서 입력하면 해당 문제는 해결된다.

![image](https://user-images.githubusercontent.com/53170968/113156749-3e5c5700-9275-11eb-90ae-53a387ea0748.png)

16. 위에서 생각한 대로 데이터를 입력했다. 물론 cafebabe를 입력할 때는 리틀엔디안을 생각해서 1Byte단위로 역순으로 넣어야한다.

17. if문에서 else문이 실행되어서 'Nah...'이 출력되지는 않았는데 프로그램이 종료되었다.

18. 무엇이 문제인지는 모르겠지만 로컬에서는 동작하지 않는 게 조금 많은 것 같다.

19. 바로 그냥 서버 host로 접속해서 문제를 풀어보자.

20. exploit을 만들어서 실행해보자. solution.py파일로 만들었다.

![image](https://user-images.githubusercontent.com/53170968/113157220-a743cf00-9275-11eb-9bfb-a617cbc0bebd.png)

21. 로컬에서 안 됬었던 것과는 다르게 잘 쉘권한을 획득했다.

22. flag파일을 확인해서 FLAG를 얻었다.

![image](https://user-images.githubusercontent.com/53170968/113157400-d2c6b980-9275-11eb-8a34-f7ff77c54809.png)

![image](https://user-images.githubusercontent.com/53170968/113157412-d4907d00-9275-11eb-9231-56ed4e6b64d4.png)

23. 사이트에서 제출하니 정답처리되었다.