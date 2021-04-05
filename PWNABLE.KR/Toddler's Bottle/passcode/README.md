# Toddler's Bottle - passcode

### Problem
![image](https://user-images.githubusercontent.com/53170968/113526381-cedbc400-95f4-11eb-88b7-7632098d2341.png)

### Solution
1. ssh를 통해서 해당 문제에 접속하자.

![image](https://user-images.githubusercontent.com/53170968/113526394-ddc27680-95f4-11eb-8703-276866a6f505.png)

2. 어떤 파일이 있나 먼저 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113526419-f599fa80-95f4-11eb-950b-ec6def9fd6f8.png)

3. 당연히 flag파일은 FLAG가 저장되어 있는 파일일 것이고 passcode파일을 실행해서 아마 저 flag파일을 읽어야 할 것이다.

4. passcode파일의 소스코드인 passcode.c파일을 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113526465-211ce500-95f5-11eb-9bf8-f49b350932e4.png)

    #include <stdio.h>
    #include <stdlib.h>
    
    void login(){
            int passcode1;
            int passcode2;
    
            printf("enter passcode1 : ");
            scanf("%d", passcode1);
            fflush(stdin);
    
            // ha! mommy told me that 32bit is vulnerable to bruteforcing :)
            printf("enter passcode2 : ");
            scanf("%d", passcode2);
    
            printf("checking...\n");
            if(passcode1==338150 && passcode2==13371337){
                    printf("Login OK!\n");
                    system("/bin/cat flag");
            }
            else{
                    printf("Login Failed!\n");
                    exit(0);
            }
    }
    
    void welcome(){
            char name[100];
            printf("enter you name : ");
            scanf("%100s", name);
            printf("Welcome %s!\n", name);
    }
    
    int main(){
            printf("Toddler's Secure Login System 1.0 beta.\n");
    
            welcome();
            login();
    
            // something after login...
            printf("Now I can safely trust you that you have credential :)\n");
            return 0;
    }

5. 소스코드를 분서해보자.

6. main함수는 간단하다. welcome함수와 login함수를 호출하기만 한다.

7. welcome함수는 name을 입력받고 그 name을 그대로 출력해주는 역할을 한다.

8. 중요한 부분은 login함수이다.

9. login함수에서 passcod1과 passcode2에 데이터를 입력받고 각각 338150, 13371337이면 if문이 만족하여 FLAG를 출력해준다.

10. 일단 지금 내용대로 실행해서 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/113526586-938dc500-95f5-11eb-8a3c-ce661651a7b2.png)

11. 입력했더니 passcode1 입력에서 에러가 발생했다.

12. 소스코드를 다시 확인해보니 이상한 부분이 있었다. 바로 scanf에 passcode1의 주소값이 아닌 passcode1자체가 들어 있었다. 즉, &기호가 변수 앞에 붙어있지 않았다.

13. 이렇게 되면 입력되는 변수는 passcode1의 메모리 공간에 저장되는 것이 아니라 passcode1에 저장되어 있는 데이터값과 동일안 주소값에 데이터를 저장한다.

14. 하지만 passcode1은 선언할 때 초기화를 하지 않았기 때문에 쓰레기 값(dummy data)가 저장되어 있다.

15. 그래서 dummy data에 해당하는 주소가 사용할 수 없기에 저 segmentation fault가 발생하게 된다.

16. 그렇다면 gdb를 통해서 코드와 메모리를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113528110-9212cb80-95fa-11eb-9e38-1883fcf79c69.png)

17. main함수는 딱히 별다른게 없으므로 welcome함수 먼저 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113528092-87f0cd00-95fa-11eb-856c-5f65c14aa75e.png)

18. name변수에 scanf로 문자열을 입력받는데 name변수의 시작 주소는 [ebp-0x70]인 것을 알 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113528176-cdad9580-95fa-11eb-847d-b135c1572339.png)

19. 그리고 login함수를 확인해보면 passcode1에 데이터를 저장하는 scanf를 확인할 수 있다.

20. passcode1의 메모리주소은 [ebp-0x10]인 것을 알 수 있다.

21. 여기서 메모리 분석을 살짝 해보자.

22. welcome함수에서 입력하는 name의 시작주소는 [ebp-0x70], login함수에서 입력하는 passcode1의 주소는 [ebp-0x10]이다.

23. 이 둘의 메모리 공간 차이를 확인해보면 0x70 - 0x10 = 0x60 = 96이다.

24. 그런데 name의 크기는 100이고 또한 welcome의 scanf에서 입력받을 수 있는 데이터의 양도 100이다.

25. 즉, name의 뒤 4Byte를 passcode1과 함께 공유해서 사용하고 있다라고 생각할 수 있다.

26. 즉, welcome함수에서 96Byte의 데이터까지는 name변수에만 저장되지만 그 이후의 데이터는 passcode1에서도 사용되어 passcode1의 데이터를 조작할 수 있게 된다는 뜻이 된다.

27. 실제로 그런지 breakpoint를 걸어서 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113528423-7bb93f80-95fb-11eb-8bf4-5f25406fdc97.png)

