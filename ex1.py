
if __name__ == "__main__":

    arr = [2,7,2,4,8,5, 1, 3, 10]
    for i in range(len(arr)):
        if arr[i]&1:
            cur = i-1
            if i == 0:
                continue
            num = arr[i]
            while cur >= 0 and arr[cur]&1==0:
                arr[cur+1] = arr[cur]
                cur -= 1
            arr[cur+1] = num
    print(arr)
            