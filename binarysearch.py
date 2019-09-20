def binarysearch(arr,ki,ka,x):
    while ki <= ka:
        mid = ki + int ((ka-ki)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            ki = mid + 1
        else :
            ki = mid - 1
    return -1
arr = [4,7,8,9,13,16,18,20]

x = 9

result = binarysearch(arr,0,len(arr)-1,x)
if result != -1 :
    print("Value ditemukan di index ke",result)
else :
    print("value tidak di temukan di index manapun")



