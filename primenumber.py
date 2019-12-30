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
