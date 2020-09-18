# Division

### Problem
    The rax register will be set up to contain a random value. Use the div instruction to divide rax by 4.

    nc shellcode.tghack.no 1111
    
    Note: This is level 3. End your assembly code with a line containing EOF.

### Solution
1. 이번 문제는 레지스터 사칙연산을 이용하는 방법이다.

2. rax에 값이 들어있고 그 값을 4로 나누기만 하면 답이 나오는 것 같다.

3. 먼저 레지스터 나누기 연산 방법을 알아보자

    mov ax, 100
    
    mov bl, 2
    
    div bl

4. 현재 레지스터에 바로 뒤의 레지스터에 나눌 값을 넣고 div를 사용하면 몫이 현재 레지스터에 들어간다.

5. 만약 현재 레지스터 앞에 레지스터가 있다면 몫 나머지 순서대로 레지스터에 값이 들어간다.
    
    mov eax, 0  ; 0으로 초기화
    
    mov edx, 0  ; 0으로 초기화

    mov ax, 100
    
    mov bl, 2
    
    div bl
    
    eax: 몫, adx: 나머지

6. 그렇다면 rax 다음의 레지스터가 무엇인지 먼저 알아보자

![register](https://user-images.githubusercontent.com/53170968/93611514-5d964400-fa09-11ea-94a3-ab491d71908c.png)

7. 위 표를 보면 rax 다음 레지스터는 rbx이다.

8. 그러면 한번 풀어보자

![solve](https://user-images.githubusercontent.com/53170968/93611913-d7c6c880-fa09-11ea-9c87-5c77248a0ad9.png)

9. rax 다음 레지스터인 rbx에 나눌 수인 4을 넣는다.

10. 그리고 div를 사용해 rax를 rbx로 나눈다.

![sol](https://user-images.githubusercontent.com/53170968/93611915-d85f5f00-fa09-11ea-8df0-d26f78ecac02.png)

11. 그러면 rax를 4로 나눈 결과가 된다.

12. FLAG가 나왔으니 입력해보자

![result](https://user-images.githubusercontent.com/53170968/93612319-56236a80-fa0a-11ea-8d91-f671c52a0e78.png)

13. 정답이다!! 이 문제는 어셈블리 연산방법을 알고 레지스터의 메모리 순서를 알아야하는 문제였다.