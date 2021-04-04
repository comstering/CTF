# Toddler's Bottle - flag

### Problem
![image](https://user-images.githubusercontent.com/53170968/113508765-d1a2ce80-958c-11eb-8b25-2ca770eff840.png)

### Solution
1. wget을 통해서 파일을 다운받고 실행권한까지 주도록 하자.

![image](https://user-images.githubusercontent.com/53170968/113508801-0747b780-958d-11eb-8124-57feaec25a5d.png)

2. gdb를 통해서 분석해보도록 하자.

![image](https://user-images.githubusercontent.com/53170968/113508825-2e9e8480-958d-11eb-9696-524474e762ab.png)

3. 어셈블리 코드 출력방식을 intel로 변경했다. 이제 각 함수별로 내용을 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113508936-c7350480-958d-11eb-9001-b8419b9af170.png)

4. 그런데...... 가장 기본인 main함수가 아예 없다고 한다... 무슨 일이지....

5. 다른 함수도 있는지 확인했지만 존재하지 않았다.

![image](https://user-images.githubusercontent.com/53170968/113508950-e7fd5a00-958d-11eb-8339-b57938e16a33.png)

6. 그래서 윈도우 환경으로 파일을 가져왔다.

![image](https://user-images.githubusercontent.com/53170968/113508957-f51a4900-958d-11eb-9199-a74928fe382b.png)

7. 윈도우에서 IDA를 통해서 리버싱 시켜보았다.

![image](https://user-images.githubusercontent.com/53170968/113508965-082d1900-958e-11eb-9fed-76347e3afb45.png)

8. Hex View를 확인했더니 살짝의 hint가 될만한 내용이 적혀있다.

9. 이 파일은 UPX 패킹이 되어 있다고 한다.

10. UPX 패킹이 무엇인지 알아보자.

![image](https://user-images.githubusercontent.com/53170968/113508987-2abf3200-958e-11eb-9005-1c113f21864b.png)

11. 간단하게 말해서 패킹이란 실행 압축이다.

12. 이 실행압축을 하면 파일의 용량을 줄일 수 있고 크래커의 리버싱으로 부터 파일을 보호할 수 있다.

13. 그렇다면 패킹이 있듯이 언패킹도 있다.

14. <https://github.com/upx/upx/releases/tag/v3.95> 이 사이트에 가서 UPX툴을 다운 받을 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113509051-6fe36400-958e-11eb-9a8f-3be80b43b1ec.png)

15. 하지만 나는 Kali Linux를 사용하고 있다.

16. Kali Linux에는 upx툴이 기본으로 제공되고 있다.

![image](https://user-images.githubusercontent.com/53170968/113509071-8c7f9c00-958e-11eb-9773-58bc9a71872a.png)

17. -d 옵션을 통해서 언패킹을 진행하자.

![image](https://user-images.githubusercontent.com/53170968/113509088-9e613f00-958e-11eb-8561-c3cf984b0a05.png)

18. 이제 다시 gdb를 통해서 파일을 분석해보자.

![image](https://user-images.githubusercontent.com/53170968/113509099-acaf5b00-958e-11eb-8302-5fcf4e4116b1.png)

19. 언패킹 전에는 확인할 수 없었던 main함수를 확인할 수 있었다.

![image](https://user-images.githubusercontent.com/53170968/113509108-bd5fd100-958e-11eb-99b0-3ffe41008cef.png)

20. 크게 눈에 띄는 것은 저 3개이다.

21. 그 중에서도 flag의 내용을 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113509136-e3857100-958e-11eb-9141-c732cc6293c5.png)

22. flag의 첫 데이터로 0x00496628의 주소값이 보인다. 해당 주소값으로 이동해보자.

![image](https://user-images.githubusercontent.com/53170968/113509166-09127a80-958f-11eb-8de5-d4d269ed101b.png)

23. 확인해 봤더니 뭔가 데이터가 많아보인다. 좀 더 길게 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113509179-19c2f080-958f-11eb-9d13-29895f8f5db3.png)

24. 많은 양의 데이터가 보이긴 하지만 16진수로 되어 있어서 정확한 내용은 잘 모르겠다.

25. 출력 방식을 16진수 방식이 아닌 String방식으로 변경해서 해당 주소값을 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113509201-395a1900-958f-11eb-89af-20788f9b3932.png)

26. 그랬더니 지금까지 보았던 FLAG와 비슷한 내용이 나왔다.

27. 사이트로 이동해서 정답인지 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113509219-5db5f580-958f-11eb-94c4-a621bd65d2c1.png)

![image](https://user-images.githubusercontent.com/53170968/113509222-60184f80-958f-11eb-8471-2faa034aaa6e.png)

28. 이렇게 정답처리가 완료되었다.