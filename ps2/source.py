
CSV_PATH = "./groceryGoods.csv"


class Grocery:

    def __init__(self, *args):
        self.no = args[0]
        self.code = args[1]
        self.name = args[2]
        self.price = args[3] 
        self.next = None 


class LinkedList:

    def __init__(self, col_name):
        self.head = None
        self.col_name = col_name

    def add_node(self, data: Grocery):
        if self.head is None:
            self.head = data 
            return 
        cur = self.head 
        while cur.next is not None:
            cur = cur.next
        cur.next = data 

    def size(self):
        if self.head is None:
            return 0
        cur = self.head 
        ans = 1
        while cur.next is not None:
            cur = cur.next
            ans += 1
        return ans


def read_csv(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        data = [i.strip("\n") for i in data]
        data = [i.split(",") for i in data]
        for i in range(1,len(data)):
            data[i][0] = int(data[i][0])
            data[i][-1] = float(data[i][-1])
        return data[0], data[1:]


def txt_reader(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        data = [i.strip("\n").split(" ") for i in data]
        for i in range(len(data)):
            data[i][1] = float(data[i][1])
        return data


def questionA():
    head, data = read_csv(CSV_PATH)
    return head, data


def questionB(col_name):
    L = LinkedList(col_name)
    return L 

def questionC(L: LinkedList, data):
    for row in data:
        new_gro = Grocery(*row)
        L.add_node(new_gro)

def questionD(L: LinkedList, dump_into = "./d.txt"):
    ls = []
    cur = L.head
    if cur is None:
        return 
    ls.append([cur.code, cur.price])
    while cur.next is not None:
        cur = cur.next 
        ls.append([cur.code, cur.price])

    tmp = sorted(ls, key=lambda x: x[1], reverse=True)
    ans = []
    max_price = tmp[0][1]
    for i in ls:
        if i[1] == max_price:
            ans.append(i[0])
    ans = "\n".join(ans)
    with open(dump_into, "w") as f:
        f.write(ans)
        f.close()


def questionE(L: LinkedList):
    new_update = txt_reader("./update.txt")
    dict_update = {}
    for _code, _price in new_update:
        if _code not in dict_update:
            dict_update[_code] = _price 
        else:
            dict_update[_code] = _price

    cur = L.head 
    while cur is not None:
        if cur.code in dict_update:
            cur.price = dict_update[cur.code] 
        cur = cur.next 
    
    questionD(L, "./e.txt")


def questionF(L: LinkedList):
    ls = []
    static_lk = []
    cur = L.head
    if cur is None:
        return 
    ls.append([cur.code, cur.no])
    static_lk.append(cur)
    while cur.next is not None:
        cur = cur.next 
        ls.append([cur.code, cur.no])
        static_lk.append(cur)
    
    store = {}
    ans = []
    for _code, _no in ls:
        if _code in store:
            ans.append(_no)
        else:
            store[_code] = 1
    ans = [str(i) for i in ans]
    ans = "\n".join(ans)
    with open("./f.txt", "w") as f:
        f.write(ans)
        f.close()
    
    ans = ans.split("\n")
    ans = [int(i) for i in ans]
    tmp = list(filter(lambda gro: gro.no not in ans ,static_lk))
    for i in range(len(tmp)):
        tmp[i] = [tmp[i].no, tmp[i].code, tmp[i].name, tmp[i].price]
    L.head = None 
    questionC(L, tmp)




if __name__ == "__main__":
    # Question A
    head, data = questionA()
    
    # Question B
    L = questionB(head)

    # Question C
    questionC(L, data)

    # Question D
    questionD(L)

    # Question E
    questionE(L)

    # Question F
    questionF(L)