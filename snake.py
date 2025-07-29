import sys




def dfs_snake(node, snake, bitmask, current_length, size):
    max_len = current_length

    for i in range(size):
        if (bitmask[node] >> i) & 1:
            valid = True

            for j in snake:
                if j != node and bitmask[j] >> i & 1 and (node not in snake):
                    valid = False
                    break

            if valid:
                snake.add(i)
                max_len = max(max_len, dfs_snake(i, snake, bitmask, current_length+1, size))
                snake.remove(i)

    return max_len




def find_max_snake(size, bitmask):
    max_size = 0

    for i in range(size):
        node = i
        snake = {node}
        max_size = max(max_size, dfs_snake(node, snake, bitmask, 1, size))

    return max_size




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