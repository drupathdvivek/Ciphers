a="abcdefghijklmnopqrstuvwxyz"
x="bcdefghijklmnopqrstuvwxyza"
m=input("Enter the message:")
enc=""
for i in m:
    if i in a:
        d=a.index(i)
        enc=enc+x[d]
    else:
        enc=enc+i
print("Encrypted message: ",enc)
