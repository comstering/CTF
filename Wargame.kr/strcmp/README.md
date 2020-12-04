# strcmp

### Problem

![image](https://user-images.githubusercontent.com/53170968/101166495-b5912e00-367b-11eb-9be9-fc49b5672e95.png)

### Solution
1. strcmp의 취약점을 찾아내는 문제다. 한번 알아보자.

![image](https://user-images.githubusercontent.com/53170968/101166508-baee7880-367b-11eb-85e2-e38d90bed0be.png)

2. 문제 자체는 정말 간단해 보인다. 패스워드를 입력해서 'chk'버튼을 누르면  결과를 보여주는 것 같다.

3. view-source로 소스먼저 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/101166520-bf1a9600-367b-11eb-8c1d-245bd691af8b.png)

4. 소스의 내용을 보니 일단 어떠한 파일에서 비밀번호 문장 랜덤하게 가져와서 내가 입력한 문자열과 비교를 한다.

5. 여기서 strcmp를 이용하여 입력한 문자열과 랜덤하게 가져온 문자열을 비교한다.

6. 여기서 해결할 키워드는 문제자체에서 언급했듯이 strcmp의 비교연산에서 취약점이 존재하는지를 찾는 것 같다.

7. 간단하게 검색창에 strcmp 취약점이라고 검색해보자.

![image](https://user-images.githubusercontent.com/53170968/101166552-ce014880-367b-11eb-9615-14a0c3346f3a.png)

8. 바로 strcmp 인증우회라는 키워드로 많은 내용들이 나온다.

9. 한번 들어가서 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/101166616-eb361700-367b-11eb-828f-dc1a9e6cfd5e.png)

10. 중요 내용만 캡쳐해보았다.

11. php로 매개변수로 값을 넘길 때 배열형태로 넘겨서 그 값이 strcmp에 들어가면 strcmp는 1, 0, -1의 값이 아닌 NULL값을 반환한다는 것이다.

12. 여기서 NULL을 주요하게 봐야하는게 NULL값은 0과 같다라고 인식하기 때문에 strcmp가 NULL값으로 바뀌면 비밀번호가 정확하지 않아도 'strcmp == 0' 이라는 문장에서 참으로 성립이 된다.

13. 이 문제를 해결하기 이해서는 php에서 '=='연산의 느슨한 비교가 아닌 '==='연산의 엄격한 비교를 진행하면 해당 취약점을 보완할 수 있다.

14. 그러면 소스코드를 다시 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/101166520-bf1a9600-367b-11eb-8c1d-245bd691af8b.png)

15. strcmp를 이용해서 비교연산을 진행하고 있으며 느슨한 비교연산인 '=='연산을 사용한다.

16. 즉, 아까 검색한 키워드의 취약점이 존재한다는 것이다.

17. 문제로 돌아가서 F12를 눌러서 개발자모드를 실행하자.

![image](https://user-images.githubusercontent.com/53170968/101168564-f63e7680-367e-11eb-9b51-7034a1877dff.png)

18. input태그의 name으로 'password'가 설정되어 있다. 이것을 배열형태인 'password[]'로 변경하자.

![image](https://user-images.githubusercontent.com/53170968/101166717-0ef95d00-367c-11eb-8717-4955bfcbda6e.png)

19. 이렇게 변경한 상태에서 패스워드를 아무거나 입력해서 chk버튼을 클릭하자.

![image](https://user-images.githubusercontent.com/53170968/101169546-76191080-3680-11eb-8a68-744f5083987f.png)

![image](https://user-images.githubusercontent.com/53170968/101166736-1ae51f00-367c-11eb-8e31-7adf57b28e27.png)

20. 이렇게 FLAG를 획득할 수 있다.