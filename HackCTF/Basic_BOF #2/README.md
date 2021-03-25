# Basic_BOF #2

### Problem
![image](https://user-images.githubusercontent.com/53170968/112505012-b5a26e80-8dcf-11eb-9ade-c3e440ca17a8.png)

### Solution
1. 역시나 바이너리 파일만 주어진다. 그럼 바로 문제를 풀어보자.

![image](https://user-images.githubusercontent.com/53170968/112505192-e4204980-8dcf-11eb-83f2-749322b317dc.png)

2. 실행할 수 있도록 파일 권한을 변경한다.

![image](https://user-images.githubusercontent.com/53170968/112505252-f5695600-8dcf-11eb-8a7e-afd84b7e1f71.png)

3. 그리고 먼저 실행했을 때의 결과를 확인해보니 내가 입력한 값과 무관하게 '하아아아아아아아아앙'이라는 문자열이 출력된다.

![image](https://user-images.githubusercontent.com/53170968/112505413-18940580-8dd0-11eb-9454-ec6b59686f41.png)

4. gdb로 해당파일을 실행한다. 그리고 어셈블리어 출력방식을 intel 방식으로 출력한다.

![image](https://user-images.githubusercontent.com/53170968/112505814-7a546f80-8dd0-11eb-8de2-8ecc864d78b7.png)

5. 먼저 main함수를 파악해보자.

![image](https://user-images.githubusercontent.com/53170968/112505888-8fc99980-8dd0-11eb-8e4f-ae5f14bd3a3e.png)

6. fgets함수를 먼저 확인해보자. 해당 코드의 분석 방법은 Basic_BOF #1에서 말했으므로 바로 fgets함수를 c언어로 바꿔보자.

7. fgets([ebp-0x8c], 133, stdin);

![image](https://user-images.githubusercontent.com/53170968/112506177-d7502580-8dd0-11eb-95d9-9860fafaa4a2.png)

8. 그리고 앞쪽부분에 [ebp-0xc]의 메모리 공간에 0x80484b4이 저장된다.

9. 그런데 저장되는 값이 뭔가 메모리주소처럼 보인다. 한번 해당 주소의 함수가 존재하는지 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112506567-3dd54380-8dd1-11eb-8381-d3335e6f6f8a.png)

10. 해당 데이터값으로 disas명령어를 사용했더니 함수의 어셈블리어가 출력되었다. 함수의 내용은 어떤 내용을 출력하는 puts함수가 호출된다.

11. main함수의 다른 부분도 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112506937-90166480-8dd1-11eb-9664-058a296fe656.png)

12. [eax] 레지스터에 [ebp-0xc]의 데이터가 저장된다. 즉, 위에서 본 함수의 주소값이 저장되는 것이다.

13. 그리고 바로 아래를 보면 함수를 호출하는 명령어인 call명령어가 있고 호출하는 함수의 주소는 eax의 데이터가 선언되어 있다.

14. 즉, 위에서 [ebp-0xc]에 저장된 0x80484b4는 함수의 메모리주소값이고 fgets함수 호출 이후에 해당 주속밧의 함수가 호출된다.

15. 함수의 내용에는 어떤 내용을 출력하는 puts함수만 존재했다. 즉, '하아아아아아아아아앙'이라는 문자열은 저 함수에서 출력되는 것이다.

16. [ebp-0xc]에 다른 값이 변한다면 call eax로 호출되는 함수는 다른 함수가 된다. 그렇다면 해당 프로그램에 어떤 함수가 있는지 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112507993-804b5000-8dd2-11eb-959d-5d347bd6aed5.png)

![image](https://user-images.githubusercontent.com/53170968/112507999-82151380-8dd2-11eb-9200-ff5a54de2568.png)

17. 눈에 띄는 함수가 존재한다.

![image](https://user-images.githubusercontent.com/53170968/112508123-9b1dc480-8dd2-11eb-90e4-c38ea36d940d.png)

18. shell이라는 함수와 system함수이다.

19. 아마 예상하기로는 shell함수안에서 system함수를 호출해서 쉘권한을 획득하는 그러한 로직일 것 같다.

20. shell함수의 코드를 한 번 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112508312-c6081880-8dd2-11eb-8065-e9e21bbe252c.png)

21. 역시나 예상대로 shell이라는 함수에서 system함수가 호출된다.

22. 이제 해야할 일이 정해졌다. BOF를 발생시켜서 [ebp-0xc]에 저장되어 있는 0x80484b4의 값을 shell함수의 주소값인 0x0804849b로 바꿔주면 된다.

23. breakpoint를 걸어서 값을 메모리 공간을 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/112508641-17180c80-8dd3-11eb-99a8-8b8158c7de33.png)

![image](https://user-images.githubusercontent.com/53170968/112508660-197a6680-8dd3-11eb-848c-bf5524109fdd.png)

24. [ebp-0xc]에 값을 저장하는 부분과 fgets함수가 호출되는 부분에 breakpoint를 걸었다.

![image](https://user-images.githubusercontent.com/53170968/112508793-3747cb80-8dd3-11eb-83ef-fb337686104c.png)

![image](https://user-images.githubusercontent.com/53170968/112508806-3a42bc00-8dd3-11eb-95d9-9423d30af5d9.png)

25. 첫번째 breakpoint가 지나면 [ebp-0xc]메모리 공간의 내용이 변한 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112509374-c0f79900-8dd3-11eb-898f-27d8e6977da4.png)

26. 다음으로 fgets에 걸린 breakpoint를 확인해보자. 아직 fgets가 실행되기 전의 메모리 상태이다.

![image](https://user-images.githubusercontent.com/53170968/112509491-dcfb3a80-8dd3-11eb-8e30-c9c0453a128e.png)

27. 'A' 8개를 입력한 결과 메모리 공간에 입력된 것을 볼 수 있다.

28. 그런데 [ebp-0x8c]의 메모리 공간은 보이는데 [ebp-0xc]의 메모리 공간은 보이지 않는다.

29. [ebp-0x8c]부터 [ebp-0xc]의 공간까지 계산해 봤더니 8*16Byte이다. 현재 메모리공간 출력은 16Byte씩 8줄로 출력되고 있다. 즉, [ebp-0xc]의 공간은 현재 출력된 메모리 공간 바로 다음 줄에 출력된다.

![image](https://user-images.githubusercontent.com/53170968/112510116-7aef0500-8dd4-11eb-9d20-4031abde8464.png)

30. 표시되는 출력 수를 늘렸더니 [ebp-0xc] 공간이 보이는 것을 볼 수 있다.

31. 우리가 이제 입력해야할 값은 정해졌다. 8*16Byte = 128Byte만큼 데이터를 입력하고 shell함수의 주소값인 0x0804849b을 입력해주면 된다.

32. 총 입력 크기는 128 + 4 = 132Byte를 입력하게 된다. fgets의 입력크기 제한이 133Byte이므로 입력 제한 값을 넘어가지 않는다.

![image](https://user-images.githubusercontent.com/53170968/112510766-18e2cf80-8dd5-11eb-8f48-12b50212b31b.png)

33. 이렇게 python을 이용해서 데이터를 입력시키자. 역시나 리틀엔디안방식을 고려해서 shell함수의 주소값을 1Byte씩 역순으로 입력하자.

![image](https://user-images.githubusercontent.com/53170968/112510966-4fb8e580-8dd5-11eb-8338-925a76c90559.png)

34. fgets함수가 호출되기 전에 메모리 공간을 확인해보면 [ebp-0xc]의 공간에 '하아아아아아아아아앙'이 출력되는 함수의 메모리 주소값이 저장된 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112511215-8ee73680-8dd5-11eb-8ea1-82c07faf5b9e.png)

35. fgets를 통해서 값을 입력한 것을 확인해보면 'A'단어가 128개가 입력되었고 BOF가 발생하여 [ebp-0xc]에 shell함수의 메모리 주소값이 저장된 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112511596-e9809280-8dd5-11eb-9641-db0448588db8.png)

36. 그리고 '하아아아아아아아아앙'이 출력되지 않고 프로그램이 종료된 것을 볼 수 있다. 쉘권한을 얻어야하지만 로컬에서 동작하여서 쉘이 출력되지 않은 것 같다.

![image](https://user-images.githubusercontent.com/53170968/112511815-1f257b80-8dd6-11eb-9b19-a105bc0d2436.png)

37. solution.py를 사용해서 위의 host에 접속해서 데이터를 전달해보자.

![image](https://user-images.githubusercontent.com/53170968/112511923-37959600-8dd6-11eb-9145-c7cfc61c0950.png)

38. 해당 host의 쉘권한을 얻어서 cat명령어를 통해서 FLAG를 얻을 수 있다.

![image](https://user-images.githubusercontent.com/53170968/112512114-6b70bb80-8dd6-11eb-9b57-eef51755574d.png)

![image](https://user-images.githubusercontent.com/53170968/112512125-6e6bac00-8dd6-11eb-864f-c81957af9ec2.png)

39. 이렇게 정답처리가 되었다.
