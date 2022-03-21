def find_index(cookie_sweetness_list, new_sweetness):
    start = 0
    end = len(cookie_sweetness_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if cookie_sweetness_list[mid] == new_sweetness:
            return mid
        elif cookie_sweetness_list[mid] > new_sweetness:
            start = mid + 1
        else:
            end = mid - 1

    # Return the index to insert at and add one to make it after the current 'end'
    return end + 1


def cookies(sweetness_threshold, cookie_sweetness_list):
    # Start by sorting the cookies
    cookie_sweetness_list.sort(reverse=True)
    iterations = 0

    # while the last value in the array is less than the minimum sweetness index
    while cookie_sweetness_list[-1] < sweetness_threshold:
        # if we run out of cookies to mashup, we lose
        if len(cookie_sweetness_list) < 2:
            return -1
        first_least = cookie_sweetness_list.pop()
        second_least = cookie_sweetness_list.pop()
        new_sweetness = combine_sweetness(first_least, second_least)
        new_sweetness_index = find_index(cookie_sweetness_list, new_sweetness)
        cookie_sweetness_list.insert(new_sweetness_index, new_sweetness)
        iterations += 1
    return iterations


def combine_sweetness(first_least, second_least):
    return (second_least * 2) + first_least


if __name__ == '__main__':
    k = 7
    A = [1, 2, 3, 9, 10, 12]

    result = cookies(k, A)
    print(result)
