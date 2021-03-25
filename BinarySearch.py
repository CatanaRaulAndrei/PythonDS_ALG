def binary_search(target, input_list):
    middleIndex = int((len(input_list) - 1) / 2) + 1
    for idx in range(len(input_list)):
        # 1.target is not in the list
        if target not in input_list: return False
        # 2.target is in the middle of the list
        if target == input_list[middleIndex]: return input_list[middleIndex]
        # 3.target is in left side of the list
        if target < input_list[middleIndex]:
            middleIndex = middleIndex - 1
            return target
        # 4.target is in right side of the list
        if target >= input_list[middleIndex + 1]:
            middleIndex = middleIndex + 1
            return target


print(binary_search(90, [1, 7, 8, 23, 45, 71, 90, 101]))
"""

1.if target is not in the list, return False
2.if target is in the middle of the list, return middle element
3.if target is < than the middle element, search in the left side of the list
4.if target is >= than the middle element, search in the right side of the list

"""
