import numpy as np

def load_mat(path):
    with open(path) as f:
        rows = f.read().strip().split('\n')
        rows = [list(r.replace('@','1').replace('.','0')) for r in rows]

    return np.matrix(rows).astype(int)

def get_removable_map(og_mat):
    horizontal_pad = np.zeros_like(og_mat[0])
    mat = np.vstack([horizontal_pad, og_mat, horizontal_pad])
    vertical_pad = np.zeros_like(mat[:,0])
    mat = np.hstack([vertical_pad, mat, vertical_pad])

    empty_mat = np.zeros_like(mat)

    path = [(1, 0), (1, 1), (-1, 0), (-1, 0), (-1, 1), (-1, 1), (1, 0), (1, 0)]
    for step, dir in path:
        mat = np.roll(mat, step, dir)
        empty_mat += mat
        
    empty_mat = empty_mat[1:-1,1:-1]
    res = ((og_mat != 0) & (empty_mat < 4)).astype(int)
    return res

if __name__ == "__main__":
    mat = load_mat('input.txt')
    print(np.sum(get_removable_map(mat)))
