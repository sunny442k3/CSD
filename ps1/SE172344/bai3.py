
def file_reader(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        head = data[0].strip("\n").split(",")
        data = data[1:]
        data = [i.strip("\n").split(",") for i in data]
        return head, data


L = []
subject = ["Math", "Phys", "Chem"]


def questionA(csv_name):
    head, data = file_reader(csv_name)
    for row in data:
        tmp_data = {}
        for k, v in zip(head, row):
            if k in subject:
                v = float(v)
            tmp_data[k] = v
        tmp_data["No."] = int(tmp_data["No."])
        L.append(tmp_data)


def questionB():
    for i in range(len(L)):
        for k in subject:
            L[i][k] = round(L[i][k], 2)
        if "Average" in L[i]:
            L[i]["Average"] = round(L[i]["Average"], 2)

def questionC():
    for i in range(len(L)):
        avg = 0
        for k in subject:
            avg += L[i][k]
        L[i]["Average"] = avg/len(subject)


def questionD(n, m):
    tmp = L.copy()
    tmp = list(filter(lambda row: row["Average"] > m, tmp))
    for k in subject:
        tmp = list(filter(lambda row: row[k] > n, tmp))
    return len(tmp)


def questionE(stID):
    global L
    new_list = L.copy()
    new_list = list(filter(lambda row: row["Student ID"] != stID, new_list))
    L = new_list


def questionF(k, m):
    tmp = L.copy()
    tmp = list(filter(lambda row:  row["No."] >= k and row["No."] <= m,tmp))
    for i in tmp:
        print(i)   


def save_csv(csv_name, data):
    head = list(data[0].keys())
    head = ",".join(head)
    tmp_data = [head]
    for row in data:
        row = list(row.values())
        row = [str(i) for i in row]
        row = ",".join(row)
        tmp_data.append(row)
    tmp_data = "\n".join(tmp_data)
    with open(csv_name, "w") as f:
        f.write(tmp_data)
        f.close()

def questionG():
    global L
    tmp = L.copy()
    tmp.sort(key=lambda row: row["Student ID"], reverse=False)
    for i in range(len(tmp)):
        tmp[i]["No."] = i+1

    L = tmp
    save_csv("./studentID_ordered.csv", L.copy())


def get_dob(row):
    ans = row["DOB"]
    ans = ans.split("/")
    ans = [int(i) for i in ans]
    return ans 


def cmp(row1, row2):
    if row1["DOB"] == row2["DOB"]:
        return row2["Student ID"] <= row1["Student ID"]
    return row2["DOB"] <= row1["DOB"]


def questionH():
    global L
    tmp = L.copy()
    for i in range(len(tmp)-1):
        for j in range(i+1, len(tmp)):
            if cmp(tmp[i], tmp[j]) == 1:
                tmp[i], tmp[j] = tmp[j], tmp[i]
    for i in range(len(tmp)):
        tmp[i]["No."] = i+1

    L = tmp 
    save_csv("./DOB_ordered.csv", L.copy())

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

    # # Question e
    questionE("SE1820280")

    # # Question f
    questionF(10,11)

    # Question G
    questionG()


    # Question H
    questionH()



if __name__ == "__main__":
    main()