from collections import defaultdict
from math import inf
import random
import csv
import sys

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    centroid = []
    if isinstance(points[0], list):
        for i in range(len(points[0])):
            x = [p[i] for p in points]
            centroid.append(sum(x)/len(points))
    else:
        x = [p for p in points]
        centroid.append(sum(x)/len(points))

    return centroid


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    clusters = list(set(assignments))
    clusters.sort()
    centroids = []

    for cluster in clusters:
        cluster_points = []
        for i in range(len(dataset)):
            if assignments[i] == cluster:
                cluster_points.append(dataset[i])
        centroids.append(point_avg(cluster_points))

    return centroids

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    result = 0

    for i in range(len(a)):
        result += (a[i] - b[i])**2
    return result**(1/2)

def distance_squared(a, b):
    return distance(a,b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    result = []
    index = [i for i in range(len(dataset))]
    index_choice = random.choices(index, k=k)
    for i in range(len(dataset)):
        if i in index_choice:
            result.append(dataset[i])
    return result

def cost_function(clustering):
    cost = 0
    for cluster_id in clustering.keys():
        cluster = clustering.get(cluster_id)
        average_point = point_avg(cluster)
        for entry in cluster:
            cost += distance_squared(entry, average_point)
    return cost


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centroids = []
    centroids.append(random.choice(dataset))
    for i in range(1,k):
        distances, prob_sums, pp = [], [], [];
        
        for point in dataset:   
            max_d = sys.maxsize
            for j in range(len(centroids)):
                dist = distance(point, centroids[j])
                distances.append(min(max_d, dist))
            dist_sum = sum(distances)
            prob = max_d / dist_sum
            pp.append(prob)
            prob_sums.append(sum(pp))

        rand_int = random.randrange(0,1)
        for prob in prob_sums:
            if rand_int < prob:
                i = j
                break
        centroids.append(dataset[i])
    return centroids  


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
