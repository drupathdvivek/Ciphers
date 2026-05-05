txt=str(input("Enter the message to encrypt :"))
key=str(input("Enter the key (Text) : "))
key=key.upper()
txt=txt.upper()

cipher=""
j=0
for i in range(len(txt)):
    if txt[i].isalpha():
        shift=ord(key[j%len(key)])-65
        enc=chr((ord(txt[i])-65+shift)%26+65)
        cipher+=enc
        j+=1
    else:
        cipher+=txt[i]
print("Encrypted text : ",cipher)