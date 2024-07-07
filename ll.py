#%%
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1 

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1 
        return True 
    
    def pop(self):
        if self.length == 0:
            return None 
        temp = self.head 
        prep = self.head 
        while (temp.next):
            prep = temp 
            temp = temp.next  
        self.tail = prep 
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
        return temp.value

    def prepend(self,value):
        new_node = Node(value)
        temp = self.head 
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head = new_node 
        self.length += 1 
        return True       

    def pop_first(self):
        if self.length == 0:
            return None 
        temp = self.head 
        self.head = self.head.next 
        temp.next = None 
        self.length -= 1 
        if self.length == 0:
            self.tail = None 
        return temp 

    def get(self,index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        return temp
    
    def set_value(self,index, value):
        temp = self.get(index)
        if temp:
            temp.value = value 
            return True 
        return False 
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node 
        self.length += 1 
        return True 
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return None 
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next 
        prev.next = temp.next 
        temp.next = None 
        self.length -= 1 
        return temp 
    
    # More study is needed!!
    def reverse(self):
        temp = self.head 
        self.head = self.tail 
        self.tail = temp 
        after = temp.next 
        before = None 
        for _ in range(self.length):
            after = temp.next 
            temp.next = before 
            before = temp 
            temp = after 
    
    def print_list(self):
        temp = self.head 
        if temp is None:
            print("[]")
        while temp is not None:
            print(temp.value)
            temp = temp.next 

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.set_value(1,4)
my_linked_list.print_list()

#%%
head = 7 
temp = head 

head = 6 
temp

