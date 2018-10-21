def nz(value, value_if_null=0):
    # Copy of the nz function in VBA
    # If value_if_null isn't specified, default to 0

    if value is None:
        return value_if_null
    else:
        return value


def first_item_in_nested_list(nested_list):
    first_item_list = []
    for full_item in nested_list:
        first_item_list.append(full_item[0])

    return first_item_list