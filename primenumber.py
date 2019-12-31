# Version 1
def isPrime(n):
    if n <= 1:
        return False
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True


N = int(input())
print(isPrime(N))

# Version 2
import math

def isPrime2(n):
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

N = int(input())
print(isPrime2(N))


# Version 3
def isPrime3(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(isPrime3(N))

# Version 4 - Sieve of Eratosthenes
N = int(input())
A = range(2, N+1)

prime = [0 for _ in range(1001)]
pn = 0
check = [True for _ in range(1001)] # 소수가 맞으면 True, 아니면 False
n = 1000
for i in range(2, n+1):
    if check[i] is True:
        prime[pn] = i
        pn += 1
        for j in range(i+i, n+1, i):
            check[j] = False
print(prime[:pn])