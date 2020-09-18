# Baby's First Assembly Code

### Problem
    Zero out the rax register. Which means you have to set rax to 0. That's it!

    nc shellcode.tghack.no 1111
    
    Note: This is level 1. End your assembly code with a line containing EOF.

### Solution
1. 이 문제는 일단 제목에서 어셈블리코드를 이용한다고 나와있다.

2. nc shellcode.tghack.no 1111 는 윈도우 cmd 환경이나 리눅스에서 nc 명령어로 해당 주로로 접근 하라는 뜻이다.

3. 나는 라즈베리파이에서 접근하였기에 리눅스환경에서 접근했다.

![problem](https://user-images.githubusercontent.com/53170968/93592065-78a68b00-f9ec-11ea-9f08-e903a4851b67.png)

4. Level이 1이므로 1로 입력하고 문제로 진입했다.

5. 문제에서 그냥 바로 답을 알려줬다. rax 레지스터를 그냥 0으로 set하면 끝이라고 한다.

6. Note와 연결된 문제에서 나와있듯이 입력을 끝내는건 EOF를 입력하면 된다고 한다.

7. rax 레지스터를 0으로 바꾸고 EOF를 입력해보자

![result1](https://user-images.githubusercontent.com/53170968/93592772-bbb52e00-f9ed-11ea-8b98-9236200cc876.png)

![result2](https://user-images.githubusercontent.com/53170968/93592779-bce65b00-f9ed-11ea-81a5-433757657fe5.png)

8. Do you want single-step mode? 를 물어본게 한 단계씩 실행한다는 뜻인가 보다.

9. 다음 문제를 풀때는 N로 설정해봐야겠다.

10. 결과가 정확하게 나왔다.

11. 이번 문제는 어셈블리어의 기초를 알려주는 문제인 것 같다.

12. 답을 입력해보자!!

![solve](https://user-images.githubusercontent.com/53170968/93598215-582ffe00-f9f7-11ea-96d0-3f5090829436.png)

13. 정답이다!! 이제 어셈블리어와 레지스터도 이용한다. 뒤에 몇문제도 계속 어셈블리 코드를 이용한다.