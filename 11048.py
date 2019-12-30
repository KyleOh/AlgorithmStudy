import sys; input = sys.stdin.readline
N, M = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(N)]
D = [[0 for _ in range(M+1)] for _ in range(N+1)]; D[1][1] = A[0][0]

for i in range(1, N+1):
    for j in range(1, M+1):
        D[i][j] = max(D[i-1][j], D[i][j-1], D[i-1][j-1]) + A[i-1][j-1]
print(D[N][M])
