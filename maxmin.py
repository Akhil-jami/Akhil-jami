#print max and min
n=int(input("Enter Number: "))
mi=9
ma=0
while n:
    r=n%10
    n=n//10
    if r>ma:
        ma=r
    if r<mi:
        mi=r
print(mi,ma)


