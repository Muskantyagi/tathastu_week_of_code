n=int(input("enter a number"))
a=0;b=1;c=0
for i in range(n):
    c=a+b
    print(a,end="")
    a=b
    b=c
