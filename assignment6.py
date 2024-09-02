#bubble_sort
def Bubble_sort(n,list):
    for i in range(n-1,0,-1):
        swap=0
        for j in range(0,i):
            if(list[j+1]<list[j]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                swap=1
        if(swap==0):
            break
    return list
#Selection sort
def Selection_sort(n,list):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(list[i]>list[j]):
                temp=list[i]
                list[i+1]=list[i]
                list[i]=temp
    return list
def insertion_sort(n,list):
    for i in range(1,n):
        temp=list[i]
        j=i-1
        while(j>=0 and list[j]>temp):
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp
    return list

def shell_sort(list,n):
    gap=n//2
    while(gap!=0):
        for j in range(gap,n):
            i=j-gap
            while(i>=0):
                if(list[i]>list[i+gap]):
                    temp=list[i]
                    list[i]=list[i+gap]
                    list[i+gap]=temp
                else:
                    break
                i-=gap
        gap=gap//2
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
    
