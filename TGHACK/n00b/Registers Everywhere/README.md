# Registers Everywhere

### Problem
    Set up the registers as follows:
![problem](https://user-images.githubusercontent.com/53170968/93600073-0fc60f80-f9fa-11ea-8164-a993645a18bf.png)

    Good luck!

    nc shellcode.tghack.no 1111
    
    Note: This is level 2. End your assembly code with a line containing EOF.

### Solution
1. 이 문제는 앞에서 풀었던 Baby's First Assembly Code 문제의 다음 단계이다.

2. 위에 있는 레지스터들의 값들을 각각 set해서 푸는 문제인 것다.

3. 바로 풀어보자

![connect](https://user-images.githubusercontent.com/53170968/93600584-d8a42e00-f9fa-11ea-9aea-bcd0aa8cf904.png)

4. 중간에 step으로 멈추고 엔터를 치는게 싫어서 N으로 설정해봤다.

5. Level은 2라고 했으므로 2로 입력

6. 위에서 설정하라는대로 레지스터들을 설정하고 EOF를 입력해보자

![sol](https://user-images.githubusercontent.com/53170968/93600587-da6df180-f9fa-11ea-9553-02ac5c619738.png)

7. 결과를 봐보자

![solve](https://user-images.githubusercontent.com/53170968/93600592-da6df180-f9fa-11ea-8fdc-d165e823f686.png)

8. 결과가 잘 나왔다. N을 입력했더니 중간에 멈춤도 없이 결과까지 나왔다. 답이 맞는지 입력해봐야겠다.

![result](https://user-images.githubusercontent.com/53170968/93600845-3df81f00-f9fb-11ea-8e2a-9687ea372895.png)

9. 정답이다!! 추가적으러 적자면 mov 명령어는 해당하는 ','앞 레지스터의 값을 ','뒤의 값으로 변경해주는 명령어이다.