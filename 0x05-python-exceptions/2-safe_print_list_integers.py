def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                printed_integers += 1
    except (IndexError, ValueError, TypeError):
        pass  # Handle cases where x is greater than the list length or the element is not an integer

    print()  # Add a new line after printing the integers
    return printed_integers
