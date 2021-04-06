# Toddler's Bottle - random

### Problem
![image](https://user-images.githubusercontent.com/53170968/113676365-4f82e900-96f7-11eb-8358-245e74c0c88b.png)

### Solution
1. ssh를 통해서 해당 문제에 접속하자.

![image](https://user-images.githubusercontent.com/53170968/113676405-5b6eab00-96f7-11eb-9e17-694559e7b292.png)

2. 어떤 파일이 있나 먼저 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113676429-63c6e600-96f7-11eb-87f2-e353e11349b5.png)

3. 언제나처럼 flag파일이 존재하고 해당 파일을 읽을 수 있는 random파일이 존재한다.

4. 소스코드의 내용은 정말 간단하다.

5. random한 값과 내가 입력한 값을 XOR 연산한 값이 0xdeadbeef이면 FLAG를 출력해준다.

6. gdb를 통해서 조금 더 자세히 분석해보자.

![image](https://user-images.githubusercontent.com/53170968/113676711-be604200-96f7-11eb-95b5-66cc7a7796ab.png)

7. gdb에 접속하고 어셈블리 출력방식을 intel로 바꾸었다.

![image](https://user-images.githubusercontent.com/53170968/113676796-d20ba880-96f7-11eb-8ff3-4f5c131bf6a6.png)

![image](https://user-images.githubusercontent.com/53170968/113676805-d33cd580-96f7-11eb-9cc6-5485e100bb1b.png)

8. main함수를 확인해보자.

9. rand함수를 통해 생성된 랜덤값은 [rbp-0x4]의 위치에 저장된다.

10. 그리고 scanf를 통해 사용자에게 입력받는 값은 [rbp-0x8]의 위치에 저장된다.

11. 메모리 분석을 하기는 매우 편한 것 같다.

12. 소스코드를 다시 확인해보니 이상한 부분이 있었다. 바로 scanf에 passcode1의 주소값이 아닌 passcode1자체가 들어 있었다. 즉, &기호가 변수 앞에 붙어있지 않았다.

![image](https://user-images.githubusercontent.com/53170968/113677012-10a16300-96f8-11eb-8929-b1486559ad67.png)

13. 먼저 breakpoint를 걸어서 메모리의 변화를 확인할 수 있도록 해보자.

![image](https://user-images.githubusercontent.com/53170968/113677104-2adb4100-96f8-11eb-8d68-6658127b2f74.png)

14. 실행 후에 메모리를 확인해보자. [rbp-0x8]의 위치 메모리를 확인했다.

15. 빨간 네모는 [rbp-0x8], 파란 네모는 [rbp-0x4]의 메모리이다.

![image](https://user-images.githubusercontent.com/53170968/113677250-5827ef00-96f8-11eb-9b34-e7cf71448c8a.png)

16. rand함수가 실행되어 랜덤한 값이 저장된 것을 확인해보면 [rbp-0x4]의 위치인 파란 네모의 메모리가 변화한 것을 볼 수 있다.

17. random 데이터는 0x6b8b4567이다. 그렇다면 우리는 scanf에 0x6b8b4567과 XOR을 한 결과가 0xdeadbeef가 나오는 값을 입력하면 된다.

![image](https://user-images.githubusercontent.com/53170968/113677683-d08eb000-96f8-11eb-8e9d-4b0f518e5948.png)

18. XOR연산에는 특별한 성질이 있다. A ^ B = C 라면 A ^ C = B가 성립한다.

19. 즉, 0x6b8b4567에 0xdeadbeef를 XOR연산하면 우리가 입력해야할 값이 나온다.

![image](https://user-images.githubusercontent.com/53170968/113677854-fcaa3100-96f8-11eb-8534-9396251bbefc.png)

20. 정확한 결과가 맞는지 다시 확인해보면 XOR한 연산 결과가 deadbeef가 나오는 것을 확인할 수 있다.

21. 우리가 입력해야할 값은 0xb526fb88이다. 단, scanf는 16진수 정수를 입력받는 것이 아닌 10진수 정수를 입력받기 때문에 해당 데이터를 10진수로 변환해주어야한다.

![image](https://user-images.githubusercontent.com/53170968/113678249-688c9980-96f9-11eb-9568-012d43092b94.png)

22. 10진수로 변환한 결과가 3039230856인 것을 볼 수 있다.

23. 이제 이 데이터를 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/113678342-7fcb8700-96f9-11eb-86fa-8bad38ef6699.png)

24. 입력한 결과 if문이 참이 되어서 if문 내의 'GOOD!'이 출력되었다.

25. 그리고 FLAG가 출력되어야하는데..... 권한부족이라는 오류가 발생했다.

26. 그래서 gdb를 나와서 권한을 확인해봤다..

![image](https://user-images.githubusercontent.com/53170968/113678616-cde08a80-96f9-11eb-8e24-0e4b06764de7.png)

27. 분명 실행권한에는 Set-UID가 설정되어 있다. 그런데.... gdb를 통해서 실행하면 권한부족이라는 결과가 나온다.

28. 그렇다면 gdb를 사용하지 않고 그냥 실행해야할 것 같은데 그냥 실행하면 우리는 random값을 알 수가 없다.

29. 여기서 우리는 저 rand함수의 특성을 알아야한다.

    <https://blog.naver.com/coms1101/221279050700>

30. 위 URL로 가면 랜덤함수의 설명이 자세히 되어있다.

31. 간단하게 지금 필요한 내용만 가져오자면 rand함수는 seed값을 주지않으면 첫 실행에서는 어떠한 값이 나올지 모르는 random함 값이 나오지만 이후의 실행에서는 처음 설정된 random값으 그대로 계속 사용된다는 것이다.

32. 즉, 저 rand함수로 만들어진 데이터는 몇 번을 실행하든지 0x6b8b4567이라는 것이다.

33. 그렇다면 우리는 저 파일을 그냥 실행해서 XOR연산 결과가 0xdeadbeef가 나오는 3039230856을 입력하면 된다.

![image](https://user-images.githubusercontent.com/53170968/113679134-624aed00-96fa-11eb-8489-abb1b0a0d019.png)

34. 이렇게 정상적으로 if문의 조건식이 참이되어 FLAG가 출력되었다.

35. 사이트에서 정답이 맞는지 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113679223-81e21580-96fa-11eb-83a9-dc9253d2e5b0.png)

![image](https://user-images.githubusercontent.com/53170968/113679238-86a6c980-96fa-11eb-9676-514ec102aa7c.png)

36. 정상적으로 정답처리 되었다.