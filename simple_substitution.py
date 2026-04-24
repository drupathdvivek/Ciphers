a="abcdefghijklmnopqrstuvwxyz"
x="bcdefghijklmnopqrstuvwxyza"
m=input("Enter the message:")
c=""

for i in m:
    if i in a:
        d=a.index(i)
        c=c+x[d]
    else:
        c=c+i
print("Encrypted message: ",c)