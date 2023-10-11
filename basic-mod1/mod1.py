set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

msg ="128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"

msg = msg.split(" ")

flag = "picoCTF{"

for num in msg:
    mod = int(num) % 37
    #print(mod)
    flag += set[mod]

print(flag + "}" )

