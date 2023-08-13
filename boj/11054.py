import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
R_A = A[::-1]
p_list = [1] * N
m_list = [1] * N
result = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            p_list[i] = max(p_list[i], p_list[j]+1)
        if R_A[i] > R_A[j]:
            m_list[i] = max(m_list[i], m_list[j]+1)
for i in range(N):
    result[i] = p_list[i] + m_list[N - i- 1] - 1
print(max(result))