def quick_sort(unsorted_list):
    unsorted_list_length = len(unsorted_list)

    if unsorted_list_length <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list.pop()

    greater_items = []
    lower_items = []

    for item in unsorted_list:
        if item > pivot:
            greater_items.append(item)
        else:
            lower_items.append(item)

    return lower_items + [pivot] + greater_items


given_list = [85, 21, 42, 33, 79, 91, 19, 57, 60]

print("Unsorted list:", given_list)

print("Sorted list:", quick_sort(given_list))
