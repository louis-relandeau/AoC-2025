with open('input.txt') as f:
    rows = [r.strip() for r in f]

raw_row = [0]*len(rows[0])

beams = raw_row.copy() # way 1
beams[rows[0].index('S')] = 1
for row in rows[1:]:
    new_beams = raw_row.copy()
    for i in range(len(rows[0])):
        if row[i] == '^' and beams[i] > 0:
            new_beams[i+1] = beams[i]
            new_beams[i-1] = beams[i] + new_beams[i-1]
        elif beams[i] > 0:
            new_beams[i] = beams[i] + new_beams[i]
    beams = new_beams
print(sum(new_beams))

beams = raw_row.copy() # way 2
beams[rows[0].index('S')] = 1
for row in rows[1:]:
    for i in reversed(range(len(rows[0]))):
        if row[i] == '^' and beams[i] > 0:
            beams[i-1] += beams[i]
            beams[i+1] += beams[i]
            beams[i] = 0
print(sum(beams))