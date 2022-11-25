



def main():
    s = input()
    n = len(s)
    st = []
    ans = []
    for idx, c in enumerate(s):
        if c == "(":
            st += [idx]
        else:
            bidx = st.pop()
            ans += [[bidx+1, idx+1]] 
    for i in ans:
        print(*i)       

if __name__ == "__main__":
    main()