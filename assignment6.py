#bubble_sort
def Bubble_sort(n,list):
    count=0
    for i in range(n-1,0,-1):
        swap=0
        for j in range(0,i):
            if(list[j+1]<list[j]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                count+=1
                swap=1
            print("array after the pass:",list)
        if(swap==0):
            break
    print("the total count:",count)
    return list
#Selection sort
def Selection_sort(n,list):
    count=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(list[i]>list[j]):
                temp=list[i]
                list[i+1]=list[i]
                list[i]=temp
                print("array after the pass:",list)
            print("array after the pass:",list)
            count+=1
    print("the total count:",count)
    return list
def insertion_sort(n,list):
    count=0
    for i in range(1,n):
        temp=list[i]
        j=i-1
        while(j>=0 and list[j]>temp):
            list[j+1]=list[j]
            print("array after the pass:",list)
            j-=1
            count+=1
        print("array after the pass:",list)
        list[j+1]=temp
    print("the total count:",count)
    return list

def shell_sort(list,n):
    count=0
    gap=n//2
    while(gap!=0):
        for j in range(gap,n):
            i=j-gap
            while(i>=0):
                if(list[i]>list[i+gap]):
                    temp=list[i]
                    list[i]=list[i+gap]
                    list[i+gap]=temp
                    print("array after the pass:",list)
                else:
                    print("array after the pass:",list)
                    break
                count+=1
                i-=gap
        gap=gap//2
    print("the total count:",count)
    return list
def radix_bucket_sort(list,n):
    count=0
    number=1
    max_val=max(list)
    while(max_val!=0):
        max_val=max_val//10
        count+=1
    while(count!=0):
        bucket=[[]for i in range(0,10)]
        for j in range(0,n):
            q=list[j]//number
            r=list[j]%10
            bucket[r].append(list[j])
        index=0
        for b in bucket:
            for item in b:
                list[index]=item
                index+=1
        number=number*10
        count-=1
    return list
def quick_sort(list,n):
    def partition(low, high):
        pivot = list[high]
        i = low - 1
        for j in range(low, high):
            if list[j] <= pivot:
                i += 1
                list[i], list[j] = list[j],;list[i]
        list[i + 1], list[high] = list[high], list[i + 1]
        return i + 1
def radi_counting_sort(list,n):
    count=0
    number=1
    arr=[]
    max_val=max(list)
    while(max_val!=0):
        max_val=max_val//10
        count+=1
    while(count!=0):
        count=[0]*10
        for j in range(0,n):
            r=(list[j]//number)%10
            list[j]=list
            count[r]+=1
        for i in range (0,10):
            count[i]=count[i]+count[i-1]
        for k in range(n-1,-1,-1):
            r=(list[k]//number)%10
            count[r]-=1
            arr[count[r]]=list[k]
        for i in range(0,n):
            list[i]=arr[i]
        number=number*10
        count=-1
    return list
    
    
n=int(input("Enter the number of element of the list:"))
value=int(input("enter the value:"))
list=[]
for i in range(0,n):
    x=int(input("enter the input:"))
    list.append(x)
while value!=0:
    menu=int(input("Enter the menu item:"))
    if(menu==1):
        result=Bubble_sort(n,list)
        print("the sorted list:",result)
        value=int(input("enter the value:"))
    elif(menu==2):
        answer=Selection_sort(n,list)
        print("the sorted list:",answer)
        value=int(input("enter the value:"))
    elif(menu==3):
        array=insertion_sort(n,list)
        print("the sorted list:",array)
        value=int(input("enter the value:"))
    elif(menu==4):
        brray=shell_sort(list,n)
        print("the sorted list:",brray)
        value=int(input("enter the value:"))
    elif(menu==5):
        crray=radix_bucket_sort(list,n)
        print("the sorted list:",crray)
        value=int(input("enter the value:"))
    elif(menu==6):
        drray=radi_counting_sort(list,n)
        print("the sorted list:",crray)
        value=int(input("enter the value:"))
