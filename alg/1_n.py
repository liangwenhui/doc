# F(N) = 1!+2!+3!...+N!

# 1 + 1*2 + 1*2*3 + ... + 1*2*...*N

# N个1 + （n-1）2 + ... + N
# 


sum2 = 0
cur = 1

for i in list(range(1, N+1)) :
    cur = cur * i
    sum2 += cur
    print(sum2)

