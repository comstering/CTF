# welcome

### Problem
    #include <stdio.h>
    
    int main(void) {
        
        FILE *fp;
        char buf[0x80] = {};
        size_t flag_len = 0;
    
        printf("Welcome To DreamHack Wargame!\n");
    
        fp = fopen("/flag", "r");
        fseek(fp, 0, SEEK_END);
        flag_len = ftell(fp);
        fseek(fp, 0, SEEK_SET);
        fread(buf, 1, flag_len, fp);
        fclose(fp);
    
        printf("FLAG : ");
    
        fwrite(buf, 1, flag_len, stdout);
    }

### Solution
1. 소스코드를 보면 프로그램을 실행하자마자 'Welcome To Dreamhack Wargame!'가 출력된다.

2. 그리고 FileOpen을 통해서 flag파일을 읽어온다.

3. 그리고 해당 파일의 내용을 출력하고 종료된다.

4. 내용은 정말 간단하다. 그냥 프로그램만 실행하면 flag를 읽어와서 출려해준다.

5. 우리 로컬에는 flag파일이 없으므로 DreamHack 네트워크에 접속해서 얻어보자.

![image](https://user-images.githubusercontent.com/53170968/112411396-31fd6900-8d60-11eb-8a3f-e8961f0c3a74.png)

6. DreamHack사이트에서 접속정보를 먼저 얻자.

![image](https://user-images.githubusercontent.com/53170968/112411444-4477a280-8d60-11eb-853e-925d354585ea.png)


7. 그리고 해당 접속정보에 해당하는 네트워크에 접속한다. nc 명령어를 사용하는데 nc는 network connectf로 네트워크로 원격 호스트에 접속하게 해주는 명령어라고 생각하면 된다.

![image](https://user-images.githubusercontent.com/53170968/112411535-6d983300-8d60-11eb-95f5-1396abf467e1.png)

8. 접속했더니 그냥 바로 FLAG를 출력해준다.

9. 이 문제는 앞으로 DreamHack Wargame을 어떻게 풀어야하는지 시작을 알려주는 문제였다.

10. DreamHack Wargame 모든 문제들이 다 이렇게 DreamHack 호스트에 접속해서 문제를 풀고 FLAG를 얻어야한다.

![image](https://user-images.githubusercontent.com/53170968/112411691-ab955700-8d60-11eb-863d-47bbe00230dc.png)

![image](https://user-images.githubusercontent.com/53170968/112411715-b5b75580-8d60-11eb-81cd-5773c81e976c.png)

11. 이렇게 원격호스트에서 얻은 FLAG를 사이트에 입력해서 제출한다.

12. 앞으로의 DreamHack 문제풀이 가장 기본을 알 수 있는 문제였다.