import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
crimeRate = list(map(int, input().split()))
mafia_state = [True] * N
R = [ list(map(int, input().split())) for _ in range(N) ]
eunjin = int(input())
night_cnt, game_end = 0, False
def get_mafia(remained, cur_night):
    global night_cnt, game_end
    if game_end: return

    night_cnt = max(night_cnt, cur_night)

    # 다 죽음
    if remained == 0: return
    # 은진만 생존
    if remained == 1 and mafia_state[eunjin]:
        game_end = True
        return

    # 밤
    if remained % 2 == 0:
        for checked_person in range(N):
            if not mafia_state[checked_person] or checked_person == eunjin:
                continue
            mafia_state[checked_person] = False

            for remained_person in range(N):
                if not mafia_state[remained_person]:
                    continue
                crimeRate[remained_person] += R[checked_person][remained_person]
            get_mafia(remained-1, cur_night+1)
            # 백트래킹
            for remained_person in range(N):
                if not mafia_state[remained_person]:
                    continue
                crimeRate[remained_person] -= R[checked_person][remained_person]
            mafia_state[checked_person] = True
    # 낮
    else:
        maxCrimeRate = checked_person = -1
        for i in range(N):
            if not mafia_state[i]:
                continue
            if maxCrimeRate < crimeRate[i]:
                checked_person, maxCrimeRate = i, crimeRate[i]
        if checked_person == eunjin:
            return
        mafia_state[checked_person] = False
        get_mafia(remained-1, cur_night)
        mafia_state[checked_person] = True
get_mafia(N, 0)
print(night_cnt)