![image](https://user-images.githubusercontent.com/53170968/113528426-7eb43000-95fb-11eb-8232-3aa6e04e50b7.png)

![image](https://user-images.githubusercontent.com/53170968/113528431-81168a00-95fb-11eb-83d9-7f4190fc0e6a.png)

28. breakpoint를 걸고 실행을 시켰다.

29. 이제 메모리를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113528464-9b506800-95fb-11eb-878e-de3488a15207.png)

30. 빨간 테두리 부분이 [ebp-0x70] ~ [ebp-0x11]까지의 위치가 된다. 0xfffeb38이 시작되는 저 부분이 passcode1의 메모리 공간이 된다.

31. 이제 해결방법을 한 번 고민해보자.

32. 먼저 소스코드대로 따라간다면 passcode1의 값을 338150으로 바꾸로 passcode2의 값도 13371337로 바꾸면 if문이 참이 되어 FLAG를 출력해줄 것이다.

33. 하지만 우리가 바꿀 수 있는 것은 passcode1뿐이다. passcode2의 메모리 위치인 [ebp-0xc]의 메모리 위치는 어디인지, 어떻게 조작할 수 있을지도 모른다.

34. 하지만 그렇다고 passcode2의 scanf로 이동하면 역시나 dummy data로 인해 segmentation fault가 발생할 것이다.

35. 그렇다면 우리는 passcode1의 scanf 이후와 passcode2의 scanf전에 어떠한 조작을 통해서 문제를 해결해야한다.

36. 그래서 이 둘 사이에 있는게 어떤 것이 있는지 확인해 봤더니 fflush라는 함수가 존재한다.

37. fflush함수는 원래 scanf입력으로 인해 발생하는 \n이 다른 입력에 영향을 주지 않도로 버퍼를 제거하는 역할이다.

38. 하지만 우리는 여기서 저 함수를 통해서 FLAG를 획득해야한다.

39. fflush함수를 한 번 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113528733-6abcfe00-95fc-11eb-8a8b-63cba901cf10.png)

40. 함수가 시작하자마자 0x804a004의 메모리 위치로 jump한다. 그렇다면 우리는 저 0x804a004의 메모리 주소에 어떠한 메모리 주소값을 넣어 fflush함수가 호출되면 내가 원하는 동작을 할 수 있도록 변경할 수 있다.

41. 이때 사용할 방법이 바로 위의 passcode1의 scanf이다.

42. scanf에는 원래 passcode1의 메모리 주소값이 들어가야한다. 하지만 &기호를 사용하지 않아 실제로는 passcode1의 데이터값 자체가 들어가게 된다.

43. 만약 passcode1의 데이터에 어떠한 주소값과 동일한 데이터가 저장되어 있다면 scanf로 입력되는 값은 passcode1의 데이터와 동일한 주소값에 입력되게 된다.

44. 즉, passcode1에 0x804a004값이 저장되어 있다면 우리가 어떠한 데이터를 입력하면 그 데이터는 0x804a004에 저장되고 그렇게 되면 fflush함수가 호출될 때 원래의 동작이 아닌 다른 동작을 하게 된다.

![image](https://user-images.githubusercontent.com/53170968/113529012-4150a200-95fd-11eb-82e2-4d5f256a7a0f.png)

45. 동작방식은 이렇게 된다. 우리가 최종적으로 호출 시켜야하는 것은 system(cat flag)이다.

![image](https://user-images.githubusercontent.com/53170968/113529075-6d6c2300-95fd-11eb-946c-9f876299b077.png)

46. 해당 함수는 login함수의 if문 안에 존재한다.

47. fflush함수가 호출되면 바로 if문을 건너뛰고 저 위치로 이동하게 한다면 당연히 함수호출로 인해 FLAG가 출력될 것이다.

48. 여기서 중요한 것은 system함수의 호출은 0x08485ea이지만 system함수호출만이 아닌 'cat flag'라는 매개변수도 같이 포함되어야하므로 0x80485e3부터 동작해야한다.

49. 우리는 fflush함수가 호출되었을 때 자동으로 저 0x80485e3으로 jump하게하면 된다.

50. 제일 먼저 name을 입력할 때 96자리까지 입려하고 나머지 4자리는 fflush에서 확인했던 주소값인 0x804a004를 입력해주면 된다.

51. 그러면 자동으로 passcode1의 scanf에서 데이터를 입력할 수 있게 되고 이때 입력되는 데이터는 0x804a004주소의 데이터를 변경한다.

52. 입력해야할 데이터는 0x080485e3인데 우리가 입력할 수 있는 값은 16진수 정수가 아닌 10진수 정수이므로 0x080485e3을 10진수로 변환한 값인 134514147을 입력해야한다.

![image](https://user-images.githubusercontent.com/53170968/113529408-4c580200-95fe-11eb-9c31-25a96ab49d0c.png)

53. 위의 내용을 그대로 입력했다. 'A'를 96개 입력하고 리틀엔디안으로 고려해서 0x804a004를 입력했다. 그리고 입력하는 scanf에서 134514147을 입력했더니 system(cat flag); 함수가 호출되어 FLAG를 출력했다.

![image](https://user-images.githubusercontent.com/53170968/113529476-80cbbe00-95fe-11eb-919b-b084cc894f26.png)

![image](https://user-images.githubusercontent.com/53170968/113529479-82958180-95fe-11eb-9e97-502f2bb097ea.png)

54. 사이트에 입력한 결과 정답처리 되었다.