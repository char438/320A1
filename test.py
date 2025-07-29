import sys

def dfs(u, visited_mask, bitmask, n):
    """
    Return the max #edges of an induced path that
    starts at u with 'visited_mask' already used.
    """
    best = 0
    for v in range(n):
        # 1) v is a neighbor of u?
        if not (bitmask[u] & (1 << v)):
            continue

        # 2) v not already visited?
        if visited_mask & (1 << v):
            continue

        # 3) induced condition:
        #    (bitmask[v] & (visited_mask_without_u)) must be zero.
        mask_without_u = visited_mask & ~(1 << u)
        if bitmask[v] & mask_without_u:
            continue

        # we can safely extend u → v
        cand = 1 + dfs(v, visited_mask | (1 << v), bitmask, n)
        if cand > best:
            best = cand

    return best


def find_max_induced_path_edges(n, bitmask):
    best = 0
    for start in range(n):
        # start with just 'start' in the mask
        length = dfs(start, 1 << start, bitmask, n)
        if length > best:
            best = length
    return best


def main():
    data = [line.strip() for line in sys.stdin if line.strip() != ""]
    i = 0
    while i < len(data):
        n = int(data[i]);  i += 1
        bitmask = [0]*n
        for u in range(n):
            for token in data[i].split():
                v = int(token)
                bitmask[u] |= 1 << v
            i += 1

        # print the number of edges in the longest induced path
        print(find_max_induced_path_edges(n, bitmask))


if __name__ == "__main__":
    main()