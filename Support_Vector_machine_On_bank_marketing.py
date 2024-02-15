import random

def svm(contact, duration):
    if contact == '"cellular"':
        return 'no'
    else:
        return 'yes'

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

def f_s(choosen_f,dataset):
    new_ds = []
    f_name = dataset.pop(0)
    for y in range(len(dataset)):
        init_new_ds = []
        for z in range(len(dataset[y][0].split(";"))):
            if z in choosen_f:
                init_new_ds.append(dataset[y][0].split(";").pop(z))
        init_new_ds.append(dataset[y][0].split(";").pop(z))    
        new_ds.append(init_new_ds)
    return new_ds, f_name

def outlayer(dataset):
    new_dataset = []
    for x in range(len(dataset)):
        is_error = False
        in_x = dataset[x][0].split(";")
        for y in in_x:
            if y == '"unknown"':
                is_error = True
        if not is_error:
            new_dataset.append(dataset[x])
    return new_dataset

with open('bank.csv', 'r') as file:
    data = [line.strip().split(',') for line in file]

data_f_s, f_names = f_s([8,11],data)

data_o = outlayer(data_f_s)

test_row, class_test, train = Split_train_test(data_o)

correct = 0
for t_r in range(len(test_row)):
    # print(t_r)
    loan = str(test_row[t_r][0])
    result = svm(loan,test_row[t_r][1])
    orig = class_test[t_r]
    if result == orig.replace('"', ''):
        correct += 1
accuracy = (correct/len(test_row))*100
print(f"Totall Row : {len(test_row)}")
print(f"Correct Predict : {correct}")
print(f"Accuracy : {accuracy}")
