def sumofdigits(n,data):

    def digits(i):
        d=0
        while i:
            r=i%10
            i=i//10
            d+=r
        return d
    c=[]           
    for i in data:
        c.append(digits(i))
    return c
n=int(input())
data=list(map(int,input().split()))
sod=sumofdigits(n,data)
print(*sod)
