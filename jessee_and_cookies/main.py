from heapq import heapify, heappush, heappop


def cookies(sweetness_threshold, cookie_sweetness_heap):
    heapify(cookie_sweetness_heap)
    iterations = 0

    # peek the first value in the heap and check if it's lower than sweetness threshold
    while cookie_sweetness_heap[0] < sweetness_threshold:
        # if we run out of cookies to mashup, we lose
        if len(cookie_sweetness_heap) < 2:
            return -1
        first_least = heappop(cookie_sweetness_heap)
        second_least = heappop(cookie_sweetness_heap)
        new_sweetness = combine_sweetness(first_least, second_least)
        heappush(cookie_sweetness_heap, new_sweetness)
        iterations += 1
    return iterations


def combine_sweetness(first_least, second_least):
    return (second_least * 2) + first_least


if __name__ == '__main__':
    k = 7
    A = [1, 2, 3, 9, 10, 12]

    result = cookies(k, A)
    print(result)
