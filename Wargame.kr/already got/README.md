# alreay got

### Problem

![image](https://user-images.githubusercontent.com/53170968/100538836-6f9c2a80-3275-11eb-9ddc-8d5a682d514c.png)


### Solution
1. 가장 기본적인 웹해킹 CTF이다.

2. 일단 Start를 눌러 문제로 가자.

![image](https://user-images.githubusercontent.com/53170968/100538842-7a56bf80-3275-11eb-8529-db624957087a.png)

3. 문제에 해당하는 웹사이트로 왔다. 웹사이트에 내가 이미 키를 가지고 있다고 한다.

4. 웹해킹에서 가장 기본적인 F12키를 눌러서 개발자 모드로 들어가 웹사이트 내부 구성을 확인하자.

![image](https://user-images.githubusercontent.com/53170968/100538848-8478be00-3275-11eb-98ba-3ec8519a6727.png)

5. 웹사이트의 내용에는 별다른 내용이 없는 것 같다. 문제 처음으로 돌아가서 처음 문제가 머였는지 생각해보자.

![image](https://user-images.githubusercontent.com/53170968/100538836-6f9c2a80-3275-11eb-9ddc-8d5a682d514c.png)

6. 문제가 HTTP Response header를 확인할 수 있는지 물어본다.

7. HTTP Resonse header란?

8. 내용이 길어서 짧게 설명하면 우리가 서버에 웹사이트 정보를 달라고 요청을 해야 서버에서 응답으로 정보를 준다.

9. 여기서 요청이 Request, 응답이 Response이다.

10. 요청과 응답에는 각각의 정보 내용을 담고 있는 body와 요약 정보 및 필수 정보가 있는 header가 있다.

11. 이 문제는 저 header 정보를 확인하여 FLAG를 얻는 것이다. 

12. 개발자 모드에서 network 카테고리로 이동한다.

![image](https://user-images.githubusercontent.com/53170968/100538857-95c1ca80-3275-11eb-9ac5-53bfcfc236e2.png)

13. 처음에는 아무것도 보이지 않지만 F5키를 눌러서 새로고침을 하면 현재 보이는 화면에 해당하는 파일을 받아왔다는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/100538860-9bb7ab80-3275-11eb-8115-61169ef6f506.png)


14. 해당파일을 클릭하면 Response에 우리가 보고 있는 화면을 받아온 것을 볼 수 있다.
![image](https://user-images.githubusercontent.com/53170968/100538869-a5411380-3275-11eb-8bfb-ee4538d2e8c9.png)

15. Headers 목록으로 옮기면 Request, Response header 정보를 확인할 수 있다.

![image](https://user-images.githubusercontent.com/53170968/100538872-ad00b800-3275-11eb-96dd-b63553ebea35.png)

16. 우리가 확인해야 할거는 Response Header의 정보로 Response Header에는 다음과 같이 FLAG라는 명목으로 값이 있는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/53170968/100538876-b4c05c80-3275-11eb-9805-d2f129773e18.png)

17. 가장 기본적인 웹해킹의 시작이라고 볼 수 있다.