def fib(num):
    a,b,c,=0,1,0
    count=2
    if num==0:
        print(1)
        return
    if num==1:
        print(2)
        return
    
    while c<=num:
       c=a+b
       a=b
       b=c
       count+=1
       if c==num:
          print("count=",count)
          break
    else:
       print(False)
num=int(input())
fib(num)
