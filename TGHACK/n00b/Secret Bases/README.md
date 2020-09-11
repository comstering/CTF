# Secret Bases

### Problem
    We managed to extract this secret information from one of Mother's 64 secret bases before we had to leave Earth. Are you able to decode it?
    
    VEcyMHt5b3VfY2FuX25ldmVyX2hhdmVfZW5vdWdoX3NlY3JldF9iYXNlc30=

### Solution
1. 문제 내용을 보면 어머니의 64개 비밀 기지((?) 번역기에서는 그렇게 번역함) 어쩌구 하는데
    CTF 문제 관점으로 봐서는 Base64 암호화 디코딩문제 같다.

2. Base64로 그냥 바로 디코딩해보자
![Base64](https://user-images.githubusercontent.com/53170968/92899008-6dd28000-f459-11ea-8b43-06ffaf625b74.png)


3. 키값은 내가 찾은게 아니라 이 암호화 툴에서 제공하는 키를 썼다. 
    심지어 기본 설정으로 되어있는 값이 저 값인데 FALG가 바로 떴다....

4. 바로 답을 넣어보자

![sol](https://user-images.githubusercontent.com/53170968/92899509-d4f03480-f459-11ea-924d-5ac1200ee76b.png)

5. 정답이다!!
    이 문제는 키값을 찾는 것에 많은 시간을 소모할 줄 알았는데 바로 FLAG가 나와버려서 당황했다.
    그래도 시간을 많이 소비하는 것보단 좋아서 행복^^