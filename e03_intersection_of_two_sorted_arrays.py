

def find_intersection(list1, list2):
    common_nums = []
    i1 = 0
    i2 = 0
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] == list2[i2]:
            common_nums.append(list1[i1])
            i1 += 1
            i2 += 1
        else:
            if list1[i1] < list2[i2]:
                i1 += 1
            else:
                i2 += 1
    return common_nums


print (find_intersection([1, 2, 3, 4, 4, 6, 8], [2, 3, 4, 4, 6, 9]))