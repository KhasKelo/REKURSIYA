def get_multplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multplied_digits(int(str_number[1:]))
    else:
         return first



print(get_multplied_digits(40203))

