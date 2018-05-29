

def find_intersection(nums1, nums2):
    common_num = []
    n1 = {}
    n2 = {}
    for num in nums1:
        if num not in n1.keys():
            n1[num] = 0
        n1[num] = n1[num] + 1
    for num in nums2:
        if num not in n2.keys():
            n2[num] = 0
        n2[num] = n2[num] + 1
    for key in n1:
        if key in n2:
            v1 = n1[key]
            v2 = n2[key]
            v3 = min(v1, v2)
            for item in range(v3):
                common_num.append(key)
    return common_num



print (find_intersection([1, 1, 2, 3, 4, 5], [1, 6, 7, 2, 3]))

print (find_intersection([1, 2, 2, 1], [2, 2]))
