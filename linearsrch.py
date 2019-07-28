def search(arr, n, x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1

arr=[10,25,35,45,12,36,67]

#n stores len of array
n=len(arr)

#x takes element to be searched
x=int(input("enter the element whose index is to be returned: "))

#result gives index
result=search(arr, n, x)

if result==-1:
    print("index not found")
else:
    print("element is at pos:", result)
