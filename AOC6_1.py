lines = open("C:\\Users\\Antonie\\Documents\\AOC\\AOC2024\\input6.txt").readlines()

maze = []

def check_guard_outofbounds(maze):
    for line in maze:
        if ">" in line or "<" in line or "^" in line or "v" in line:
            return False
    return True

def check_amount_X(maze):
    ans = 0
    for line in maze:
        for elem in line:
            if elem == "X":
                ans += 1
    return ans

for line in lines:
    line.strip("\n")
    line_elems = []
    for elem in line:
        line_elems.append(elem)
    maze.append(line_elems)

#print(maze)

while not check_guard_outofbounds(maze):
    for line in maze:
        if '>' in line:
            index_guard_x = line.index('>')
            index_guard_y = maze.index(line)
            if not index_guard_x == len(line) - 1:
                next_index = index_guard_x + 1
                if not line[next_index] == '#':
                    line[next_index] = ">"
                elif index_guard_y != len(maze) - 1:
                    maze[index_guard_y + 1][index_guard_x] = "v"
            line[index_guard_x] = 'X'
        
        if '<' in line:
            index_guard_x = line.index('<')
            index_guard_y = maze.index(line)
            if not index_guard_x == 0:
                next_index = index_guard_x - 1
                if not line[next_index] == '#':
                    line[next_index] = "<"
                elif index_guard_y != 0:
                    maze[index_guard_y - 1][index_guard_x] = "^"
            line[index_guard_x] = 'X'

        if '^' in line:
            index_guard_x = line.index('^')
            index_guard_y = maze.index(line)
            if not index_guard_y == 0:
                next_index = index_guard_y - 1
                if not maze[next_index][index_guard_x] == '#':
                    maze[next_index][index_guard_x] = "^"
                elif index_guard_x != len(line) - 1:
                    maze[index_guard_y][index_guard_x + 1] = ">"
            line[index_guard_x] = 'X'

        if 'v' in line:
            index_guard_x = line.index('v')
            index_guard_y = maze.index(line)
            if not index_guard_y == len(maze) - 1:
                next_index = index_guard_y + 1
                if not maze[next_index][index_guard_x] == '#':
                    maze[next_index][index_guard_x] = "v"
                elif index_guard_x != 0:
                    maze[index_guard_y][index_guard_x - 1] = "<"
            line[index_guard_x] = 'X'


#print(maze)

print(check_amount_X(maze))