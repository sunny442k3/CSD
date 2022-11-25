
from linked_list import LinkedList


# O(logN)
def build_tree(k: int, l: int, r: int, A: list) -> int:
    if l > r:
        return 0
    if l == r:
        return A[l]
    m = (l+r)//2
    get_left = build_tree(2*k+1, l, m, A)
    get_right = build_tree(2*k+2, m+1, r, A)
    return get_left + get_right


if __name__ == "__main__":
    arr = [1,2,3,4,2,1,5,2]
    N = len(arr)
    print(build_tree(0, 0, N-1, arr))


def longest_none_des(L: LinkedList) -> list:
    cur = L.head # Get head node
    arr = [cur.data] 
    while cur.next is not None:
        cur = cur.next 
        arr += [cur.data]

    N = L.get_len() # Get size list
    end_idx = -1
    max_length = 1
    tmp_length = 1

    for i in range(1, N):
        if arr[i] >= arr[i-1]:
            tmp_length += 1 
        else:
            if tmp_length > max_length:
                max_length = tmp_length
                end_idx = i-1
                tmp_length = 1
    
    if tmp_length > max_length:
        max_length = tmp_length 
        end_idx = N-1

    return arr[end_idx-max_length+1: end_idx+1]

def recur(A: list, n: int, k: int) -> None:
    left = 2*k + 1
    right = left+1

    max_idx = k
    for idx in [left, right]:
        if idx < n and A[idx] > A[max_idx]:
            max_idx = idx 
    
    if max_idx != k:
        # Swap
        A[k] += A[max_idx]
        A[max_idx] = A[k] - A[max_idx]
        A[k] -= A[max_idx]

        recur(A, n, max_idx)


def heap_sort(A: list) -> None:
    n = len(A)
    last_root = n//2 - 1
    for k in range(last_root, -1, -1):
        recur(A, n, k)
    
    for i in range(n-1, 0, -1):
        A[i] += A[0]
        A[0] = A[i] - A[0]
        A[i] -= A[0]
        recur(A, i, 0)