def l_search(a,x,l,n):
    if  l<n:
        if a[l]==x:
            print("The element found at",l+1,"position")
        else:
            l_search(a,x,l+1,n)
    else:
        print("Element not found")
print("Enter list:") 
a=[int(b) for b in input().split()] 
x=eval(input("Enter the search element:")) 
n=len(a)
l_search(a,x,0,n)
