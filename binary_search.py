

def bs_recur(a, x, l, r):
    if l > r or l < 0 or r >= len(a):
        return -1
    
    mid = int((l+r)/2)
    if a[mid] == x:
        return mid 
    elif a[mid] > x:
        return binary_search(a, x, l, mid-1)
    else:
        return binary_search(a, x, mid+1, r)
    
    return -1


def bs(a, x):
    l = 0
    r = len(a)

    while l < r:
        mid = int((l+r)/2)
        if a[mid] == x:
            return mid 
        if a[mid] > x:
            r = mid-1
        else:
            l = mid+1
    return -1


def get_num(n, k):
    ans = 1
    if k > n-k:
        k = n-k
    for i in range(k):
        ans *= (n-i)
        ans /= (i+1)
        ans = int(ans)
    return ans

def pascal_triangle(n, cur):
    if cur > n:
        return
    for i in range(cur+1):
        print(get_num(cur, i), end=" ")
    print("\n")
    pascal_triangle(n, cur+1)



if __name__ == "__main__":
    pascal_triangle(5,0)