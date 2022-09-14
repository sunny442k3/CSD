class Node:

    
    def __init__(self, data, next_node=None):
        self.data = data 
        self.next = next_node 

    
class LinkedList:


    def __init__(self):
        self.head = None


    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            current_node = self.head 
            while current_node.next is not None:
                current_node = current_node.next 
            current_node.next = new_node  
        

    def remove_node_by_value(self, data):
        if self.head is None:
            return 

        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            return 

        while current_node.next is not None:
            nxt_node = current_node.next
            if nxt_node.data == data:
                current_node.next = nxt_node.next
                return 

    def print_list(self):
        current_node = self.head
        if current_node is None:
            return None 
        print(current_node.data, end=" ")
        while current_node.next is not None:
            current_node = current_node.next
            print(current_node.data, end = " ")
        print()


    def get_len(self):
        if self.head is None:
            return 0
        len_list  = 1
        current_node = self.head
        while current_node.next is not None:
            len_list += 1
            current_node = current_node.next
        return len_list 


    def count_prime_number(self):
        count = 0
        if self.head is None:
            return count 

        def is_prime(number):
            if number < 2:
                return 0
            for i in range(2, int(number**0.5)+1):
                if number % i == 0:
                    return 0
            return 1

        current_node = self.head
        while 1:
            if isinstance(current_node.data, int):
                if is_prime(current_node.data):
                    count += 1
            if current_node.next is None:
                break 
            current_node = current_node.next

        return count


if __name__ == "__main__":
    ls = LinkedList()
    ls.add_node(5)
    ls.add_node(9)
    ls.add_node(11)
    ls.add_node("java")
    ls.add_node(12.3)
    ls.add_node(16)
    ls.add_node(31)
    print("The number of prime number in linked list is:", ls.count_prime_number())
    # print("Length is:",ls.get_len())