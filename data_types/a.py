s = input()
n = int(len(s))
list_of_even = [i for i in range(n)  if i%2==0]
list_of_odd = [x for x in range(n)  if x%2!=0]
def reverse_even_indexing():
    t = ""
    for i in list_of_even:
        t += s[i]
    return t[::-1]
print(s[2])
print(s[n-2])
print(s[0:5])
print(s[0:n-2])
for i in list_of_even:
    print(s[i],end="")
print()
for x in list_of_odd:
    print(s[x],end="")
print()
print(s[::-1])
print(reverse_even_indexing())
print(n)
