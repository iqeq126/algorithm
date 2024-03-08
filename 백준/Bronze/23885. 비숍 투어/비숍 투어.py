N, M = map(int,input().split())
sx, ex = map(int,input().split())
sy, ey = map(int,input().split())
if N == 1 or M == 1:
    print("YES") if sx==sy and ex==ey else print("NO")
elif (sx+ex)%2==0:
    print("YES") if (sy+ey)%2==0 else print("NO")
else:
    print("NO") if (sy+ey)%2==0 else print("YES")