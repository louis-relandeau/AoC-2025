with open('input.txt') as f:
    rows = [r.strip() for r in f]

beams = set([rows[0].index('S')])

row_size = len(rows[0])
split_count = 0
for row in rows[1:]:
    new_beams = set()
    for i in range(row_size):
        if row[i] == '^' and i in beams:
            split_count += 1
            new_beams.add(i-1) # no bounds issue, splitter never on edge
            new_beams.add(i+1)
        elif i in beams:
            new_beams.add(i)
    beams = new_beams

print(split_count)