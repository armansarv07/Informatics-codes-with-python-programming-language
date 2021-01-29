s = input()
n_first = int((len(s)/2)+(len(s)%2))
first_half = s[0:n_first]
second_half = s[n_first:]
print(second_half,end="")
print(first_half)
