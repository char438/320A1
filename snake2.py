import sys


def dfs_bitmask(cur_node, visited, bitmask, size):
    max_len = 0
    for next_node in range(size):
        if not (bitmask[cur_node] & (1 << next_node)):
            continue

        if visited & (1 << next_node):
            continue

        visited_alternate = visited & ~(1 << cur_node)
        if bitmask[next_node] & visited_alternate:
            continue
        

        new_visited = visited | (1 << next_node)
        possible_path = 1 + dfs_bitmask(next_node, new_visited, bitmask, size)
        if possible_path > max_len:
            max_len = possible_path

    return max_len


def find_max_snake(size, bitmask):
    max_path = 0

    for node in range(size):
        visited = 1 << node
        max_path = max(max_path, dfs_bitmask(node, visited, bitmask, size))
    
    return max_path


def main():
    lines = sys.stdin.readlines()

    i = 0
    while i < len(lines) - 1:
        size = int(lines[i].strip())
        bitmask = [0] * size

        for j in range(size):
            i += 1
            for node in lines[i].split():
                bitmask[j] |= 1 << int(node)

        print(find_max_snake(size, bitmask))
        i += 1



main()