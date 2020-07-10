def merge_sort(unsorted_list):
    unsorted_list_length = len(unsorted_list)

    # Dividing code

    if unsorted_list_length > 1:
        mid = unsorted_list_length // 2
        left_list = unsorted_list[:mid]
        right_list = unsorted_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        # merging code

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                unsorted_list[k] = left_list[i]
                i += 1
            else:
                unsorted_list[k] = right_list[j]
                j += 1

            k += 1

        while i < len(left_list):
            unsorted_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            unsorted_list[k] = right_list[j]
            j += 1
            k += 1


given_list = [85, 21, 42, 33, 79, 91, 19, 57, 60]
print("Unsorted list:", given_list)

merge_sort(given_list)

print("Sorted list:", given_list)
