# The Message

### Problem
    One of our radars have detected a weak transmission coming from the direction of the Earth. I think I know what this is, but I'll let you handle it. That's fair play, right?
    
    --- -... -.- --.- .--. - . -.- ... - -.-. -.- ..- .... .-. --.- -.- ...-
    

### Solution
1. 문제를 보면 일단 기본적으로 모스부호인 것을 알 수 있다.
    일단 먼저 모스부호부터 복호화해보자
    
![morse](https://user-images.githubusercontent.com/53170968/92394572-bbe73b00-f15c-11ea-8f4c-c5a8e7fbbdf5.png)
    
2. 모스부호 복호화한 결과가 'OBKQPTEKSTCKUHRQKV'가 나온 것을 볼 수 있다.
    하지만 FLAG라고 하기엔 부족하다. 아마 암호화된 문장인 것 같다.

3. 문제를 다시 살펴보니 마지막에 어색한 문장이 있다. That's fair play, right?
    암호화 알고리즘 중에 Play Fair 알고리즘이 있다.
    이 암호화 알고리즘으로 한번 복호화 해보자
    복호화 사이트: <https://www.quinapalus.com/cgi-bin/playfair>
![breaker](https://user-images.githubusercontent.com/53170968/92395623-96f3c780-f15e-11ea-970c-10cbf6953ff7.png)

4. 나온 결과중에 FLAG라고 보일 만한 TEXT가 첫줄에 'helpussheiscommingx'인것 같다.
5. x가 FLAG에 포함되는지 안되는지 모르겠지만 둘다 입력해보자

![solution](https://user-images.githubusercontent.com/53170968/92396246-acb5bc80-f15f-11ea-8800-d1ff0a3ed859.png)

6. x를 제외한 문장이 답이었다.