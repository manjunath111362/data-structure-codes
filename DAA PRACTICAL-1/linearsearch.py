n=int(input("enter number of elements:"))
arr=[]
print("enter elements:")
for i in range(n):
    arr.append(int(input()))
target=int(input("enter element to search:"))  
found=False
for i in range(n):
    if arr[i]==target:
        print("element found at index:",i)
        found=True
        break
else:
        print("element not found")
