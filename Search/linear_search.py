array = [1,3,45,54,2]

def linear_search(items, target):
    found = False
    index = 0

    while not found and index < len(items):
        if items[index] == target:
            found = True
            return f"Item at {index + 1}"
        else:
            index += 1



print(linear_search(array, 4))

