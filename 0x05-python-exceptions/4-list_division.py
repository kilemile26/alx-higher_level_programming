#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                result.append(my_list_1[i] / my_list_2[i])  # Perform the division
            else:
                result.append(0)  # Handle wrong type
                print("wrong type")
        except ZeroDivisionError:
            result.append(0)  # Handle division by 0
            print("division by 0")
        except IndexError:
            result.append(0)  # Handle out of range
            print("out of range")
        finally:
            # This code will be executed regardless of whether an exception occurred or not
            pass  # You can add specific actions here if needed

    return result

