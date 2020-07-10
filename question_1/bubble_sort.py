def bubble_sort(unsorted_list):
    unsorted_list_length = len(unsorted_list)

    for number in range(unsorted_list_length - 1, 0, -1):
        for i in range(number):
            if unsorted_list[i] > unsorted_list[i + 1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = temp


given_list = [85, 21, 42, 33,  79, 91, 19, 57, 60]
print("Unsorted list:", given_list)

bubble_sort(given_list)

print("Sorted list:", given_list)
