def solve():
    n = int(input())
    def Fibbonacci(n):
        if n==0:
            return 1
        if n==1:
            return 1
        return Fibbonacci(n-1) + Fibbonacci(n-2)
    print(Fibbonacci(n))
solve()