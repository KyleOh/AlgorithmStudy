import itertools; import sys; input = sys.stdin.readline

t = int(input())
for _ in range(t):
    A = []; A.append(list(int(x) for x in input().split())[1:]); sum = 0
    for i, j in list(itertools.combinations([i for i in range(A[0]))], 2)):
        sum += gcd(A[0][i], A[0][j])
    print(sum)