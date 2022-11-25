
class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None 


class LinkedList:

    def __init__(self, name_col):
        self.head = None 
        self.name_col = name_col

    
    def add_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head 
            while cur.next is not None:
                cur = cur.next 
            
            cur.next = Node(data)

    
    def round_score(self, node):
        for k in self.name_col[2:5]:
            node.data[k] = round(node.data[k], 2)
        
        if "Average" in self.name_col:
            node.data["Average"] = round(node.data["Average"], 2)
    
    
    def modify_score(self):
        cur = self.head 
        if cur is None:
            return 
        
        while cur is not None:
            self.round_score(cur)
            cur = cur.next 


    def compute_average(self, node):
        N = 3
        _sum = sum(list(node.data.values())[2:5])
        return _sum / N
    

    def add_average(self):
        cur = self.head 
        if cur is None:
            return 
        while cur is not None:
            cur.data["Average"] = self.compute_average(cur)
            cur = cur.next 


    def print_list(self):
        cur = self.head 
        if cur is None:
            return 

        while cur is not None:
            print(cur.data)
            cur = cur.next

    
    def delete_node_by_kv(self, k, v):
        cur = self.head 
        if cur is None:
            return 
        back = cur 
        cur = cur.next
        if back.data[k] == v:
            self.head = cur
        while cur is not None:
            if cur.data[k] == v:
                back.next = cur.next
                break 
            back = cur 
            cur = cur.next

    
    def size(self):
        cur = self.head 
        if cur is None:
            return 0
        size = 1
        while cur.next is not None:
            cur = cur.next 
            size += 1
        return size 
    


def file_reader(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        head = data[0].strip("\n").split(",")
        data = data[1:]
        data = [i.strip("\n").split(",") for i in data]
        return head, data


L = LinkedList(name_col=None)



def questionA(csv_name):
    head, data = file_reader(csv_name)
    L.name_col = head
    for row in data:
        tmp_data = {}
        for k, v in zip(head, row):
            if k in ["Math", "Phys", "Chem"]:
                v = float(v)
            tmp_data[k] = v
        L.add_node(tmp_data)


def questionB():
    L.modify_score()

def questionC():
    L.name_col += ["Average"]
    L.add_average()

def questionD(n, m):
    cur = L.head 
    if cur is None:
        return 
    ans = 0
    while cur is not None:
        flag = 1
        for k in ["Math", "Phys", "Chem"]:
            if cur.data[k] <= n:
                flag = 0
                break 
        if cur.data["Average"] <= m:
            flag = 0
        if flag == 1:
            ans += 1
        cur = cur.next
    return ans 


def questionE(stID):
    L.delete_node_by_kv("Student ID", stID)


def questionF(csv_name, k, m):
    head, data = file_reader(csv_name)
    for i in range(len(data)):
        data[i][0] = int(data[i][0])

    ans = list(filter(lambda row: row[0] >= k and row[0] <= m, data))
    print(ans)    


def get_dob(row):
    ans = row["DOB"]
    ans = ans.split("/")
    ans = [int(i) for i in ans]
    return ans 


def cmp(row1, row2):
    date1 = get_dob(row1)
    date2 = get_dob(row2)
    stID1 = row1["Student ID"]
    stID2 = row2["Student ID"]
    for i in range(len(date1)):
        if date2[i] < date1[i]:
            return True
    return stID1 <= stID2 


def questionH():
    tmp = L.copy()
    for i in range(len(tmp)):
        for j in range(i+1, len(tmp)):
            if cmp(tmp[i], tmp[j]):
                tmp[i], tmp[j] = tmp[j], tmp[i]
    print(tmp[:10])


def main():
    # Question a
    questionA("students.csv")

    # Question b
    questionB()

    # Question c 
    questionC()

    # Question d
    c = questionD(5,5)
    print(c)


    # Question e
    questionE("SE1820280")
    # L.print_list()

    # Question f
    questionF("students.csv", 10,15)

    questionH()


if __name__ == "__main__":
    main()