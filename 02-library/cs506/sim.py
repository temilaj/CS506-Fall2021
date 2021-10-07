def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    result = 0

    for i in range(len(x)):
        result += abs(x[i] - y[i])
    return result

def jaccard_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0

    intersection_count = len(list(set(x).intersection(y)))
    union_count = (len(set(x)) + len(set(y))) - intersection_count
    result = 0 if union_count == 0 else (intersection_count/union_count)
    return result

def norm(x):
    result = sum( [x[i]**2 for i in range(len(x))] )
    return result**(1/2)

def cosine(x,y):
    result = 0
    try:
        result = (x @ y )/ (norm(x) * norm(y))
        return result
    except:
        return result

def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0
    if len(x) != len(y):
        return -1

    return 1 - cosine(x,y)

# Feel free to add more