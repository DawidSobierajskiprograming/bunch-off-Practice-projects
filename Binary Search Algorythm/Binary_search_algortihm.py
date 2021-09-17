
def search(list, target, low, high):

    if high >= low:
        
    
        mid = (high + low) // 2

        if list[mid] == target:
            return mid
        
        elif target < list[mid]:
            print(1)
            return search(list, target, low, mid - 1 )
            
        else:
            print(2)
            return search(list, target, mid + 1,high  )
            
    else:
         return -1  



numbers = [1,3,4,6,7,11,12,25,37,55]
target = 55


result = search(numbers, target, 0, len(numbers)-1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")