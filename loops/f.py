x = int(input())
y = int(input())
cnt = 1
while x <= y:
    x = x + (x/10)
    cnt += 1 
print(cnt)