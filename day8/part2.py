with open("input.txt") as f:
    coords = [tuple([int(c) for c in coord.strip().split(',')]) for coord in f.readlines()]

distances = []
for i in range(len(coords)):
    for j in range(i+1, len(coords), 1):
        a1, b1, c1 = coords[i]
        a2, b2, c2 = coords[j]
        dist = ((a2-a1)**2+(b2-b1)**2+(c2-c1)**2)**0.5
        distances.append((dist, coords[i], coords[j]))
distances.sort(key=lambda x: x[0])

assigned_nodes = {}
circuit_index = 0
i = 0
while len(assigned_nodes) < len(coords) or len(set(assigned_nodes.values())) > 1:
    d1, d2 = distances[i][1:]
    circuit1 = assigned_nodes.get(d1, None)
    circuit2 = assigned_nodes.get(d2, None)
    if circuit1 and not circuit2:
        assigned_nodes[d2] = circuit1
    elif circuit2 and not circuit1:
        assigned_nodes[d1] = circuit2
    elif not circuit1 and not circuit2:
        assigned_nodes[d1] = circuit_index
        assigned_nodes[d2] = circuit_index
        circuit_index += 1
    elif circuit1 != circuit2:
        for n, c in assigned_nodes.items():
            if c == circuit2:
                assigned_nodes[n] = circuit1
    i += 1

print(d1[0]*d2[0])