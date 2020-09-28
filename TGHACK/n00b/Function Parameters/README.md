# Function Parameters

### Problem
    Create a function that takes one parameter, a, and returns (a * 4) + 3. The C declaration would look like this:

        int func(int a)
        {
            return (a * 4) + 3;
        }

    nc shellcode.tghack.no 1111
    Note: This is level 5. End your assembly code with a line containing EOF.

### Solution
1. 이번 문제는 파라미터를 받아서 계산 결과를 반환하는 함수를 만들라고 한다.

2. 이번 문제도 call명령어나 이런거 필요 없이 그냥 몸체에 들어갈 내용만 적으면 될 것 같다.

3. 문제에 들어가보자

![image](https://user-images.githubusercontent.com/53170968/94422773-8e713880-01c2-11eb-8827-064d886c2bd2.png)


4. 문제를 풀기전에 어셈블리에서는 함수의 파라미터가 어느 레지스터에 들어가는지 알아야 한다.

5. 어셈블리에서는 대개 rdi나 rsi 레지스터에 함수에서 전달받은 파라미터 값이 들어간다.

6. 지금까지 했던 것 처럼 rax 레지스터에 전달받은 파라미터와 4를 곱한 값을 넣고 그리고 3을 더해서 결과값을 리턴해보겠다.

![image](https://user-images.githubusercontent.com/53170968/94423149-22430480-01c3-11eb-8cf0-c56d8b2a4faa.png)

7. rax 레지스터에 4를 넣고 mul을 통해서 rax와 rdi를 곱한 값을 rax에 저장한다.

8. 그리고 add를 통해 rax의 값에 3을 더한다.

9. 마지막으로 ret를 통해서 rax값을 리턴한다.

![image](https://user-images.githubusercontent.com/53170968/94423305-646c4600-01c3-11eb-908c-6a1db5badb0e.png)

10. 결과가 잘 나왔다.

11. 그럼 저 FLAG를 입력해보자

![image](https://user-images.githubusercontent.com/53170968/94423466-a4cbc400-01c3-11eb-84dd-4fb97a744018.png)

12. 정답처리 되었다.

13. TGHACK가 제대로 풀기 시작한 첫 CTF인데 여러가지로 많은 것을 알게 되었다.

14. 어셈블리어를 코딩해보는 것도 처음인데 뭔가 신기롭기도 하다.

15. 계속 문제를 풀면서 실력을 향상시키고 싶다!!!