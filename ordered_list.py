def get_ordered_list(lst=None):
    if lst == None:
        input_str = input("Enter numbers separated by commas: ")
        lst = [int(x.strip()) for x in input_str.split(",")]
    return sorted(lst)