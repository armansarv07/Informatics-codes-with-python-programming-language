def solve():
    n,k = map(int,input().split())
    def Binomial(n,k):
        if n == n and k == 0:
            return 1
        if n == k:
            return 1
        return Binomial(n-1,k-1)+Binomial(n-1,k)
    print(Binomial(n,k))
solve()