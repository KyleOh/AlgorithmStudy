import sys; input = sys.stdin.readline
N = int(input())
T = [0 for _ in range(N)]; P = [0 for _ in range(N)]
X = [0 for _ in range(N+1)]
for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(1, N+1):
    