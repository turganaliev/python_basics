def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
        return full_name.title()
    else:
        full_name = first + ' ' + last
        return full_name.title()
