with open("input.txt") as f:
    tiles = [tuple([int(t) for t in tile.strip().split(',')]) for tile in f.readlines()]

max_area = 0
for i in range(len(tiles)):
    for j in range(i+1, len(tiles), 1):
        a1, b1 = tiles[i]
        a2, b2 = tiles[j]
        area = (abs(a2-a1)+1)*(abs(b2-b1)+1)
        max_area = max(area, max_area)
print(max_area)