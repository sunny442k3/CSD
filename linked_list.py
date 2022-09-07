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
        
    def remove_node(self, data):
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



if __name__ == "__main__":
    ls = LinkedList()
    ls.add_node(1)
    ls.add_node(2)
    ls.add_node(5)
    ls.add_node(3)
    print(ls.get_len())
    ls.print_list()
    ls.remove_node(2)
    ls.remove_node(5)
    ls.add_node(10)
    ls.print_list()