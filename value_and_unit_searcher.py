

def search_for_value(word) -> float:
    try:
        number = float(word)
    except:
        number = None
    return number


def value_processing(object_found, number_str):
    potential_number = search_for_value(number_str)
    if type(potential_number) == float:
        object_found.values.append(potential_number)


if __name__ == '__main__':
    a_word, b_word, c_word, d_word = "57v", "kalashnikov", "hello", "-40°C"
    a = search_for_value(a_word)
    b = search_for_value(b_word)

