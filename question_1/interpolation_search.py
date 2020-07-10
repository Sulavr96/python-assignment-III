def interpolation_sort(given_list, key):
    given_list_length = len(given_list)
    lower_bound = 0
    upper_bound = given_list_length - 1

    while lower_bound <= upper_bound and given_list[lower_bound] <= key <= given_list[upper_bound]:
        if lower_bound == upper_bound:
            if given_list[lower_bound] == key:
                return lower_bound
            return -1

        position = lower_bound + int(((float(upper_bound - lower_bound) /
                                       (given_list[upper_bound] - given_list[lower_bound])) *
                                      (key - given_list[lower_bound])))
        if given_list[position] == key:
            return position

        if given_list[position] < key:
            lower_bound = position + 1

        else:
            upper_bound = position - 1

    return -1


user_list = [85, 21, 42, 33, 79, 91, 19, 57, 60]
search_key = int(input("Enter the number you want to search: "))
user_list.sort()
print(user_list)

search_key_index = interpolation_sort(user_list, search_key)

if search_key_index != -1:
    print("Key found at index:", search_key_index)
else:
    print("Key not found")
