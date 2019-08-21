def mean(num_list):
    # assert type(num_list)==list
    assert isinstance(num_list, list)

    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError:
        return 0
    # TypeError will occur when the type is different as what we imagine
    # Like we put the string into the list we expect to use numbers
    except TypeError as detail:
        msg = "Please provide a list of numbers."
        # raise <exception>
        # The raise statement allows the programmer to force a specified exception to occur.

        raise TypeError(detail.__str__() + "\n" + msg)
