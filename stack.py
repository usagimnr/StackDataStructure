########################################
#                                      
# A stack linear data structure.
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:

    def __init__(self):
        self.top = None
        self.count = 0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        if self.top == None:
            return True 
        else: 
            return False

    def __len__(self):
        return self.count

    
    def peek(self):
        if self.top == None:
            return 'Stack is empty'
        else: 
            return self.top.value

    def push(self,value):
        nn = Node(value)
        nn.next = self.top
        self.top = nn 
        self.count += 1

    def pop(self):
        if self.top == None:
            return 'Stack is empty'
        else: 
            x = self.top.value
            self.top = self.top.next 
            self.count -= 1
            return x
