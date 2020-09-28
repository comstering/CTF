# More Parameters

### Problem
    Create a function that takes two parameters, multiplies them together and returns the result.
    The equivalent in C would be something like this:

        int func(int a, int b)
        {
            return a * b;
        }
    
    Connect to the challenge server to solve the task: nc shellcode.tghack.no 1111
    Note: This is level 6. End your assembly code with a line containing EOF.

### Solution
1. 이번 문제는 앞서 파라미터 1개를 입력받은 함수에 이어서 2개를 입력받는 함수를 만드는 문제이다.

2. 앞과 똑같이 함수의 바디(몸체)만 만들면 되는 것 같다.

3. 바로 문제에 들어가보자

![image](https://user-images.githubusercontent.com/53170968/94447574-db660680-01e4-11eb-8f54-4247c8ee3237.png)

4. 이전 문제에서 말했듯이 함수의 파라미터로 넘어온 값은 rdi레지스터나 rsi레지스터에 들어간다.

5. rdi의 값을 저장하고 rsi와 곱해서 리턴하는 형식으로 코드를 짜보겠다.

![image](https://user-images.githubusercontent.com/53170968/94447844-37308f80-01e5-11eb-97e9-189667d8bfb7.png)

6. rax 레지스터에 rdi 레지스터 값을 넣는다.

7. mul을 통해 rax 레지스터와 rsi 레지스터의 값을 곱하고 ret로 그 값을 반환한다.

![image](https://user-images.githubusercontent.com/53170968/94447943-58917b80-01e5-11eb-853f-fcea3a12c4e4.png)

8. 정답으로 나왔다. 그러면 역시나 FLAG를 입력해보자

![image](https://user-images.githubusercontent.com/53170968/94448522-f2f1bf00-01e5-11eb-9d57-b4d0dcd65bd2.png)

9. 정답이다!!! 이 문제는 앞전에 풀었던 문제를 풀기위해 공부했다면 바로 풀 수 있는 문제였다.