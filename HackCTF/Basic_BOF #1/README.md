# Basic_BOF #1

### Problem
![image](https://user-images.githubusercontent.com/53170968/112443791-b536b300-8d90-11eb-89f6-57e42583bb88.png)


### Solution
1. HackCTF는 소스코드 없이 바이너리 파일만 주어진다.

![image](https://user-images.githubusercontent.com/53170968/112443919-d3041800-8d90-11eb-82d9-7e7922fcd66a.png)

2. 먼저 파일을 실행할 수 있도록 권한변경을 해준다.

3. 해당파일을 실행해서 어떤 결과가 나오는지 먼저 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112444073-fcbd3f00-8d90-11eb-9d6a-4e7abe4bbd35.png)

4. 문자열을 입력받고 입력받은 문자열이 저장되는 buf변수의 값을 출력해주고 check라는 값도 출력해준다.

![image](https://user-images.githubusercontent.com/53170968/112444260-3130fb00-8d91-11eb-9802-836f86a0131c.png)

5. gdb로 실해시켜서 메모리를 파악해보자.

![image](https://user-images.githubusercontent.com/53170968/112444352-49a11580-8d91-11eb-9423-de4c1f556982.png)

![image](https://user-images.githubusercontent.com/53170968/112444355-4ad24280-8d91-11eb-82d2-c7f19166c79a.png)

![image](https://user-images.githubusercontent.com/53170968/112444364-4d349c80-8d91-11eb-88ca-47583c862831.png)

6. 이렇게 main함수의 구조를 확인해 봤다.

![image](https://user-images.githubusercontent.com/53170968/112444474-69383e00-8d91-11eb-981b-2b9edf02be38.png)

7. 그 중에서도 cmp라는 어셈블리코드가 존재하는데 c언어로 말하자면 if문의 조건식과 비슷하다. 앞 뒤의 데이터를 비교하는 연산이다. 즉, [ebp-0xc]의 메모리에 존재하는 데이터와 0x4030201과 같은지 비교한다는 뜻이다.

![image](https://user-images.githubusercontent.com/53170968/112444659-a13f8100-8d91-11eb-8403-4572e92925d1.png)

8. 밑으로 좀 더 내려와서 확인해보니 눈에 띄는 함수가 존재한다. 바로 system함수이다. system함수는 리눅스의 쉘에 명령어를 전달해주는 함수이다. 즉, 우리는 어떠한 조작을 통해서 저 system함수가 실행될 수 있도록 해야할 것 같다.

9. 다른 부분을 좀 더 분석해보자.

![image](https://user-images.githubusercontent.com/53170968/112465333-f4243300-8da7-11eb-8480-64c6a4e9e928.png)

10. je와 jne는 cmp뒤쪽에 나오는 어셈블리어다.

11. je는 cmp의 비교결과가 같다면 je 뒤쪽에 표시된 메모리로 jump한다. 만약 비교결과가 다르다면 je다음 코드로 넘어간다.

12. jne는 je와 반대의 개념이다. cmp의 비교결과가 다르다면 jne의 뒤쪽에 표시된 메모리로 jump하고 비교결과가 다르다면 jnu 다음 코드로 넘어간다.

13. 밑줄 친 jne를 보면 두 연산의 비교결과가 다르다면 main+177메모리로 넘어간다. 하지만 우리가 호출시켜야하는 system함수는 main+153에 있다. 즉, jne의 코드에 걸리면 안되므로 [ebp-0xc]의 데이터 값은 0xdeadbeef이어야 한다.

![image](https://user-images.githubusercontent.com/53170968/112465622-46655400-8da8-11eb-848e-596d08daf93c.png)

14. 프로그램을 실행했을 때 사용자입력을 받았었다. 그래서 입력함수를 찾아봤더니 해당 프로그램에는 fgets함수만이 존재한다.

15.  즉 우리는 저 fgets로 입력하는 문자열을 이용해서 BOF를 발생시켜야한다.

![image](https://user-images.githubusercontent.com/53170968/112466168-e28f5b00-8da8-11eb-9f84-3cec9b2c3662.png)

16. 비교연산이 진행되는 [ebp-0xc]의 데이터를 찾아봤더니 프로그램 초반에 0x4030201초 초기화를 시키고 있다. 즉, 현재의 [ebp-0xc]의 값은 0x4030201이다.

17. 메모리에 저장된 데이터를 알아보기 위해 breakpoint를 걸어서 데이터를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112466834-a1e41180-8da9-11eb-9a56-a8534dbd53d3.png)

18. [ebp-0xc]의 데이터가 변화하는 main+17과 사용자 입력을 받는 main+39위치에 breakpoint를 걸었다.

![image](https://user-images.githubusercontent.com/53170968/112466948-ca6c0b80-8da9-11eb-919b-01d5a9f2118a.png)

19. 아직 mov어셈블리가 실행되지 않은 상태에서의 [ebp-0xc]위치가 있는 데이터 내역들이다.

20. ni를 통해서 mov어셈블리어가 실행되고 [ebp-0xc]위치의 데이터를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112467173-115a0100-8daa-11eb-8bce-b88cea42be32.png)

21. 첫 부분의 데이터가 0x04030201로 바뀐 것을 볼 수 있다. [ebp-0xc]의 위치가 어디이고 어떻게 데이터가 변화하는지 확인할 수 있었다.

22. 다음으로 fgets위치의 어셈블리 구조를 알아보자.

![image](https://user-images.githubusercontent.com/53170968/112467390-5847f680-8daa-11eb-9891-b3b82f159a06.png)

23. c를 이용해서 다음 breackpoint까지 이동시키자.

![image](https://user-images.githubusercontent.com/53170968/112467453-6ac23000-8daa-11eb-896a-6858f2c3f70c.png)

24. fgets함수의 호출을 볼 때 앞쪽의 데이터도 확인해야한다.

25. push는 Stack영역에 데이터를 삽입하는 명령어다. 왜 코드 중간에 Stack영역에 데이터를 넣을까?

26. 바로 fgets의 매개변수이다. 매개변수도 하나의 지역변수이기 때문에 Stack영역에 저장된다. 단, 매개변수는 앞쪽의 매개변수부터가 아니라 뒤쪽의 매개변수부터 Stack영역에 저장된다.

27. 그렇다면 위의 fgets는 c언어로 바꾸자면 fgets(eax, 0x2d, eax);가 된다.

28. eax는 레지스터이다. 메모리 데이터가 임시로 저장되는 영역이라는 뜻이다. 위쪽에 eax에 데이터를 저장하거나 복사하는 명령어까지 고려해서 fgets함수를 표현하면 fgets([ebp-0x34], 45, ds:0x804a040);이 된다.

29. 45는 0x2d를 정수형인 10진수로 표현한 것이다. (16x2 + 13(d) = 45)

30. 우리가 프로그램을 실행했을 때 문자열 입력을 사용자 키보드로 입력했다. 이건 표준입력이다. 즉, ds:0x804a040이란 값은 stdin이란 뜻이 된다.

31. fgets함수를 최종적으로 표현하면 fgets([ebp-0x34], 45, stdin);이 된다.

32. fgets는 c언어에서 사용해봤듯이 매개변수로 전달받은 문자열, 메모리 포인터에 입력한 문자열을 저장한다. 즉, 우리가 입력한 문자열은 [ebp-0x34]에 저장된다는 것이다. 그렇다면 해당 메모리를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112468670-e670ac80-8dab-11eb-9809-51a6d2f7e0d2.png)

33. [ebp-0x34]위치의 메모리를 확인했는데 익숙한 데이터가 보인다. 바로 [ebp-0xc]위치에 저장되었던 0x04030201이다.

34. 우리는 저 [ebp-0xc]위치의 데이터를 0xdeadbeef로 바꾸어야한다. 즉 fgets로 입력하는 데이터를 이용해서 BOF를 일으켜 [ebp-0xc]의 데이터를 0xdeadbeef로 바꿔주면 된다.

35. [ebp-0x34]에서 부터 [ebp-0xc]의 위치까지의 메모리크기는 40Byte이다. 즉, 40Byte만큼 아무 데이터나 입력하고 그 뒤에 0xdeadbeef데이터를 넣어주면 된다.

36. 데이터를 입력해서 다시 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/112469174-80d0f000-8dac-11eb-9ff9-b3869d17db41.png)

37. A를 40개 입력하고 그 뒤에 0xdeadbeef값을 추가해서 입력값으로 넣었다. deadbeef를 입력할 때 주의할 점은 반드시 1Byte단위로 역순으로 입력해야한다는 것이다.

38. 역순으로 해야하는 이유는 리틀엔디안과 관련되어 있다.

39. breakpoint를 이용해서 프로그램이 돌아갈 때마다 메모리를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112469533-f046df80-8dac-11eb-8a14-5826b6dcdbd9.png)

40. 첫 breakpoint에는 아직 데이터가 저장되지 않았기 때문에 메모리 공간에 변화가 없다.

![image](https://user-images.githubusercontent.com/53170968/112469615-06ed3680-8dad-11eb-9f5e-7b0923f3d051.png)

41. fgets가 실행되기 직전인 두번째 breapoint에서 메모리를 확인해보면 [ebp-0xc]의 데이터가 0x04030201의 데이터가 저장된 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112469755-2e440380-8dad-11eb-832a-191608ca0799.png)

42. ni명령을 통해서 fgets만 실행한 상태로 다시 메모리를 확인하면 [ebp-0x34]부터 [ebp-0xc]의 앞쪽까지 A의 값인 0x41로 채워진 것을 볼 수 있고 최종적으로 [ebp-0xc]의 데이터가 0xdeadbeef로 바뀐 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112470014-7d8a3400-8dad-11eb-93a7-4d41ee573348.png)

43. gdb를 나와서 일반적인 실행으로 결과를 확인해본 결과 쉘을 획득했다고 나온 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112470120-a14d7a00-8dad-11eb-89b5-ce51440efec0.png)

44. 해당 host에 pwntools를 이용해서 접속하여 문제를 해결하도록 하겠다.

![image](https://user-images.githubusercontent.com/53170968/112470251-cb9f3780-8dad-11eb-91e6-d612c17076f9.png)

45. solution.py를 실행시켜보면 해당 host의 쉘을 얻은 것을 볼 수 있다.

46. 그리고 flag파일의 내용에 우리가 원하는 FLAG가 있는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112470401-f5f0f500-8dad-11eb-895b-b5a8cf9c1186.png)

![image](https://user-images.githubusercontent.com/53170968/112470416-f9847c00-8dad-11eb-934a-ff55dd9be8c8.png)

47. FLAG를 제출해서 정답으로 처리되었다.