def solve():
    cnt = 0
    n = int(input())
    for i in range(n):
        for x in range(i):
            print(i,end=" ")
            cnt += 1
        if cnt == n:
            break
solve()