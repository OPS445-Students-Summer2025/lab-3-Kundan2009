#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends a new item to the end of the list with the value (last item + 1)
    if ordered_list:  # check list is not empty
        new_value = ordered_list[-1] + 1
    else:
        new_value = 1
    ordered_list.append(new_value)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values found in items_to_remove from ordered_list
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
