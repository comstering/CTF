# Introduction to Functions

### Problem
    Create a function that takes no parameters and returns 0. You only have to write the function body.

    nc shellcode.tghack.no 1111
    
    Note: This is level 4. End your assembly code with a line containing EOF.

### Solution
1. 문제에서 파라미터를 받지 않고 0을 리턴하는 함수를 만들라고 나와있다.

2. 오직 함수의 바디만 만들면 된다고 한다.. 한번 함수를 만들어보자

3. 일단 문제에 들어가자

![image](https://user-images.githubusercontent.com/53170968/94361654-f35c5e00-00f0-11eb-82ef-be4523f19cc2.png)

4. 문제를 다시 읽어 봤는데 조금 어색하다. 어셈블리에서 함수를 작성하고 호출하려면 작성된 함수의 주소값과 call 명령어를 써야한다.

5. 그런데 그런 것 없이 그냥 함수의 바디만 만들면 된다라고 한다면 지금 들어와 있는 상태가 함수의 바디 내부인것 같다.

6. rax에 0을 넣고 그 0을 바로 리턴하는 형식으로 바로 작성해보겠다.

![image](https://user-images.githubusercontent.com/53170968/94361725-7b426800-00f1-11eb-946b-74ff26dccd1f.png)

7. rax에 0을 넣고 ret 명령어로 rax의 값을 반환하며 함수를 끝낸다.

8. ret는 정확하게 같진 않지만 c언어나 파이썬, 자바와 같은 언어에서 return의 역할이라고 생각하면 된다.

![image](https://user-images.githubusercontent.com/53170968/94361780-dd02d200-00f1-11eb-8d43-6b55ebe03e55.png)

9. 터미널 창이 작아서 조금 키웠다.

10. 지금 작성하던 화면은 함수의 내부를 쓰는 곳이었다. 간단하게 결과를 리뷰해보자.

11. call 명령어로 func라는 함수를 호출한다. func의 내용은 아까 내가 작성한 코드이다.

12. func에서는 rax레지스터 값을 0으로 만들고 ret 명령어로 rax의 값인 0을 반환한다.

13. 결과가 정확하게 나와서 FLAG가 나왔다. 답을 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/94362729-61585380-00f8-11eb-8206-daa99926cc51.png)

14. 이상없이 정답처리가 되었다.

15. 이번 문제는 어셈블리에서 함수의 호출과 끝내는 과정을 알 수 있는 좋은 계기가 되었다!!