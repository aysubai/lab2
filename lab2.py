n=int(input())
a=[0]*n
k=0
s=0
from random import randint
for i in range(n):
    a[i]=int(input())
print('A:', a)
for x in  a:
    if x<0:
        s=s+x
print(s)
