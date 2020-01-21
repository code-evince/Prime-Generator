'''Enter number of test cases in line 1 (eg. 1 or 2 or 10)
   Enter the range in which you need primes "seperated by a space" (eg. 1 1000000 )'''
import math
def prime(s,l):
    for j in range(s,l+1,1):
        if (j>1):
            for k in range(2,int(math.sqrt(j)+1)): #number theory theorm that states that for every composite number there exists atleast 1 prime factor that is less than its square root
                if (j%k==0):
                    break
            else:
                print(j)

#test cases and inputs
t = int(input())
for _ in range(t):
    s,l = map(int,input().split())
    prime(s,l)
    print()
