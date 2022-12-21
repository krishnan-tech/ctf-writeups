Chall: Reversing ELF
URL: https://tryhackme.com/room/reverselfiles

---

## Task 1: Crackme1

Solution:

1. `chmod +x ./crackme1`
2. Run the file: `./crackme1`
   and boom, we will get the flag!!

Flag: `flag{not_that_kind_of_elf}`

---

## Task 2: Crackme2

Solution:

1. use this command in order to get strings in the program: `strings crackme2`
2. we will see the password in the output: `super_secret_password`
3. on running the chall, we will get the flag: `./crackme2 super_secret_password`

Flag: `flag{if_i_submit_this_flag_then_i_will_get_points}`

---

## Task 3: Crackme3

Solution:

1. use strings to get the string: `strings crackme3`
2. we will see there is some base64 strings in the output: `ZjByX3kwdXJfNWVjMG5kX2xlNTVvbl91bmJhc2U2NF80bGxfN2gzXzdoMW5nNQ==`
3. Decoding that string from cyberchef, we will get the flag

Flag: `f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5`

---

## Task 4: Crackme4

Solution:

1. we have to solve it using GDB: `gdb crackme4`
2. getting info of functions using and get the hex value for `strcmp@plt`: `0x0000000000400520  strcmp@plt`
3. make breakpoint from that value: `b *0x0000000000400520`
4. run the program: `r aaaa`
5. we will see the password string in `$rdi` register: `my_m0r3_secur3_pwd`

Flag: `my_m0r3_secur3_pwd`

---

## Task 5: Crackme5

Solution:

1. open the file with gdb: `gdb crackme5`
2. checked info and adding breakpoint to main: `b *main`
3. run the program using: `r`
4. use `ni` to check for next instruction and continue entering till it will ask for input.
5. Write input as `test`
6. continue `ni` and we will see `OfdlDSA|3tXb32~X3tX@sX`4tXtz`in the register section

Flag:`` OfdlDSA|3tXb32~X3tX@sX`4tXtz ``

---

## Task 6: Crackme6

Solution:

1. On running the binary, it has provided hint to analyze the binary, ghidra is the best software to do so. Therefore upload file to ghidra
2. Analyse mysecure test function

```

undefined8 my_secure_test(char *param_1)

{
  undefined8 uVar1;

  if ((*param_1 == '\0') || (*param_1 != '1')) {
    uVar1 = 4294967295;
  }
  else if ((param_1[1] == '\0') || (param_1[1] != '3')) {
    uVar1 = 0xffffffff;
  }
  else if ((param_1[2] == '\0') || (param_1[2] != '3')) {
    uVar1 = 0xffffffff;
  }
  else if ((param_1[3] == '\0') || (param_1[3] != '7')) {
    uVar1 = 0xffffffff;
  }
  else if ((param_1[4] == '\0') || (param_1[4] != '_')) {
    uVar1 = 0xffffffff;
  }
  else if ((param_1[5] == '\0') || (param_1[5] != 'p')) {
    uVar1 = 0xffffffff;
  }
  else if ((param_1[6] == '\0') || (param_1[6] != 'w')) {
    uVar1 = 0xffffffff;
  }
  else if ((param_1[7] == '\0') || (param_1[7] != 'd')) {
    uVar1 = 0xffffffff;
  }
  else if (param_1[8] == '\0') {
    uVar1 = 0;
  }
  else {
    uVar1 = 0xffffffff;
  }
  return uVar1;
}
```

3. From this function, we can clearly see the flag

Flag: `1337_pwd`

---

## Task 7: Crackme7

Solution:

1. Same as before, analyse main function in ghidra
2. In main function there is this bit of code:

```
else if (local_14 == 0x7a69) {
  puts("Wow such h4x0r!");
  giveFlag();
}
```

3. So, if value is 0x7a69 (31337), it will return flag

Flag: `flag{much_reversing_very_ida_wow}`

---

## Task 8: Crackme8

Solution:

1. Exactly as before, in ghidra analyse main function
2. In the code, it is showing if condition

```
if (iVar2 == -0x35010ff3) {
  puts("Access granted.");
  giveFlag();
  uVar1 = 0;
}
```

3. when we run the function with that decimal it will give flag: `/crackme8 -889262067`

Flag: `flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}`
