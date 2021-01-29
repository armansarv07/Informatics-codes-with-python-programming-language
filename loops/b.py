def solve():
    n = int(input())
    divisors = []
    for i in range(2,n):
        if n % i == 0:
            divisors.append(i)
    print(divisors[0])
solve()