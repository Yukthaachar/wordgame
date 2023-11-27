def transform1(file1):
    f1 = open(file1, 'r')
    list1 = f1.read().split("\n")
    list3 = []
    for i in range (0,26,1):
        list2 = list1[i].split(',')
        list3.append(list2)
    return list3

