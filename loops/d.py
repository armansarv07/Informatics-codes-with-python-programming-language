n = int(input())
def check_two(a):
    if a % 2 == 0:
        return True
    else:
        return False
while n > 0:
    if check_two(n):
        n = n/2
    elif n==1:
        print("YES")
        break
    elif not(check_two(n)):
        print("NO")
        break

