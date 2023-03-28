#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = float(my_list_1[i]) / float(my_list_2[i])
            new_list.append(div)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except (ValueError, TypeError):
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            pass
    return new_list
