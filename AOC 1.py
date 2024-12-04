lines = open("c:/Users/anton/OneDrive/Documenten/AOC2024/input.txt", "r").readlines()

list1 = []
list2 = []


for line in lines:
    split = line.split(" ")
    list1.append(int(split[0]))
    list2.append(int(split[3]))

print(len(list1))
print(len(list2))
list1.sort()
list2.sort()

list_distances = []

for i in range(len(list1)):
    n = list1[i]
    amount = 0
    for m in list2:
        if n == m:
            amount += 1
    
    list_distances.append(n * amount)


print(sum(list_distances))
