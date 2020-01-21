'''Enter number of test cases in line 1 (eg. 1 or 2 or 10)
   Enter the range in which you need primes "seperated by a space" (eg. 1 1000000 )'''
#taking inputs and test cases
for _ in range(int(input())):
    m,n = map(int,input().split())

#the code
    primes = {}
    for i in range(2,round(n**0.5)+1):
        for j in range(max(m//i,2),(n//i)+1):
            primes[i*j] = 1
    for i in range(max(m,2),n+1):
        if i not in primes:
            print(i)
    print()
# this code marks primes as 1 and composite as 0 in dictionary by using sieve of eratosthenes
