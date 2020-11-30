# login filtering

### Problem

![image](https://user-images.githubusercontent.com/53170968/100620685-0c3bf680-3362-11eb-816f-aaed172e02b7.png)

### Solution
1. 로그인 필터링을 할 수 있냐고 묻는 문제다. 일단 사이트에 들어가보자.

![image](https://user-images.githubusercontent.com/53170968/100620786-2675d480-3362-11eb-82d9-eed7f7ab1dc8.png)

2. 아이디와 패스워드를 입력해서 로그인을 하는거다.

3. get source를 눌러서 이 웹사이트의 코드를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/100620804-2c6bb580-3362-11eb-9de8-558474f9d3cf.png)

4. 주요 코드는 다음 2부분인 것 같다.

5. mysql_fetch_array는 mysql 데이터베이스에 연결하여 해당 sql문의 결과를 얻어 오는 코드이다.

![image](https://user-images.githubusercontent.com/53170968/100620952-62109e80-3362-11eb-8d29-0927734b7521.png)

5. $row에 sql문으로 얻은 결과를 저장한다.

![image](https://user-images.githubusercontent.com/53170968/100621080-8b312f00-3362-11eb-917e-805238e5e61b.png)

6. 만약 $row에 값이 설정되지 않았다면 worng..이라는 문장를 보여주고 로그인이 되지만 아이디가 guest나 blueh4g라면 'your account is blockec'라는 문장을 보여주어 해당 아이디를 쓸 수 없다라고 보여준다.

7. 개발자 모드의 소스코드도 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/100626341-0e558380-3369-11eb-8adf-ad4a2e096769.png)

8. 아래쪽에 주석으로 block된 아이디와 비밀번호를 알려준다.

![image](https://user-images.githubusercontent.com/53170968/100619102-0513e900-3360-11eb-80d8-9cb476f11941.png)

9. SQL문의 특성에 대해 알아보면 SQL에서는 대소문자를 구분하지 않는다.

10. 다음 예시를 보면

![image](https://user-images.githubusercontent.com/53170968/100626238-e8c87a00-3368-11eb-9ae0-762a48d263bb.png)

11. 간단한 회원들의 정보가 있는 데이터베이스 테이블이다.

![image](https://user-images.githubusercontent.com/53170968/100628754-e87dae00-336b-11eb-8328-064182f670af.png)

12. where문으로 'nara' 아이디의 정보를 비밀번호와 함께 확인하여 출력한다.

13. 현재 웹사이트에서 확인하는 방법과 동일하다.

14. 하지만 만약 nara를 Nara로 제일 앞의 n만 소문자에서 대문자로 바꾸면 어떻게 될까?

![image](https://user-images.githubusercontent.com/53170968/100626254-f251e200-3368-11eb-966a-d31af16849e1.png)

15. 앞선 결과와 같아진다. 즉, 대소문자 구분없이 출력이 된다.

16. 하지만 php는 다르다. 대소문자 구분을 확실하게 한다.

17. 이 문제는 정말 간단하게 guest라은 아이디를 Guest로 변경하여 로그인하면 바로 해결될 수 있다.

18. 한 번 해보자.

![image](https://user-images.githubusercontent.com/53170968/100625614-18c34d80-3368-11eb-8a16-c816bbe3bc0c.png)

19. 아이디는 Guest 비밀번호는 guest로 해서 로그인을 해보자.

![image](https://user-images.githubusercontent.com/53170968/100625640-2082f200-3368-11eb-89a1-a576a7d56761.png)

20. 로그인해 성공해서 FLAG를 획득했다. SQL문을 다뤄보고 보안 위협이 있는 부분을 생각해보고 풀어야 하는 간단하지만 생각이 필요한 문제였다.