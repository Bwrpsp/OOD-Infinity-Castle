from room import Room,process_room_number

class AVLTree:
    def __init__(self):
        self.root = None

    def insertRoom(self, room):  
        self.root = self._insert(self.root, room)

    def _insert(self, node, room):
        if not node:
            return Node(Room(room[0], room[1]))
        elif room[0] >= node.data.num:
            node.right = self._insert(node.right,room)
        elif room[0] < node.data.num:
            node.left = self._insert(node.left,room)

        
        node = self.balance(node)
        return node
    
    def balance(self, node):
        node.setHeight()
        balance = node.balanceFactor()

        # Right heavy
        if balance == 2:
            if node.right and node.right.balanceFactor() < 0:
                node.right = node.right.rotateRight()
            node = node.rotateLeft()

        # Left heavy
        elif balance == -2:
            if node.left and node.left.balanceFactor() > 0:
                node.left = node.left.rotateLeft()
            node = node.rotateRight()

        node.setHeight()
        return node

    def move_room(self,method,n=0):
        return self._move_room(self.root,method,n)
    
    def _move_room(self,node,method,n):
        if not node:
            return
        
        node.data.num = process_room_number(method, n, node.data.num)

        node.left = self._move_room(node.left,method,n)
        node.right = self._move_room(node.right,method,n)

        return node 
    
    def removeRoom(self, roomNumber):
        self.root, removed = self._remove(self.root, roomNumber)
        return removed

    def _remove(self, node, roomNumber):
        if not node:
            return node, None  

        if roomNumber < node.data.num:
            node.left, removed = self._remove(node.left, roomNumber)
        elif roomNumber > node.data.num:
            node.right, removed = self._remove(node.right, roomNumber)
        else:
            removed = node.data  
            
            if not node.left:
                return node.right, removed
            elif not node.right:
                return node.left, removed

            successor = node.right
            while successor.left:
                successor = successor.left

            node.data = successor.data
            node.right, _ = self._remove(node.right, successor.data.num)

        return node, removed


    def get_all(self):
        return self._get_all(self.root)
    
    def _get_all(self,node):
        if not node:
            return []
        return self._get_all(node.left) + [node.data] + self._get_all(node.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return f'{self.data}'
    
    def balanceFactor(self):    #Get balance factor
        if not self:
            return -1
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return right_height - left_height
    
    def setHeight(self):        #Set height base on child node
        a = self.left.height if self.left else -1  
        b = self.right.height if self.right else -1
        self.height = 1 + max(a,b)

    def rotateRight(self):      #Rotate right (clockwise)
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self.setHeight()
        new_root.setHeight()
        return new_root
    
    def rotateLeft(self):       #Rotate left (counter-clockwise)
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self.setHeight()
        new_root.setHeight()
        return new_root