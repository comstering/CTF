# Toddler's Bottle - collision

### Problem
![image](https://user-images.githubusercontent.com/53170968/113151467-10284880-9270-11eb-8b91-bb579b5af145.png)

### Solution
1. ssh로 해당 host에 접속하자.

![image](https://user-images.githubusercontent.com/53170968/113148424-c853f200-926c-11eb-8eb5-5c8ad957efb7.png)

2. 그리고 파일을 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113151564-2df5ad80-9270-11eb-932c-46b31faf84be.png)

3. flag파일은 역시나 확인할 수 없다.

4. col파일을 실행해서 flag파일을 확인할 것 같다.

5. col파일의 소스코드인 col.c파일을 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/113151732-58476b00-9270-11eb-82b7-a5abd77c963d.png)

6. 소스코드는 크게 어렵지 않다. hashcode라는 데이터가 존재하고 저 데이터와 입력한 데이터가 같으면 flag를 출력해준다.

7. 단, 내가 입력한 값이 check_password함수를 통해서 변환되고 변환된 값이 hashcode와 비교된다.

8. check_password함수를 분석해보자.

9. 코드는 간단하다. 입력한 데이터가 저장되어 있는 주소값은 1Byte단위로 끊어져서 데이터가 저장되어 있다.

![image](https://user-images.githubusercontent.com/53170968/113152297-f5a29f00-9270-11eb-90f7-e50460ed4c12.png)

10. 이 데이터를 int형 주소값 4Byte의 크기만큼으로 바꿔서 읽게 한다.   

11. 그리고 이러한 과정을 배열로 만들어 int형 주소공간을 5번 입력받는다.

![image](https://user-images.githubusercontent.com/53170968/113152354-02bf8e00-9271-11eb-9d1a-c6f10723c47a.png)

12. 이러한 형식으로 포인터 p가 가리키는 주소공간이 바뀌게 된다.

13. 코드를 보면 res값은 int형 주소공간 5개에 저장되어 있는 데이터를 모두 더한다.

14. 그리고 check_password함수는 그 res값을 반환한다.

15. 즉, 최종적으로 res값과 hashcoded의 값이 비교되는 것이다.

16. hashcode의 값은 0x21DD09EC라고 되어 있다. 10진수로 변환해보자.

![image](https://user-images.githubusercontent.com/53170968/113152673-5205be80-9271-11eb-800c-b4b3ce8b12d6.png)

17. 568134124라는 결과가 나온다.

![image](https://user-images.githubusercontent.com/53170968/113152761-69dd4280-9271-11eb-81f9-63f6c5ec913e.png)

18. 568134124를 5로 나누면 113626824.8이라는 결과가 나온다.

![image](https://user-images.githubusercontent.com/53170968/113152842-7cf01280-9271-11eb-9d54-3a9daed53dc9.png)

19. 소수점은 버리고 정수만을 다시 X5하면 568134120이라는 결과가 나온다.

20. 즉, 4번의 입력을 113626824로 입력하고 나머지 한번을 113626828로 입력하면 res에는 56813424라는 값이 저장될 것이다.

21. 113626824를 16진수로 바꿔보자.

![image](https://user-images.githubusercontent.com/53170968/113153091-b7f24600-9271-11eb-885f-81da7a5c7641.png)

22. 6c5cec8이 나왔다. 4번은 6c5cec8, 1번은 6c5cecc로 입력하면 된다.

23. 데이터를 입력해보자.

![image](https://user-images.githubusercontent.com/53170968/113153272-e2440380-9271-11eb-90d4-64f8dc3d0ea3.png)

24. python을 이용해서 입력하고자 python이 해당 host에 있는지 확인했는데 존재했다. 조금 더 간단하게 문제를 풀 수 있겠다.

![image](https://user-images.githubusercontent.com/53170968/113153375-fd167800-9271-11eb-883f-8ef3a2f37266.png)

25. python을 이용해서 데이터를 입력했다. 이때 중요한 점은 메모리구조를 알고 리틀엔디안을 고려해서 1Byte씩 역순으로 데이터를 입력해야한다는 것이다.

![image](https://user-images.githubusercontent.com/53170968/113153568-30f19d80-9272-11eb-892d-1fb8c2619e2c.png)

![image](https://user-images.githubusercontent.com/53170968/113153577-32bb6100-9272-11eb-9482-5154d76764e4.png)

26. 획득한 FLAG를 사이트에 입력해서 정답으로 처리되었다.