lines = open("c:/Users/anton/OneDrive/Documenten/AOC2024/input4.txt").readlines()

matrix = []

for line in lines:
    line = line.strip("\n")
    matrix.append(line)

ans = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "A" and i-1 >= 0 and i+1 < len(matrix) and j-1 >= 0 and j+1 < len(matrix[i]):
            # MM UP
            if matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "S":
                ans += 1
            # MM DOWN
            if matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "M" and matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "S":
                ans += 1
            # MM RIGHT
            if matrix[i-1][j+1] == "M" and matrix[i+1][j+1] == "M" and matrix[i-1][j-1] == "S" and matrix[i+1][j-1] == "S":
                ans += 1
            # MM LEFT
            if matrix[i-1][j-1] == "M" and matrix[i+1][j-1] == "M" and matrix[i-1][j+1] == "S" and matrix[i+1][j+1] == "S":
                ans += 1

print(ans)
