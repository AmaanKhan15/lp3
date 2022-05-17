from math import *
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(train_row, test_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


train_data = [[2, 4, "Orange"], [4, 4, "Blue"], [4, 6, "Orange"], [4, 2, "Orange"], [6, 2, "Blue"], [6, 4, "Orange"]]
test_data = [[6, 6]]

for item in test_data:
    print("Data point : ", item)
    neighbors = get_neighbors(train_data, item, 3)
    print("Nearest Neighbors : ", neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    print("Prediction : ", prediction, "\n")
    
    
