#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        int = 0
        try:
            int = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        except (ZeroDivisionError):
            print("division by 0")
        finally:
            list.append(int)
    return (list)
