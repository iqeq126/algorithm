import sys
input = sys.stdin.readline
N, K = map(int, input().split()) # N : 동전 개수, K : 가격합
_list = [] # 저금통
for i in range(N): # 동전 넣기
    t = int(input())
    _list.append(t)
DP = [ 0 for i in range(K+1)] # 가격합의 경우의 수
DP[0] = 1 # 초기값 설정
# 1부터 하는 이유? 그렇게 하지 않으면 더하다가 오차가 생길 수 있음
# ex) 1,2,5일 때 10을 만드는 경우. 0~9까지를 초기화한다면 
# 5로 10을 만드는 경우같이 배수를 처리하기 까다로워짐
for i in range(1, N+1): # 1 ~ N
    for j in range(_list[i-1], K+1): # 가장 작은 동전 ~ K
        DP[j] += DP[j - _list[i-1]] # 가진 동전을 빼나가면서 해당하는 동전을 더해줌

print(DP[K])