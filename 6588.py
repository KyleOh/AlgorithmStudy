import sys; input = sys.stdin.readline
MAX = 1000000
prime = [0]*(MAX+1)
check = [False]*(MAX+1)
pn = 0

for i in range(2, MAX+1):
    if not check[i]:
        prime[pn] = i
        pn += 1
        for j in range(i+i, MAX+1, i):
            if j % i == 0:
                check[j] = True

def prove(n):
    for i in prime:
        if i >= n: break
        if check[n-i] is False:
            return i, n-i


x = int(input())
while x != 0:
    a, b = prove(x)
    msg = "{} = {} + {}\n".format(x, a, b)
    sys.stdout.write(msg)
    #print("{} = {} + {}".format(x, a, b))
    x = int(input())