with open("input.txt") as f:
    tiles = [tuple([int(t) for t in tile.strip().split(',')]) for tile in f.readlines()]

all_areas = []
for i in range(len(tiles)):
    for j in range(i+1, len(tiles), 1):
        a1, b1 = tiles[i]
        a2, b2 = tiles[j]
        area = (abs(a2-a1)+1)*(abs(b2-b1)+1)
        all_areas.append((area, tiles[i], tiles[j]))

all_areas.sort(key=lambda x: x[0], reverse=True)

tiles.append(tiles[0]) # wrap around
for largest_area, t1, t2 in all_areas:
    good_color = True
    for n in range(len(tiles)-1):
        xs = sorted([t1[0], t2[0]])
        ys = sorted([t1[1], t2[1]])
        # tile n strictly in area
        c1 = (xs[0] < tiles[n][0] < xs[1] and ys[0] < tiles[n][1] < ys[1])
        # tile n+1 strictly in area
        c2 = (xs[0] < tiles[n+1][0] < xs[1] and ys[0] < tiles[n+1][1] < ys[1])
        # if not in area, either x or y must be on the same side
        c3 = (tiles[n][0] <= xs[0] and tiles[n+1][0] <= xs[0]) or (tiles[n][0] >= xs[1] and tiles[n+1][0] >= xs[1])
        c4 = (tiles[n][1] <= ys[0] and tiles[n+1][1] <= ys[0]) or (tiles[n][1] >= ys[1] and tiles[n+1][1] >= ys[1])
        if (c1 != c2) or (not c1 and not c2 and not (c3 or c4)):
            good_color = False
            break

    if good_color:
        print(largest_area)
        exit()