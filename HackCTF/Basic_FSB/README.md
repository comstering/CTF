# Basic_FSB

### Problem
![image](https://user-images.githubusercontent.com/53170968/113080991-cb21f900-9212-11eb-966c-60b185dec205.png)

### Solution
1. 파일을 다운 받아서 실행권한을 주어서 파일을 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/113081014-d7a65180-9212-11eb-8717-7c93b65ad322.png)

2. 실행 결과로는 내가 입력한 문자열을 그냥 그대로 출력해주는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113081114-08868680-9213-11eb-83a6-e638508d74f8.png)

3. gdb를 이용해서 파일을 분석해보자.

![image](https://user-images.githubusercontent.com/53170968/113081257-4aafc800-9213-11eb-805b-4ae74047bb1e.png)

4. main함수를 먼저 확인해 봤다.

5. 눈에 띄는 함수 2개가 있다. sevbuf함수와 vuln함수이다.

6. sevbuf함수는 입력버퍼를 설정하는 함수인데 매개변수로 0x2가 3번째 인자로 들가는 것을 볼 수 있다.

7. sevbuf의 3번째 인자는 버퍼를 설정하는 mode이다.

8. _IOFBF: 완전 버퍼링, _IOLFBF: 행 버퍼링, _IONBF: 버퍼링 사용안함.

9. 각 mode에 별 정수 값을 확인해보자.


    #include <stdio.h>

    int main(void)
    {
    	printf("%x %x %x \n", _IOFBF, _IOLBF, _IONBF);
    	return 0;
    }


![image](https://user-images.githubusercontent.com/53170968/113132687-c2084a80-9259-11eb-9483-d9a0f5252b02.png)

10. _IOFBF = 0, _IOLBF = 1, _IONBF = 2인 것을 확인 할 수 있다.

11. sevbuf의 모드는 버퍼를 사용하지 않는 것으로 설정되어 있는 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113132864-f845ca00-9259-11eb-9020-0188e091e7bc.png)

12. 다음으로 vuln함수를 확인해보자.

13. 크게 4개의 함수가 보인다. printf, fgets, snprintf, printf

14. 첫번째 printf는 'input : '을 출력해주는 함수이다.

15. 그리고 두번째 fgets는 내가 데이터를 입력하는 함수이다.

16. 그리고 snprintf는 서식지정자를 이용해서 새로운 문자열을 만들어주는 함수이다.

17. 그리고 마지막 printf는 입력한 문자열을 출력해주는 함수이다.

18. 여기서 printf와 snprintf에는 FSB(Format String Bug)라는 취약점이 존재한다.

19. 출력하는 문자열에 서식지정자가 있다면 해당 서식지정자가 실행되는 버그이다.

![image](https://user-images.githubusercontent.com/53170968/113135368-03e6c000-925d-11eb-962c-3822d168e0d2.png)

![image](https://user-images.githubusercontent.com/53170968/113135375-05b08380-925d-11eb-91b3-8e503de43d39.png)

20. 이렇게 %x를 이용해서 출력결과를 확인해보면 AAAA의 아스키코드값이 16진수형태로 출력되는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113135487-24af1580-925d-11eb-9d12-8fa119776a71.png)

21. 그리고 info function으로 해당 파일의 함수 목록을 확인해보면 flag라는 함수가 존재하는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113135598-41e3e400-925d-11eb-9614-1007b6f00792.png)

22. flag함수의 내용을 보면 system함수를 호출하는 것을 볼 수 있다.

23. 저 함수로 인해 쉘권한을 얻을 수 있게 될 것 같다.

24. 우리의 목표는 FSB를 이용해서 저 flag함수를 실행시키는 것이 될 것이다.

![image](https://user-images.githubusercontent.com/53170968/113135740-7192ec00-925d-11eb-9e21-e07f34436a24.png)

25. printf함수를 확인해보면 함수가 호출되지 마자 0x804a00c의 메모리 위치로 jump한다.

26. printf함수가 호출될 때 이동하는 저 0x804a00c의 값을 flag함수의 주소값으로 바꾸어서 printf함수가 호출되면 flag함수가 호출되도록 하면 이번 문제를 풀 수 있다.

27. 여기어 FSB가 일어나는 지점은 snpirntf이다.

28. exlpoit을 만들어서 실행시켜보자.

29. pwntools를 이용해서 FSB를 일으켜서 0x804a00c의 위치에 flag함수의 주소값인 0x080485b4를 넣어보자.

30. 해당 주소값에 데이터를 넣는 방법은 %x와 %n을 이용하면 된다.

31. '0x804a00c%x%n'이러한 형식으로 데이터입력하면 된다.

32. 이때 %n으로 특정 주소에 데이터를 넣을 때는 %n의 앞쪽에 존재하는 문자열의 개수(크기)값이 주소값의 데이터로 저장된다.

![image](https://user-images.githubusercontent.com/53170968/113140970-157f9600-9264-11eb-8e84-432c504b4be2.png)

33. pwntools를 이용해서 만든 solution.py exploit을 실행해보면 고격에 성공한 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113141142-4d86d900-9264-11eb-92e6-38d7ef1a11ed.png)

![image](https://user-images.githubusercontent.com/53170968/113141259-714a1f00-9264-11eb-98af-7b9e28ba05b8.png)

![image](https://user-images.githubusercontent.com/53170968/113141274-760ed300-9264-11eb-8228-3f17374e8a65.png)

35. 이렇게 정답 처리 되었다.