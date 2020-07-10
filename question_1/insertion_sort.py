def insertion_sort(unsorted_list):
    unsorted_list_length = len(unsorted_list)

    for list_index in range(1, unsorted_list_length):
        current_value = unsorted_list[list_index]
        current_position = list_index

        while current_position > 0 and unsorted_list[current_position - 1] > current_value:
            unsorted_list[current_position] = unsorted_list[current_position - 1]
            current_position -= 1

        unsorted_list[current_position] = current_value


given_list = [85, 21, 42, 33, 79, 91, 19, 57, 60]
print("Unsorted list:", given_list)

insertion_sort(given_list)

print("Sorted list:", given_list)
