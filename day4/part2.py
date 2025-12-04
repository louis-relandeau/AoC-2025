import numpy as np

from part1 import load_mat, get_removable_map

mat = load_mat('input.txt')

count = 0
while True:
    removable_map = get_removable_map(mat)
    removable_count = np.sum(removable_map)
    if removable_count == 0:
        break

    count += removable_count
    mat -= removable_map

print(count)