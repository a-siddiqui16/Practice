items = [1,4,5,2,4,6,3,12,5,6]

def sort(values):

    n = len(items)
    swapped = True

    while n > 0 and swapped == True:
        swapped = False
        n -= 1

        for i in range(0, n):
            if items[i] > items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
                swapped = True
                
    return items


print(sort(items))

