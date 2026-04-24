t=input("Enter text to encrypt:")
c=int(input("Ente key:"))
for i in t:
    if i.isupper():
        enc=chr((ord(i)-65+c)%26+65)
        print(enc,end="")
    elif i.islower():
        enc=chr((ord(i)-97+c)%26+97)
        print(enc,end="")
    else:
        print("Enter valid text")