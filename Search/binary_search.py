items = [1,2,3,4,5,6,9,32]


def binary_search(items, target):

    found = False
    first = 0
    last = len(items) - 1

    while first <= last and not found:

        mid = (first + last) // 2

        if items[mid] == target:
            found = True
            

        else:
            if items[mid] < target:
                first = mid + 1
            else:
                last = mid - 1


    if found:
        return True
    else:
        return False


print(binary_search(items, 00))