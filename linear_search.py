array = [2,5,6,8,4,3]

def search(target):

    count = 0
    found = False

    for num in array:
        if num == target:
            found = True
    
        else:
            count += 1
    
    if found:
        print(f"Target at index pos {count}")
    else:
        print("Target not found")
        

search(4)
