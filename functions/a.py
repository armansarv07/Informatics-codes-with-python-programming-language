from math import*
def solve():
    a,b,c,d = map(int,input().split())
    def mini(a,b,c,d):
        return min(min(a,b),min(c,d))
    print(mini(a,b,c,d))
solve()