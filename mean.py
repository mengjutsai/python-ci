def mean(num_list):
    # assert type(num_list)==list
    assert isinstance(num_list, list)
    for element in num_list:
        assert isinstance(element, int or float)
    # assert len(num_list)!=0
    # if len(num_list)==0:
    #     raise Exception("The algebraic mean of an empty list is undefined. Please provide a list of numbers.")
    # num_list = []
    # print(sum(num_list), len(num_list))

    # try to run with python
    # >>>> from mean import *
    # >>>> mean([])
    # Then you will get the error msg
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail:
        msg = "Please provide a list of numbers rather than an empty string"
        raise ZeroDivisionError(detail.__str__() + "\n" + msg)
