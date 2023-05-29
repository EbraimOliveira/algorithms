def is_palindrome_recursive(word, low, high):
    word = word.strip().lower().replace(' ', '')

    if len(word) == 0:
        return False

    if word[low] == word[high]:
        low += 1
        high -= 1

        if low >= high:
            return True

        return is_palindrome_recursive(word, low, high)

    return False
