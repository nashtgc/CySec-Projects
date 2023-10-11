
#Take each number mod 41
#find the modular inverse for the result. 
#Then map to the following character set: 
#1-26 are the alphabet, 27-36 are the decimal digits, 
#and 37 is an underscore.
#Wrap your decrypted message in the 
#picoCTF flag format (i.e. picoCTF{decrypted_message})


import string


alphabets = string.ascii_uppercase + string.digits + "_"
print(alphabets)

msg ="432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63"

words = msg.split(" ")
print(words)

result = "picoCTF{"


for word in words:
    module = int(word) % 41

    for i in range(41):
        if((module * i) % 41 == 1):
            result += alphabets[i-1]
            print(result)
            break
print(result + "}")




