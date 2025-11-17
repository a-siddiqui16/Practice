items = [1,3,5,6,7,8]

def search(target):

    found = False
    first = 0
    last = len(items) - 1

    while first <= last and found == False:

        midpoint = (first + last) // 2
        
        if items[midpoint] == target:
            found = True
            break

        else:
            if items[midpoint] < target:
                first = midpoint + 1

            else:
                last = midpoint - 1

    return found


print(search(7))


