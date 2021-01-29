def solve():
    n = int(input())
    def prime_number(n):
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                return True
    if prime_number(n):
        print("prime")
    else:
        print("composite")
solve()