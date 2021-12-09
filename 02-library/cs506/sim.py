import random

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
    intersection = len(list(set(x).intersection(y)))
    union = (len(set(x)) + len(set(y))) - intersection
    if union == 0:
        return 1
    else:
        return 1 - float(intersection) / union

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

def dot_prod(A,B): 
    return (sum(a*b for a,b in zip(A,B)))

def cosine_sim(x, y):
    if dot_prod(x,x) == 0 or dot_prod(y,y) == 0:
        return 0
    else:
        return dot_prod(x,y) / ( (dot_prod(x,x) **.5) * (dot_prod(y,y) ** .5) )