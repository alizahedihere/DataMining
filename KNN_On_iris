import matplotlib.pyplot as plt
import math
import random

# Read Iris
with open('iris.data', 'r') as file:
    data = [line.strip().split(',') for line in file]
    
# Split train and test
def Split_train_test(dataset):
    test = []
    test_count = (len(dataset)*30)//100
    i = 0
    while (i < test_count):
        if random.randint(0, 1) == 1:
            test.append(dataset.pop(random.randrange(len(dataset))))
            i += 1
    class_test = []
    for t in range(len(test)):
        class_test.append(test[t].pop(-1))
    return test, class_test, dataset

# KNN function
def knn(row, dataset, k):
    d_class = []
    for row_dataset in dataset:
        d_class_inner = 0
        for f in range(len(row)):
            d_class_inner += math.pow(float(row_dataset[f])-float(row[f]), 2)
        if d_class_inner < k:
            d_class.append([math.sqrt(d_class_inner), row_dataset[-1]])
    return d_class

# Check data
def check_data(element):
    dictionary = element[0]
    string = element[1]
    max_key = max(dictionary, key=dictionary.get)
    if max_key == string:
        return True
    else:
        return False

# Function call
accuracy = {}
for k in range(1, 11):
    test_row, class_test, train = Split_train_test(data)
    i = 0
    main_dic = {}
    for row in test_row:
        knn_row = knn(row, train, k)
        li = {}
        for kn in knn_row:
            if kn[1] in li:
                li[kn[1]] += 1
            else:
                li[kn[1]] = 1
        main_dic[i] = [li, class_test[i]]
        i += 1
    t_num = 0
    f_num = 0
    for element in main_dic:
        result = check_data(main_dic[element])
        if result == True:
            t_num += 1
        else:
            f_num += 1
    accuracy[k] = [t_num, f_num]

# Accuracy
max_t_num = max(accuracy.values())[0]
max_k = max(accuracy, key=accuracy.get)
print(f"t_num and f_num for different k values:")
for k in accuracy:
    print(f"k = {k}, t_num = {accuracy[k][0]}, f_num = {accuracy[k][1]}")
print(f"Maximum value of k for maximum t_num: {max_k}")

# Ploting
k_list = []
t_num_list = []
for k in accuracy:
    k_list.append(k)
    t_num_list.append(accuracy[k][0])
plt.plot(k_list, t_num_list, color="green", label="t_num")
plt.xlabel("k")
plt.ylabel("Number of correct predictions")
plt.title("Accuracy of KNN algorithm for different k values")
plt.legend()
max_t_num = max(accuracy.values())[0]
max_k = max(accuracy, key=accuracy.get)
plt.annotate(f"Maximum t_num with k = ({max_t_num} , {max_k})", xy=(max_k, max_t_num), xytext=(
    max_k + 1, max_t_num - 5), arrowprops=dict(facecolor="black"))
plt.show()
