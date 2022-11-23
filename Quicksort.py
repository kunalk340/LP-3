import random    

def partition(a,lb,ub):
    pivot = a[lb]
    start = lb 
    end = ub
    while start < end:
        while (a[start] <= pivot and start < end) :
            start = start + 1
        while a[end] > pivot:
            end = end - 1
        if start < end:
            a[start], a[end] = a[end], a[start]
    a[lb], a[end] = a[end], a[lb]
    return end

def partitionrand(a,lb,ub):
    start = lb 
    randpivot = random.randrange(lb,ub)
    a[start], a[randpivot] = a[randpivot], a[start]
    return partition(a,lb,ub)

def quick_sort(a,lb,ub):
    if lb < ub:
        loc = partition(a,lb,ub)
        quick_sort(a, lb, loc-1)
        quick_sort(a, loc+1, ub)
    return a

def main():
    a = []
    m = int(input("Enter the number of elemens: "))
    for i in range(m):
        b =int(input("\tEnter the elements: "))
        a.append(b)
    print("\nThe elements entered are: ")
    for i in range(m):
        print(a[i],end="  ")

    print("\n\nThe sorted order is :",quick_sort(a,0,m-1))    
main()           
