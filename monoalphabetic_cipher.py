txt="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher="MZNXBCVLAKSJDHFGPQOWIEURYT"
msg=str(input("Enter the message to encrypt  : "))
msg=msg.upper()

enc=""
for ch in msg:
    if ch==" ":
        enc+=" "
    else:
        index=txt.find(ch)
        enc+=cipher[index]
print("Encrypted message: ",enc)

dec=""
for ch in enc:
    if ch == " ":
        dec+= " "
    else:
        index=cipher.find(ch)
        dec+=txt[index]
print("Decrypted message: ",dec)