"""All prime numbers between given interval using functions."""
global p
def primeOfN(n,p):
    if(n==1):
        p=False
    else:
        for j in range(2,n):
            if(n%j==0):
                p=False
    return n,p



p=True
n=int(input("Enter the number:"))
print("List of Prime Numbers:")
for i in range(1,n+1):
    m,t=primeOfN(i,p)

    if (t == True):
        print(m)


