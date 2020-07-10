def binary_search(given_list, key):
    given_list_length = len(given_list)
    lower_bound = 0
    upper_bound = given_list_length - 1

    while lower_bound <= upper_bound:
        mid_value = (lower_bound + upper_bound) // 2

        if given_list[mid_value] == key:
            return True
        else:
            if given_list[mid_value] < key:
                lower_bound = mid_value + 1
            else:
                upper_bound = mid_value - 1


user_list = [85, 21, 42, 33, 79, 91, 19, 57, 60]
search_key = int(input("Enter the number you want to search: "))
user_list.sort()
print(user_list)

if binary_search(user_list, search_key):
    print("Key found")
else:
    print("Key not found")
