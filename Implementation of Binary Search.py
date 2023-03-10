def b_search(a,x,l,n):
    if l<=n:
        mid=(l+n)//2
        if a[mid]==x:
            print("The element found at",mid+1,"position")
        else:
            if a[mid]>x:
                b_search(a,x,l,mid-1)
            else:
                b_search(a,x,mid+1,n)
    else:
        print("Element not found")
print("Enter list:")
a=[int(b) for b in input().split()] 
list.sort(a) 
print("the sorted list is",a) 
x=eval(input("Enter the search element:")) 
n=len(a) 
b_search(a,x,0,n)
