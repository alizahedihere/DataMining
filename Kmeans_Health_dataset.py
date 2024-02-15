#####
import pandas as pd
from math import sqrt
import numpy as np 
####


###
def distance(list_1, list_2):
    under_sqrt = 0.0
    for x in range(len(list_1)):
        under_sqrt += ((list_1[x]-list_2[x])*(list_1[x]-list_2[x]))
    euclidean = sqrt(under_sqrt)
    return euclidean

def cal_dis_c_row(centroids, main_database):
    dict_dis = {}
    list_dis = []
    for c in centroids:
        in_list = []
        for x in range(main_database.shape[0]):
            row = main_database.iloc[x].tolist()
            dis = distance(c, row)           
            in_list.append(dis)
        list_dis.append(in_list)
    return list_dis

def create_initial_centroids(database,k):
    centroids = []
    min_max_features = []
    for x in database:
        min = database[x][0]
        max = database[x][0]
        for y in database[x]:
            if y < min:
                min = y
            else:
                if y > max:
                    max = y
        min_max_features.append([min,max])
    for x in range(k):
        c = []
        for y in min_max_features:
            if int(y[0]) == y[0]:
                r = np.random.randint(y[0],y[1])                
            else:
                r = round(np.random.uniform(y[0],y[1]),2)
            c.append(r)
        centroids.append(c)
    return centroids

def set_row_to_c(list_row):
    cluster = []
    for y in range(len(list_row[0])):
        up = list_row[0][y]
        down = list_row[1][y]
        if up < down:
            cluster.append(0)
        else:
            cluster.append(1)
    return cluster

def awe_centroid(main_database,cluster):
    new_centroid_0 = []
    new_centroid_1 = []
    i, j = 0, 0
    for x in range(main_database.shape[0]):
        row = main_database.iloc[x].tolist()
        if cluster[x] == 0:
            for y in range(len(row)):
                if y == len(new_centroid_0):
                    new_centroid_0.append(row[y])
                else:
                    new_centroid_0[y] += row[y]
            i += 1
        else:
            for y in range(len(row)):
                if y == len(new_centroid_1):
                    new_centroid_1.append(row[y])
                else:
                    new_centroid_1[y] += row[y]        
            j += 1
    for c in range(len(new_centroid_0)):
        new_centroid_0[c] = new_centroid_0[c]/i
    for c in range(len(new_centroid_1)):
        new_centroid_1[c] = new_centroid_1[c]/j
    return new_centroid_0, new_centroid_1
###

##
main_database = pd.read_csv("dataset_health.csv")
x_train = main_database.sample(frac=0.7, random_state=0)
x_test = main_database.drop(x_train.index)
death = x_train["DEATH_EVENT"].tolist()
x_train = x_train.drop(["DEATH_EVENT"],axis=1)
centroids = create_initial_centroids(x_train,2)
##

#
i = 0
while True:
    i += 1
    list_dis_c_row = cal_dis_c_row(centroids, x_train)
    cluster = set_row_to_c(list_dis_c_row)
    new_centroid_0, new_centroid_1 = awe_centroid(x_train, cluster)
    old = centroids
    centroids = [new_centroid_1,new_centroid_0]
    if centroids[1] == old[0]:
        break 
print(f"K-means Learned! step:{i}")
print(centroids)
#

#!
i = 0
death_test = x_test["DEATH_EVENT"].tolist()
for x in range(x_test.shape[0]):
    row = x_test.iloc[x].tolist()
    d1 = distance(centroids[0], row)
    d2 = distance(centroids[1], row)
    if d1 > d2:
        if death_test[death_test[x]] == 0:
            print("pass")
            i += 1
        else:
            print("failed")
    else:
        if death_test[death_test[x]] == 1:
            print("pass")
            i += 1
        else:
            print("failed")
accuracy = (i/x_test.shape[0])*100
print(f"The Accuracy is : {accuracy}")
#!
