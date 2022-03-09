num=int(input("Enter a number:"))
a=-1
b=1
fibo=0
for i in range(0,num):
    fibo=a+b
    a=b
    b=fibo
    print(fibo)
