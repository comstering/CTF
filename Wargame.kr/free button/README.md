# free button

### Problem

![image](https://user-images.githubusercontent.com/53170968/100539515-76796c00-327a-11eb-8c9a-0fddfd4a03b9.png)

### Solution
1. 문제가 버튼을 클릭해라이다. 버튼을 잡지 못한다고 한다.

2. 일단 Start를 눌러 문제로 가자.

![image](https://user-images.githubusercontent.com/53170968/100539535-90b34a00-327a-11eb-8852-457d9b49bc79.png)

3. 이 화면에서 저 'click me!'를 클릭하면 되는데 마우스를 움직이면 저 'click me!'가 마우스를 피해서 계속 움직인다.

4. 즉 마우스를 이용해서는 저 'click me!'를 클릭할 수 없다는 뜻이다.

5. 역시나 F12를 눌러 개발자모드로 이동하자.

![image](https://user-images.githubusercontent.com/53170968/100539543-9ad54880-327a-11eb-9986-f355765d6351.png)

6. 개발자모드에서 Elements로 이동하여 화면에 대한 html 코드를 확인해보자.

![image](https://user-images.githubusercontent.com/53170968/100539550-a294ed00-327a-11eb-8615-ce9b2b743884.png)

7. 마우스로 html의 코드에 가져다 놓으면 코드에 해당하는 구성을 표시해 준다.

![image](https://user-images.githubusercontent.com/53170968/100539567-c3f5d900-327a-11eb-9703-a4eb1ef596fe.png)

8. 즉 저 input 태그에 해당하는 값이 'click me!'에 해당하는 내용인 것이다.

9. input 태그 안의 내용을 확인해 보면 해당 버튼을 클릭할 경우 [window.location='?key=ad13']이 코드가 실행이 된다.

![image](https://user-images.githubusercontent.com/53170968/100539574-d53ee580-327a-11eb-9f66-6768ff349119.png)

10. 저 코드는 화면은 전환하는데 현재의 url 뒤에 request 값으로 key=ad13을 넣어 화면을 바꾼다는 뜻이다.

11. 그렇다면 지금의 url 뒤에 저 값을 그대로 집어 넣으면 'click me!'를 클릭한 결과와 동일한 결과를 얻을 수 있다.

![image](https://user-images.githubusercontent.com/53170968/100539625-2222bc00-327b-11eb-87a6-964c0559c1f9.png)


12. url을 변경해서 다시 접속한 결과 FLAG를 얻을 수 있었다.

![image](https://user-images.githubusercontent.com/53170968/100539635-28b13380-327b-11eb-8d06-0ba598cb6a60.png)

13. 이 문제는 html코드를 작성해본 사람이라면 금방 풀 수 있을 것 같다.
