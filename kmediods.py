import itertools
import copy
import csv
import random
import math
random.seed(42)
records = []
row_count = sum(1 for row in csv.reader(open('kmeans_data.csv')))
with open('kmeans_data.csv', 'rt') as f:
    reader = csv.reader(f)
    records = list(reader)
n = len(records[0])
for i in range(0, row_count):
    for j in range(0, n):
        records[i][j] = float(records[i][j])
k = int(input("Enter k: "))
c = []
for i in range(0, k):
    c.append(random.randint(1, row_count) - 1)
flag = 0
clusters = []
for i in c:
    s = set()
    s.add(i)
    clusters.append(s)

# Define a Manhattan distance function


def manhattan_distance(point1, point2):
    return sum(abs(point1[j] - point2[j]) for j in range(n))


for i in range(0, row_count):
    if i not in c:
        min_dist = float('inf')
        min_index = 0
        for x in range(0, k):
            dist = manhattan_distance(records[i], records[c[x]])
            if dist < min_dist:
                min_dist = dist
                min_index = x
        clusters[min_index].add(i)

while not flag:
    flag = 1
    means = []
    c = []
    for i in range(0, k):
        s = clusters[i]
        temp = []
        for x in range(0, n):
            temp.append(sum(records[j][x] for j in s) / len(s))
        c.append(temp)
    for i in range(0, row_count):
        min_dist = float('inf')
        min_index = 0
        for x in range(0, k):
            dist = manhattan_distance(records[i], c[x])
            if dist < min_dist:
                min_dist = dist
                min_index = x
        if i not in clusters[min_index]:
            flag = 0
            for j in range(0, k):
                if i in clusters[j]:
                    clusters[j].remove(i)
            clusters[min_index].add(i)

print("The clusters are:")
print(clusters)
