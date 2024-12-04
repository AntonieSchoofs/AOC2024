lines = open("c:/Users/anton/OneDrive/Documenten/AOC2024/input4.txt").readlines()

matrix = []

for line in lines:
    line = line.strip("\n")
    matrix.append(line)

ans = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "X":
            #Right
            if j+3 < len(matrix[i]) and matrix[i][j+1] == "M" and matrix[i][j+2] == "A" and matrix[i][j+3] == "S":
                ans += 1
            #Left
            if j-3 >= 0 and matrix[i][j-1] == "M" and matrix[i][j-2] == "A" and matrix[i][j-3] == "S":
                ans += 1
            #Up
            if i-3 >= 0 and matrix[i-1][j] == "M" and matrix[i-2][j] == "A" and matrix[i-3][j] == "S":
                ans += 1
            #Down
            if i+3 < len(matrix) and matrix[i+1][j] == "M" and matrix[i+2][j] == "A" and matrix[i+3][j] == "S":
                ans += 1
            #Diag R/U
            if i-3 >= 0 and j+3 < len(matrix[i]) and matrix[i-1][j+1] == "M" and matrix[i-2][j+2] == "A" and matrix[i-3][j+3] == "S":
                ans += 1
            #Diag R/D
            if i+3 < len(matrix) and j+3 < len(matrix[i]) and matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S":
                ans += 1
            #Diag L/U
            if i-3 >= 0 and j-3 >= 0 and matrix[i-1][j-1] == "M" and matrix[i-2][j-2] == "A" and matrix[i-3][j-3] == "S":
                ans += 1
            #Diag L/D
            if i+3 < len(matrix) and j-3 >= 0 and matrix[i+1][j-1] == "M" and matrix[i+2][j-2] == "A" and matrix[i+3][j-3] == "S":
                ans += 1
            

print(ans)
