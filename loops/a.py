n = int(input())
count = 1
temp = 1
while temp < n:
    temp = count*count
    count += 1 
    if temp > n:
        break
    print(temp)
