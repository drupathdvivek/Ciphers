t=input("Enter text to encrypt: ")
k=input("Enter key: ")
keyind=0
for i in t:
    if i.isalpha():
        c=ord(k[keyind% len(k)].lower())-97
        if i.isupper():
            enc= chr((ord(i)-65+c)%26+65)
            print(enc,end="")
        else:
            enc= chr((ord(i)-97+c)%26+97)
            print(enc,end="")
        keyind +=1