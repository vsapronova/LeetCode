

def bubble_sort(bad_list):
    i = 0
    while i != len(bad_list):
        for i in range(len(bad_list)):
            if bad_list[i] > bad_list[i + 1]:
                bad_list[i], bad_list[i + 1] = bad_list[i + 1], bad_list[i]

    return bad_list


print (bubble_sort([93, 11, 20, 0, 30, 5]))