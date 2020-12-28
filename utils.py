def unique_vals(rows, col):
    return set([row[col] for row in rows])
def nb_counts(X, y):
    counts = {} 
    for i in range(len(X)):
        target = y[i]
        if target not in counts:
            counts[target] = 0
        counts[target] += 1
    return counts
def check_numeric(value):
    return isinstance(value, int) or isinstance(value, float)