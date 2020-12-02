# fly me to the moon

### Problem

![image](https://user-images.githubusercontent.com/53170968/100875182-06245200-34e9-11eb-945b-f947f26de60b.png)

### Solution
1. 자바스크립트 게임이다. 해당 게임을 깰 수 있냐고 묻는다. 문제로 가보자.

![image](https://user-images.githubusercontent.com/53170968/100875244-1b00e580-34e9-11eb-8529-a338c1681d26.png)

2. 게임화면이 나왔다 플레이를 한번 해보자.

![image](https://user-images.githubusercontent.com/53170968/100876620-fad22600-34ea-11eb-9b0d-d62db45a155f.png)

3. 양쪽 벽을 피해서 우주선을 움직이면 이동한 거리만큼 점수를 얻는 게임이다.

![image](https://user-images.githubusercontent.com/53170968/100876646-0291ca80-34eb-11eb-9f6d-f58ca538b462.png)

4. 클리어 조건은 점수가 31337점이면 게임을 클리어하는 것 같다.

5. 개발자 모드로 코드를 먼저 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/100875276-26eca780-34e9-11eb-84a4-84d8efef5feb.png)

6. 자바스크립트를 보니 무슨 소리인지 모르게 코드가 나와있다.

7. 가장 편하게 생각할 수 있는 난독화를 키워드로 검색해보자.

![image](https://user-images.githubusercontent.com/53170968/100875311-34099680-34e9-11eb-9fa7-e46d62c452ef.png)

8. 자바스크립트를 난독화하여 다른 사람들이 로직이나 내용을 알아볼 수 없도록 하는 방법이 있다.

9. 그렇다면 반대로 이 난독화된 코드를 되돌리는 방법도 있지 않을까?

10. 복호화라는 키워드로 다시 검색해보자.

![image](https://user-images.githubusercontent.com/53170968/100875644-a4181c80-34e9-11eb-89fa-fb86531f9474.png)

11. 난독화 해제 사이트들이 많다. 검색결과 중 하나에 들어가보자.

![image](https://user-images.githubusercontent.com/53170968/100876022-2bfe2680-34ea-11eb-98bf-cffcc24f6123.png)

12. 블로그에 난독화 해제 사이트를 알려준다. 해당 사이트로 가본다.

![image](https://user-images.githubusercontent.com/53170968/100876046-33bdcb00-34ea-11eb-8708-b1b5bbe6a10d.png)

13. 사이트에서 난독화된 코드를 입력하면 복호화 해주는 것 같다. 그러면 아까 문제코드에서 난독화된 자바스크립트 코드를 복붙해보자.

![image](https://user-images.githubusercontent.com/53170968/100876091-43d5aa80-34ea-11eb-938e-cb751c17292b.png)

14. Beautify Code로 복호화 시켜보았다.

![image](https://user-images.githubusercontent.com/53170968/100876128-4c2de580-34ea-11eb-905b-f96f1f5d4a0d.png)

15. 복호된 코드가 나왔다. 이제 코드를 분석해보자.

![image](https://user-images.githubusercontent.com/53170968/100876368-a3cc5100-34ea-11eb-8267-4933e155fe1d.png)

16. 아마 이 getScore가 점수값를 얻는 코드인 것 같다. getScore에 해당하는 함수는 _0x8618x7()이다 저 함수를 찾아보자.

![image](https://user-images.githubusercontent.com/53170968/100876402-b181d680-34ea-11eb-8591-fc72c7f1a7e7.png)

17. 바로 위에 해당 함수가 있다. 함수 내용이 _0x8618x6의 값을 반환하는 함수이다. 그렇다면 다시 변수 _0x8618x6를 찾아보자.

![image](https://user-images.githubusercontent.com/53170968/100876434-bb0b3e80-34ea-11eb-817e-65af27e3c317.png)

18. 바로 위에 변수가 있는 것을 알 수 있다. 그렇다면 저 값을 31337로 바꿔주면 점수가 31337점으로 도달한 것과 같은 결과를 얻을 수 있을 것이다.

![image](https://user-images.githubusercontent.com/53170968/100876765-25bc7a00-34eb-11eb-8a7c-03d328359f7d.png)

19. 콘솔창을 열어서 난독화된 자바스크립트 코드를 전부 복사한다.

![image](https://user-images.githubusercontent.com/53170968/100876745-1f2e0280-34eb-11eb-8a41-b2a9ab199a8a.png)

20. 아까 찾은 점수에 해당하는 변수에 클리어 점수인 31337을 넣어주고 enter을 친다.

![image](https://user-images.githubusercontent.com/53170968/100876801-3c62d100-34eb-11eb-81ec-dd9a2f1cc3c9.png)

21. 게임을 시작하면 바로 클리어가 되어서 FLAG를 얻을 수 있었다.