import sys

lines = sys.stdin.readlines()

i=0
while i < len(lines) - 1:
    cardinality = int(lines[i].strip())
    edges = 0

    for _ in range(cardinality):
        i += 1
        edges += len(lines[i].strip().split())

    i+= 1
    print(edges//2)

