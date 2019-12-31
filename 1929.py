M, N = map(int, input().split())
prime = [0 for _ in range(N+1)]
pn = 0
check = [True for _ in range(N+1)]

for i in range(2, N+1):
    if check[i] is True:
        prime[pn] = i
        pn += 1
        for j in range(i+i, N+1, i):
            check[j] = False

for i in range(M, N+1):
    if check[i] is True:
        print(prime[i])

MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] = True

for i in range(2, MAX+1):
    if not check[i]:
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i

m, n = map(int, input().split())
for i in range(m, n+1):
    if check[i] is False:
        print(i)