# def bubble_sort(string):
#     string = list(string.strip().lower().replace(" ", ""))
#     for iteracao in range(len(string)-1, 0, -1):
#         for i in range(iteracao):
#             if string[i] > string[i + 1]:
#                 temp = string[i]
#                 string[i] = string[i + 1]
#                 string[i + 1] = temp
#     return string


# def is_anagram(fst_string, scnd_string):
#     str_01 = ''.join(bubble_sort(fst_string))
#     str_02 = ''.join(bubble_sort(scnd_string))
#     true_or_false = True
#     if str_01 != str_02 or len(fst_string) == 0 == len(scnd_string):
#         true_or_false = False

#     return str_01, str_02, true_or_false


def merge_sort(vector):
    length = len(list(vector))
    if length > 1:
        mid = length // 2
        left_vector = vector[:mid]
        right_vector = vector[mid:]

        # recursion
        merge_sort(left_vector)
        merge_sort(right_vector)

        merge(vector, left_vector, right_vector)

    return vector


def merge(vector, left_vector, right_vector):
    i = j = k = 0
    while i < len(left_vector) and j < len(right_vector):
        if left_vector[i] <= right_vector[j]:
            vector[k] = left_vector[i]
            i += 1
        else:
            vector[k] = right_vector[j]
            j += 1
        k += 1

    while i < len(left_vector):
        vector[k] = left_vector[i]
        i += 1
        k += 1

    while j < len(right_vector):
        vector[k] = right_vector[j]
        j += 1
        k += 1


def is_anagram(fst_string, scnd_string):
    str_01 = merge_sort(list(fst_string.strip().lower().replace(' ', '')))
    str_02 = merge_sort(list(scnd_string.strip().lower().replace(' ', '')))
    true_or_false = True
    if str_01 != str_02 or len(fst_string) == 0 == len(scnd_string):
        true_or_false = False

    return ''.join(str_01), ''.join(str_02), true_or_false
