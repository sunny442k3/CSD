class Node:
    def __init__(self, head, next_node=None):
        self.head = head 
        self.next_node = next_node 

    
class LinkedList:
    def __init__(self):
        self.first_node = None

    def add_node(self, data):
        new_node = Node(data)
        if self.first_node is None:
            self.first_node = new_node 
        else:
            current_node = self.first_node 
            while current_node.next_node is not None:
                current_node = current_node.next_node 
            current_node.next_node = new_node  
        
    def remove_node(self, data):
        if self.first_node is None:
            return 
        current_node = self.first_node
        if current_node.head == data:
            self.first_node = current_node.next_node
            return 

        while current_node.next_node is not None:
            nxt_node = current_node.next_node
            if nxt_node.head == data:
                current_node.next_node = nxt_node.next_node
                return 

    def print_list(self):
        current_node = self.first_node
        if current_node is None:
            return None 
        print(current_node.head, end=" ")
        while current_node.next_node is not None:
            current_node = current_node.next_node
            print(current_node.head, end = " ")
        print()


    def get_len(self):
        if self.first_node is None:
            return 0
        len_list  = 1
        current_node = self.first_node
        while current_node.next_node is not None:
            len_list += 1
            current_node = current_node.next_node 
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