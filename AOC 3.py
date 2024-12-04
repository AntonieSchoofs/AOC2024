input = open("c:/Users/anton/OneDrive/Documenten/AOC2024/input3.txt").read()

#print(input)

ans = 0

enabled = True

for i in range(len(input) - 1):
    element = input[i]
    if element == "(":
        do = input[i-2:i]
        dont = input[i-5:i]

        if do == "do":
            enabled = True
        elif dont == "don't":
            enabled = False

        mul = input[i-3:i]
        print(mul)
        if mul == "mul" and enabled:
            print("found mul:  " + input[i-3:i+9])
            
            if input[i+1:i+4].isnumeric() and input[i+4] == "," and input[i+5:i+8].isnumeric() and input[i+8] == ")": #3/3
                n1 = int(input[i+1:i+4])
                n2 = int(input[i+5:i+8])
                print("3/3 " + input[i+1:i+4] + " " + input[i+5:i+8] +"\n")
                ans += n1 * n2
            if input[i+1:i+3].isnumeric() and input[i+3] == "," and input[i+4:i+7].isnumeric() and input[i+7] == ")": #2/3
                n1 = int(input[i+1:i+3])
                n2 = int(input[i+4:i+7])
                print("2/3 " + input[i+1:i+3] + " " + input[i+4:i+7] +"\n")
                ans += n1 * n2
            if input[i+1].isnumeric() and input[i+2] == "," and input[i+3:i+6].isnumeric() and input[i+6] == ")": #1/3
                n1 = int(input[i+1])
                n2 = int(input[i+3:i+6])
                print("1/3 " + input[i+1] + " " + input[i+3:i+6] +"\n")
                ans += n1 * n2
            if input[i+1:i+4].isnumeric() and input[i+4] == "," and input[i+5:i+7].isnumeric() and input[i+7] == ")": #3/2
                n1 = int(input[i+1:i+4])
                n2 = int(input[i+5:i+7])
                print("3/2 " + input[i+1:i+4] + " " + input[i+5:i+7] +"\n")
                ans += n1 * n2
            if input[i+1:i+3].isnumeric() and input[i+3] == "," and input[i+4:i+6].isnumeric() and input[i+6] == ")": #2/2
                n1 = int(input[i+1:i+3])
                n2 = int(input[i+4:i+6])
                print("2/2 " + input[i+1:i+3] + " " + input[i+4:i+6] +"\n")
                ans += n1 * n2
            if input[i+1].isnumeric() and input[i+2] == "," and input[i+3:i+5].isnumeric() and input[i+5] == ")": #1/2
                n1 = int(input[i+1])
                n2 = int(input[i+3:i+5])
                print("1/2 " + input[i+1] + " " + input[i+3:i+5] +"\n")
                ans += n1 * n2
            if input[i+1:i+4].isnumeric() and input[i+4] == "," and input[i+5].isnumeric() and input[i+6] == ")": #3/1
                n1 = int(input[i+1:i+4])
                n2 = int(input[i+5])
                print("3/1 " + input[i+1:i+4] + " " + input[i+5] +"\n")
                ans += n1 * n2
            if input[i+1:i+3].isnumeric() and input[i+3] == "," and input[i+4].isnumeric() and input[i+5] == ")": #2/1
                n1 = int(input[i+1:i+3])
                n2 = int(input[i+4])
                print("2/1 " + input[i+1:i+3] + " " + input[i+4] +"\n")
                ans += n1 * n2
            if input[i+1].isnumeric() and input[i+2] == "," and input[i+3].isnumeric() and input[i+4] == ")": #1/1
                n1 = int(input[i+1])
                n2 = int(input[i+3])
                print("1/1 " + input[i+1] + " " + input[i+3] +"\n")
                ans += n1 * n2

print(ans)
