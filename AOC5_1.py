lines = open("c:/Users/anton/OneDrive/Documenten/AOC2024/input5.txt").readlines()

rules = []
updates = []

ans = 0

for line in lines:
    if "|" in line:
        rules.append(line.strip("\n"))
    elif "," in line:
        updates.append(line.strip("\n"))

for update in updates:
    correct_update = True
    for rule in rules:
        x = rule[0:2]
        y = rule[3:5]
        if x in update and y in update and update.find(x) > update.find(y):
            correct_update = False
    
    if correct_update:
        #print(update[(len(update) - 1)//2:((len(update) - 1)//2)+2])
        ans += int(update[(len(update) - 1)//2:((len(update) - 1)//2)+2])

print(ans)
