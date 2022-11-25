
class Pet:
    def __init__(self, name, age, price, _id = None):
        self.ID = _id 
        self.name = name 
        self.age = age 
        self.price = price 

    def print_info(self):
        print(f"\t ID: {self.ID}\n\t Name: {self.name}\n\t Age: {self.age}\n\t Price: {self.price}")


class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, data: Pet):
        self.data = [data] + self.data

    def dequeue(self):
        if len(self.data) == 0:
            return -1
        return self.data.pop()

    def front(self):
        if len(self.data) == 0:
            return -1
        return self.data[-1]

    def size(self):
        return len(self.data)


class PetManager:

    def __init__(self):
        self.pet_list = Queue()

    def add_pet(self, pet: Pet):
        list_id = []
        tmp = Queue()
        while self.pet_list.size():
            fq = self.pet_list.dequeue()
            tmp.enqueue(fq)
            list_id.append(fq.ID)
        list_id.sort()
        if pet.ID in list_id:
            print(f"Pet with id:{pet.ID} had in list")
            self.pet_list = tmp
            return
        if pet.ID is None:
            if len(list_id) == 0:
                pet.ID = 1
            else:
                pet.ID = list_id[-1] + 1
                for i in range(1, list_id[-1]+1):
                    if i not in list_id:
                        pet.ID = i
                        break 
        tmp.enqueue(pet)
        print("Add pet successfully")    
        self.pet_list = tmp 

    def search_by_name(self, patern):
        tmp = Queue()
        ans = []
        while self.pet_list.size():
            fq = self.pet_list.dequeue()
            if patern in fq.name:
                ans.append(fq)
            tmp.enqueue(fq)
        self.pet_list = tmp 
        return ans 
    
    def update_by_id(self, pet_info: Pet):
        fl = 0
        tmp = Queue()
        while self.pet_list.size():
            fq = self.pet_list.dequeue()
            if fq.ID == pet_info.ID:
                fq = pet_info
                fl = 1
            tmp.enqueue(fq)
        self.pet_list = tmp 
        return fl

    def delete_by_id(self, ID):
        tmp = Queue()
        fl = 0
        while self.pet_list.size():
            fq = self.pet_list.dequeue()
            if fq.ID == ID:
                fl = 1
                continue 
            tmp.enqueue(fq)
        self.pet_list = tmp
        return fl 

    

def menu():
    print(
"""
PetManagement
Choose from 1-5
1. Add a Pet in to list of Pet
2. Find pet by name
3. Update the pet information via its code or ID 
4. Delete a pet via code or ID
5. Exit the program""")
    print("-> Enter your option: ", end="")


def valid_id(ID):
    try:
        ID = int(ID)
    except:
        print("ID of pet must be integer not less than 1")
        return 0
    if ID < 1:
        print("ID of pet must be integer not less than 1")
        return 0
    return 1

def valid_age(age):
    try:
        age = int(age)
    except:
        print("Age of pet must be integer none negative")
        return 0
    if age < 0:
        print("Age of pet must be integer none negative")
        return 0
    return 1

def valid_price(price):
    try:
        price = float(price)
    except:
        print("Price of pet must be float none negative")
        return 0
    if price < 0:
        print("Price of pet must be float none negative")
        return 0
    return 1


def op1(manager: PetManager):
    ID = input("Enter ID of pet: ")

    if len(ID) != 0:
        if valid_id(ID):
            ID = int(ID)
        else:
            return 
    else:
        ID = None
    name = input("Enter name of pet: ")
    age = input("Enter age of pet: ")
    if valid_age(age):
        age = int(age)
    else:
        return 
    price = input("Enter price of pet: ")
    if valid_price(price):
        price = float(price)
    else:
        return 
    
    new_pet = Pet(name, age, price, ID)
    manager.add_pet(new_pet)

def op2(mamager: PetManager):
    name = input("Enter name of pet for searching: ")
    ans = mamager.search_by_name(name)
    if len(ans) == 0:
        print("No pet found!")
        return
    for idx, pet in enumerate(ans, 1):
        print(f"Pet {idx}")
        pet.print_info()

def op3(manager: PetManager):
    ID = input("Enter ID of pet for updating: ")
    if valid_id(ID):
        ID = int(ID)
    else:
        return 
    name = input("Enter new name of pet: ")
    age = input("Enter new age of pet: ")
    if valid_age(age):
        age = int(age)
    else:
        return 
    price = input("Enter new price of pet: ")
    if valid_price(price):
        price = float(price)
    else:
        return 
    new_pet = Pet(name, age, price, ID)
    ans = manager.update_by_id(new_pet)
    if ans:
        print("Update infomation of pet successfully")
    else:
        print(f"Pet with id:{ID} not found")


def op4(manager: PetManager):
    ID = input("Enter ID of pet for updating: ")
    if valid_id(ID):
        ID = int(ID)
    else:
        return 
    ans = manager.delete_by_id(ID)
    if ans:
        print("Delete pet successfully")
    else:
        print(f"Pet with id:{ID} not found")

def main():
    manager = PetManager()
    while 1:
        menu()
        op = input()
        try:
            op = int(op)
        except:
            print("Option must be integer from 1-5")
            continue 
        if op > 5 or op < 1:
            print("Option must be integer from 1-5")
            continue 
        if op == 5:
            print("Good bye")
            return 
        if op == 4:
            print("="*20)
            op4(manager)
            print("="*20)
        if op == 3:
            print("="*20)
            op3(manager)
            print("="*20)
        if op == 2:
            print("="*20)
            op2(manager)
            print("="*20)
        if op == 1:
            print("="*20)
            op1(manager)
            print("="*20)


if __name__ == "__main__":
    main()
