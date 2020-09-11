# Shifty Science

### Problem
    This flag was tampered with by a shifty scientist. Can you get it back to normal?
    
    BO20{xtmiam_lwvb_bzg_apqnba_tqsm_bpqa_ib_pwum}

### Solution
1. 이 문제는 가장 고전암호인 시저암호(카이사르 암호)를 활용하는 것 같다.
2. 기호와 숫자를 제외한 문자만을 기준으로 보면 BO는 TG보다 18만큼 앞쪽에 있는 것을 알 수 있다.
3. 그렇다면 다른 문자들 역시 기본의 숫자들 보다 18만큼 앞쪽에 있다는 해석을 할 수 있다.
4. 시저암호를 복호화 해보자!!
5. 먼저 키값을 18로 입력한다.
![caesar1](https://user-images.githubusercontent.com/53170968/92907044-f5bb8880-f45f-11ea-9196-0f7648ac7d40.png)

6. 복호화할 문장을 넣고
![caesar2](https://user-images.githubusercontent.com/53170968/92907054-f6ecb580-f45f-11ea-9efb-6e341e01df52.png)

7. 결과를 보자
![caesar3](https://user-images.githubusercontent.com/53170968/92907062-f81de280-f45f-11ea-8ddd-8b87f469e0c4.png)

8. 결과가 이상하다... 기본적으로 젤 앞에 BO20이 TG20이 아닌 jw20으로 나왔다.

9. 복호화라는 개념라서 그런가...? 키를 -18로 두고 다시 해보자
![caesar4](https://user-images.githubusercontent.com/53170968/92907069-f9e7a600-f45f-11ea-9d4f-b2a3e9e49b92.png)

![caesar5](https://user-images.githubusercontent.com/53170968/92907076-fa803c80-f45f-11ea-95cd-52f8bde4a81e.png)


10. 결과가 잘 나왔다. 복호화라는 개념이라서 그런가 반대로 생각해야 했었나 보다.
11. 그럼 답을 입력해보자
![sol](https://user-images.githubusercontent.com/53170968/92907081-fbb16980-f45f-11ea-91c9-d6899ef2273b.png)


12. 정답이다!! 이 문제는 BO20을 보고 시저암호라는 생각이 들면 바로 풀 수 있었던 문제같다.