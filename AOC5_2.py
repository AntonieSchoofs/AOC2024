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
    faults = 0
    prev_faults = 0
    new_faults = True
    
    #This while loop broke my brain
    while new_faults:
        for rule in rules:
            x = rule[0:2]
            y = rule[3:5]
            if x in update and y in update and update.find(x) > update.find(y):
                faults += 1
                correct_update = False
                index_x = update.find(x)
                index_y = update.find(y)
                #print(update)
                #print(rule)
                update = update[0:index_x] + y + update[index_x+2:]
                update = update[0:index_y] + x + update[index_y+2:]
                #print(update)
        
        if faults <= prev_faults:
            new_faults = False
        
        prev_faults = faults
    
    if not correct_update:
        #print(update[(len(update) - 1)//2:((len(update) - 1)//2)+2])
        ans += int(update[(len(update) - 1)//2:((len(update) - 1)//2)+2])

print(ans)
