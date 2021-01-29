s = input()
list_of_appearances = []
counter_of_iteration = 0
for i in s:
    if i == "h":
        list_of_appearances.append(counter_of_iteration)
    counter_of_iteration += 1
list_of_appearances[-1]+=1
s_delete = s[list_of_appearances[0]:list_of_appearances[len(list_of_appearances)-1]]
s = s.replace(s_delete,"")
print(s)
