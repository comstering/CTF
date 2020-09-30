# Baby's First Shellcode

### Problem
    Time to write your first shellcode! Write shellcode that issues the syscall exit with a status code of 42. The C equivalent would be something like: exit(42).

    Good luck!

    nc shellcode.tghack.no 1111
    Note: This is level 7. End your assembly code with a line containing EOF.

### Solution
1. 문제 제목이 First Shellcode이다. 셀코드를 작성해야할 것 같은 느낌이 들지만 일단 문제부터 읽어보자

2. status code 42로 syscall의 exit를 발행하여야 하는 문제이다.

3. 즉, exit에 해당하는 syscall을 42의 값을 줘서 호출하는 것이다.

4. 일단 syscall에서 exit에 해당하는 값이 무엇인지 알아보자.

5. 그냥 인터넷에서 'syscall table'이라고 검색해서 나온 결과이다.

![image](https://user-images.githubusercontent.com/53170968/94662352-3d3c8280-0343-11eb-850c-db11101637f0.png)

![image](https://user-images.githubusercontent.com/53170968/94662404-4c233500-0343-11eb-9298-0cb0a513c565.png)

6. exit에 해당하는 syscall은 60번인 것을 알 수 있다. 그리고 rax 레지스터를 사용하면 된다고 친절하게 표에 표시되어있다.(사용하면 된다라기보다는 rax레지스터를 사용한다라고 표시되어있다라고 말하는게 맞는 느낌인것 같다;;;)

7. 그리고 문제에서 c언어를 예로 들어줬는데 exit(42)와 같은 형태라고 했으니 42는 함수의 매개변수로 넣는다고 생각해볼 수 있을 것 같다.

8. 현재 공부가 부족한 나로써는 문제에서 말하는 대로 shell code를 직접 짜서 하는 문제인지 아니면 지금 내가 풀고 있는 방식이 맞는 건지 모르겠다.

9. 하지만 현재로썬 레지스터를 이용해서 푼다라고 밖에 생각이 들지 않는다.

10. 다시 문제로 돌아가서 rax레지스터에 60을 넣고 함수의 매개변수로 전달되는 값이 담기는 rdi레지스터에 42를 넣어서 syscall을 실행하면 될 것 같다.

11. 일단 먼저 문제에 들어가보자

![image](https://user-images.githubusercontent.com/53170968/94663178-52fe7780-0344-11eb-9c79-206bc0299190.png)

12. 내가 생각한 답을 적어보자

![image](https://user-images.githubusercontent.com/53170968/94663712-f51e5f80-0344-11eb-8c76-cae873315aaf.png)

13. rax에 60을 넣고 rdi에 42를 넣고 syscall을 호출한다.

![image](https://user-images.githubusercontent.com/53170968/94663793-0cf5e380-0345-11eb-98d2-3dfd7822259c.png)

14. 결과가 성공적으로 나왔다.

15. 그럼 FLAG를 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/94664033-5fcf9b00-0345-11eb-92d8-643259065230.png)

16. 정답이다.