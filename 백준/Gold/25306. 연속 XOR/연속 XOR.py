a, b = map(int, input().split())
res_a, res_b = [a, 1, a+1, 0], [b,1,b+1,0]
print( a ^ res_a[ a % 4 ] ^ res_b[ b % 4 ] )