# 내 버퍼가 흘러넘친다!!!

### Problem
![image](https://user-images.githubusercontent.com/53170968/113141899-3eecf180-9265-11eb-8302-999bc01c2811.png)

### Solution
1. 파일을 다운 받고 실행권한을 주어서 파일을 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/113141969-5330ee80-9265-11eb-9848-ac4e66f84e2e.png)

2. 따로 출력문은 없는 것 같다. 내 입력만 받고 프로그램이 종료한다.

![image](https://user-images.githubusercontent.com/53170968/113142171-8f644f00-9265-11eb-82ba-c23ea0e9d25b.png)

3. gdb를 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/113142317-b458c200-9265-11eb-893e-d685202002cf.png)

![image](https://user-images.githubusercontent.com/53170968/113142324-b6228580-9265-11eb-9b1b-d64094fe33d7.png)

4. 언제나 처럼 main함수를 먼저 확인하자.

5. setvbuf함수는 Basic_FSB에서 말했듯이 버퍼설정 함수인데 mode로 2값이 들어가서 버퍼설정을 안한다. 있느나마나한 함수..?

6. 그리고 printf, read, printf, gets가 나오는 것을 볼 수 있다.

7. 두 printf는 각각 'Name : ', 'input : '이다.

![image](https://user-images.githubusercontent.com/53170968/113142979-8de75680-9266-11eb-89d9-a6c694341fcb.png)

8. 숨겨져 있는 다른 함수가 있나 봤더니 딱히 없다.

9. 우리가 직접 쉘권한을 주어야하는 것이다.

10. 이번 문제는 쉘코드를 만들어서 쉘코드가 실행되도록 하는 문제이다.

11. 나머지 두 함수를 살펴보자.

![image](https://user-images.githubusercontent.com/53170968/113143299-f20a1a80-9266-11eb-9764-b7df74975ec7.png)

12. read함수는 입력함수이다. 보통 파일입력에 사용하는 함수인데ㅐ 일반 표준 입력도 가능하다.

13. 위의 코드를 기준으로 read함수를 c언어로 바꿔보자.

14. read(int fd, void* buf, size_t size); -> read(0x0, 0x804a060, 0x32); -> read(0, 0x804a060, 50);

15. 최종 결과는 'read(0, 0x804a060, 50);'이다.

16. 첫번째 매개변수에는 원래 파일에 대한 내용이 나온다. 여기에 0이 입력되면 표준입력을 의미한다.

17. 두번째 매개변수는 데이터가 저장될 버퍼, 3번째는 입력되는 크기이다.

![image](https://user-images.githubusercontent.com/53170968/113144000-bde32980-9267-11eb-8d56-99ba273b9b3c.png)

18. gets함수를 확인해보자.

19. 먼저 eax에 [ebp-0x14]의 데이터가 복사되고 그 위치에 gets로 입력받은 데이터가 저장된다.

![image](https://user-images.githubusercontent.com/53170968/113144424-30540980-9268-11eb-8571-9e9727c93826.png)

20. 분석은 마쳤으니 breakpoint를 걸고 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/113144577-58dc0380-9268-11eb-9c62-964bcb99fb71.png)

21. ebp레지스터에는 주소값이 저장되어 있다. 해당 주소값의 데이터를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113144657-71e4b480-9268-11eb-9087-aeca284a7863.png)

22. 현재 메모리에는 아무런 데이터가 저장되어 있지 않다.

23. 계속 실행해서 한 번 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113144854-b40df600-9268-11eb-8827-168c9dcae760.png)

24. read함수가 호출되기 전 read함수의 매개변수인 주소값을 확인해보면 아무런 데이터가 저장되어 있지 않다.

![image](https://user-images.githubusercontent.com/53170968/113144955-cee06a80-9268-11eb-98c3-127f83e2d3d2.png)

25. read함수가 실행되고 다시 확인해보면 AAAAAAAA의 데이터가 저장되어 있다.

26. 그리고 gets함수에서 사용되는 메모리 주소를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113145096-fb948200-9268-11eb-8d94-2fc429a39699.png)

![image](https://user-images.githubusercontent.com/53170968/113145137-05b68080-9269-11eb-86d2-4d67b02d10da.png)

27. eax의 데이터는 [ebp-0x14]의 데이터가 복사되었기에 두 위치가 동일한 것을 볼 수 있다.

28. 이제 쉘권한을 얻는 방법만 생각하면 된다.

29. 먼저 쉘권한을 얻을 수 있는 쉘코드를 사용하자.

30. \x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80

31. 나는 26Byte의 쉘코드를 사용했다.

32. 그리고 다시 코드를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113145421-5a59fb80-9269-11eb-828f-739451686aa0.png)

33. 저 gets함수를 보면 [ebp-0x14]의 레지스터에 데이터를 저장한다. 그런데 ebp는 프로그램 시작에 지역변수로 스택 영역에 쌓은 데이터이다. 즉, 이 프로그램에서 하나만 존재하는 변수라는 뜻이다.

![image](https://user-images.githubusercontent.com/53170968/113145682-adcc4980-9269-11eb-8ad4-a0e57d1b7ed5.png)

34. 그렇다면 stack영역은 이렇게 메모리구조로 되어 있을 것이다.

35. 그렇다면 buf에 BOF를 발생시켜서 ret의 복귀 주소값을 변경하면 해당 문제를 쉽게 풀 수 있다.

![image](https://user-images.githubusercontent.com/53170968/113145702-b7ee4800-9269-11eb-9825-4439e577a6d2.png)

36. 이러한 방식으로 동작하도록 BOF가 발생하면 문제를 풀 수 있다.

37. exploit을 만들어 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/113145892-f7b52f80-9269-11eb-8d95-dc55c086cfc0.png)

38. 그런데 쉘권한을 얻지 못했다.

39. 왜일까.. 생각했는데 Wargame에서는 보통 주어진 것을 모두 이용하는 것이 좋다. 하지만 우리가 사용하지 않은 부분이 있다. 바로 read함수에서 입력되는 버퍼이다. 그래서 동작 방식을 조금 변경해봤다.

![image](https://user-images.githubusercontent.com/53170968/113146494-b40ef580-926a-11eb-9465-c53cd61b9c79.png)

40. name의 위치는 read로 데이터를 입력받는 버퍼의 메모리 주소이다.

41. 그렇다면 메모리 주소를 확인해보고 exploit을 수정해보자.

![image](https://user-images.githubusercontent.com/53170968/113146629-dd2f8600-926a-11eb-9bf3-fd794fe89eac.png)

42. 주소값을 확인하고 이제 실행해보자.

![image](https://user-images.githubusercontent.com/53170968/113146685-ee789280-926a-11eb-92bf-e96849540d6f.png)

43. 실행했는데 이번에도 권한을 얻지 못했다. 왜그럴까 했는데 혹시나 해서 해당 문제의 서버 host에 접속해보기로 했다.

![image](https://user-images.githubusercontent.com/53170968/113146773-0a7c3400-926b-11eb-8d72-6d740072abe0.png)

44. 정상적으로 FLAG를 획득했다. HackCTF의 문제들은 무엇때문인지 모르겠지만 로컬에서는 해결이 안되는 문제들이 조금 있는 것 같다.

45. 이제 FLAG를 획득했으니 정답을 제출해보자.

![image](https://user-images.githubusercontent.com/53170968/113146885-2c75b680-926b-11eb-95db-9ef9125c3ce3.png)

![image](https://user-images.githubusercontent.com/53170968/113146894-2e3f7a00-926b-11eb-8312-062d0c20e070.png)

46. 정답으로 처리되었다.