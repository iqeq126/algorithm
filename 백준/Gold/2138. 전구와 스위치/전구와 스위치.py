import sys, copy
input = sys.stdin.readline
# 0 : HIGH, 1 : LOW
n = int(input())
cur_state = list(map(bool, map(int, input().rstrip())))
copied_cur_state = copy.deepcopy(cur_state)
res_state = list(map(bool, map(int, input().rstrip())))

def bulb_switch(bulb, state, max_size=n):
    for i in range(state, state+3):
        if i >= max_size: continue
        bulb[i] = not bulb[i]
    return bulb

def switch_times(cur_state, res_state, max_size=n, cnt = 0):
    for i in range(max_size-1):
        if cur_state[i] != res_state[i]:
            cur_state = bulb_switch(cur_state, i, max_size)
            cnt+=1
    return (cnt, cur_state)

# 0번째 스위치를 누르는 경우
result = sys.maxsize
# 0, 1 switch 연산
cur_state[0], cur_state[1] = not cur_state[0], not cur_state[1]
res, cur_state = switch_times(cur_state, res_state)
if cur_state == res_state: result = min(res+1, result)

# 0번째 스위치를 누르지 않는 경우
res, cur_state = switch_times(copied_cur_state, res_state)
if cur_state == res_state: result = min(res, result)
print(-1) if result == sys.maxsize else print(result)