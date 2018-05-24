def find_number(list):
    list1 = []
    list2 = []
    for number in list:
        if number not in list1:
            list1.append(number)
        else:
            list2.append(number)
    return [x for x in list1 if x not in list2]


def numbers(list_of_numbers):
    occurs = [0] * 10
    for number in list_of_numbers:
        occurs[number] = occurs[number] + 1
    new_list = []
    for oc_number in range(len(occurs)):
        if occurs[oc_number] == 1:
            new_list.append(oc_number)
    return new_list


print(find_number([1, 2, 3, 4, 3, 2, 1]))
print(numbers([1, 1, 4, 5, 5, 6, 7, 7]))
