import sys
from linked_list import LinkedList


class Stack(LinkedList):


    def __init__(self, limit=None):
        super(Stack, self).__init__()
        self.limit = limit


    def push(self, data):
        if self.limit is not None:
            if self.get_len() + 1 > self.limit:
                print("Stack overflow")
                return 
        self.add_node(data)


    def top(self):
        if self.get_len() == 0:
            print("Stack is empty")
            sys.exit()

        current_node = self.head 
        while current_node.next is not None:
            current_node = current_node.next 
        return current_node.data


    def pop(self):
        if self.get_len() == 0:
            return -1
        current_node = self.head 
        if self.get_len() == 1:
            self.head = None 
            return current_node.data

        previous_current_node = current_node 
        while current_node.next is not None:
            previous_current_node = current_node
            current_node = current_node.next 

        previous_current_node.next = None 
        return current_node.data
        

    def empty(self):
        return self.get_len() == 0


    def size(self):
        return self.get_len()


if __name__ == "__main__":
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    print(st.top())

