import math,random
from math import log2

def class_type_def(dataset):
    class_type = []
    for row in dataset:
        class_type.append(row[-1])
    return class_type

def feature_class_cout(feature,class_type):
    result_dict = {}
    for i in range(len(class_type)):
        current_class = class_type[i]
        current_feature = feature[i]
        if current_feature not in result_dict:
            result_dict[current_feature] = {}
        if current_class not in result_dict[current_feature]:
            result_dict[current_feature][current_class] = 1
        else:
            result_dict[current_feature][current_class] += 1
    return result_dict

def Entropy_A_D(multy_dic):
    i = 0
    ddd = ""
    for m in multy_dic:
        for c in dict(multy_dic[m]):
            i += dict(multy_dic[m])[c]
    for m in multy_dic:
        ii = 0
        for mm in dict(multy_dic[m]):
            ii += dict(multy_dic[m])[mm]
        dd = f" ({ii}/{i}) * ("
        for c in dict(multy_dic[m]):
            cc = dict(multy_dic[m])[c]
            dd += f"({-cc}/{i}*log2({cc}/{i})) + "
        dd = dd[:-3]
        dd += ")"
        ddd += dd+" + "
    ddd = ddd[:-2]
    result = eval(ddd)
    return result

def Entropy_d(dataset):
    i = 0
    d = 0
    class_name_counter = {}
    for row in dataset:
        i += 1
        if row[-1] in class_name_counter:
            class_name_counter[row[-1]] = class_name_counter[row[-1]] + 1
        else:
            class_name_counter[row[-1]] = 1
    for x in class_name_counter:
        d -= (class_name_counter[x]/i)*math.log2(class_name_counter[x]/i)
    return class_name_counter , d

def Split_train_test(dataset):
    test = []
    test_count = (len(dataset)*30)//100
    i = 0
    while(i<test_count):
        if random.randint(0, 1) == 1:
            test.append(dataset.pop(random.randrange(len(dataset))))
            i += 1
    return test,dataset

def Split_feature(feature_index,dataset):
    feature = []
    for rp in dataset:
        feature.append(rp[feature_index])
    return feature

#-----Main-----#
with open('iris.data', 'r') as file:
    data = [line.strip().split(',') for line in file]
with open('iris.data', 'r') as file:
    main_data = [line.strip().split(',') for line in file]

#split to test and train
test_row, train_row = Split_train_test(data)
tree = []
col_name = ['sl','sw','pl','pw']

#loop for each
while col_name != []:
    ig_dic = {}  
    entropy_dataset,d_d = Entropy_d(data)

    if 'sl' in col_name:
        Sepal_Length_f = Split_feature(col_name.index('sl'),data)
    if 'sw' in col_name:
        Sepal_Width_f = Split_feature(col_name.index('sw'),data)
    if 'pl' in col_name:
        Petal_Length_f = Split_feature(col_name.index('pl'),data)
    if 'pw' in col_name:
        Petal_Width_f = Split_feature(col_name.index('pw'),data)

    class_type_f = class_type_def(data)

    if 'sl' in col_name:
        Sepal_Length_f_class_cout_f = feature_class_cout(Sepal_Length_f,class_type_f)
    if 'sw' in col_name:
        Sepal_Width_f_class_cout_f = feature_class_cout(Sepal_Width_f,class_type_f)
    if 'pl' in col_name:
        Petal_Length_f_class_cout_f = feature_class_cout(Petal_Length_f,class_type_f)
    if 'pw' in col_name:
        Petal_Width_f_class_cout_f = feature_class_cout(Petal_Width_f,class_type_f)

    if 'sl' in col_name:
        Entropy_SLF_SL = Entropy_A_D(Sepal_Length_f_class_cout_f)
    if 'sw' in col_name:
        Entropy_SLF_SW = Entropy_A_D(Sepal_Width_f_class_cout_f)
    if 'pl' in col_name:
        Entropy_SLF_PL = Entropy_A_D(Petal_Length_f_class_cout_f)
    if 'pw' in col_name:    
        Entropy_SLF_PW = Entropy_A_D(Petal_Width_f_class_cout_f)
    
    if 'sl' in col_name:
        ig_dic['sl'] = d_d-Entropy_SLF_SL
    if 'sw' in col_name:
        ig_dic['sw'] = d_d-Entropy_SLF_SW
    if 'pl' in col_name:
        ig_dic['pl'] = d_d-Entropy_SLF_PL
    if 'pw' in col_name:    
        ig_dic['pw'] = d_d-Entropy_SLF_PW

    biggest_feature = col_name[0]
    biggest_number = ig_dic[col_name[0]]
    for x in col_name:
        if ig_dic[x]>biggest_number:
            biggest_feature = x
    tree.append(biggest_feature)
    u = 0
    for row in data:
        ii = col_name.index(biggest_feature)
        data[u].pop(ii)
        u += 1
    col_name.remove(biggest_feature)
print(tree)
