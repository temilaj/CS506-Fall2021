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
    intersection_count = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            intersection_count += 1

    union_count = len(x) + len(y) - intersection_count
    
    result = 0
    try:
        result = intersection_count/union_count
        return result
    except:
        return result


def transpose(matrix):
    return list(map(list, zip(*matrix)))

def norm(x):
    result = 0
    for i in range(len(x)):
        result += x[i]**2
    return result**(1/2)

def multiply(x,y):
    result = 0
    for i in range(len(x)):
        result += x[i]* y[i]
    return result

def cosine(x,y):
    result = 0
    try:
        result = multiply(transpose(x), y) / (norm(x) *norm(y))
        return result
    except:
        return result

def cosine_sim(x, y):
    return 1 - cosine(x,y)

# Feel free to add more
