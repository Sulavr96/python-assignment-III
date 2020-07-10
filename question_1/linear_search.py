def linear_search(given_list, key):
    given_list_length = len(given_list)

    for i in range(given_list_length):
        if given_list[i] == key:
            print("Key found at index: ", i)
            break
    else:
        print("Key not found")


user_list = [85, 21, 42, 33, 79, 91, 19, 57, 60]
search_key = int(input("Enter the number you want to search: "))

print(user_list)
linear_search(user_list, search_key)
