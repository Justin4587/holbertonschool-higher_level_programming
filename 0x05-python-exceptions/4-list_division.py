#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    d_list = []
    for i in range(list_length):
        dividend = 0
        try:
            dividend = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        except (IndexError):
            print("out of range")
        finally:
            d_list.append(dividend)
    return(d_list)
