

def main():
    n = int(input())
    st = {}
    for i in range(2, n+1):
        if n== 1:
            break
        while n % i == 0:
            if i not in st:
                st[i] = 1
            else:
                st[i] += 1
            n = n//i
    print(len(st.keys()))
    for k, v in st.items():
        print(k, v)

if __name__ == "__main__":
    main()