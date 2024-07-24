# LINEAR SEARCH
def linear_search(arr,element):
    count=0
    for i in range(len(arr)):
        count=count+1
        if arr[i]==element :
            print("the index of the element:",i)
            print("the count for linear search is:",count)
            return i
    print("element not found")
    return -1

# BINARY SEARCH
def binary_search(brr,element):
    count=0
    temp=0
    f=0
    l=len(brr)
    
    for i in range(len(brr)-1):
        for j in range(i+1,len(brr)):
            if brr[i]>brr[j]:
                temp=brr[i]
                brr[i]=brr[j]
                brr[j]=temp
    while(f<=l):
        count+=1
        mid=(l+f)/2
        if element==brr[mid]:
            return i
menu=int(input("input the menu number:"))        
while menu!=0:           
    element=int(input("enter the number to be found:"))
    m=int(input("enter the number of element in the list:"))
    arr=[]
    NUMBER=int(input("enter the number for searching the element:"))
    for i in range(0,m):
        arr.append(int(input()))
    if NUMBER==1:
        linear_search(arr,element)
    else:
        print(binary_search(arr,element))
