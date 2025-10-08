from room import Room,process_room_number

class AVLTree:
    def __init__(self):
        self.root = None

    def insertRoom(self, room):  
        self.root = self._insert(self.root, room)

    def _insert(self, node, room):
        if node is None:
            return Node(Room(room[0], room[1]))

        key = room[0]
        if key < node.data.num:
            node.left = self._insert(node.left, room)
        else:
            node.right = self._insert(node.right, room)

        # Update height once
        lh = node.left.height if node.left else -1
        rh = node.right.height if node.right else -1
        node.height = 1 + (lh if lh > rh else rh)

        balance = rh - lh

        # Right heavy
        if balance == 2:
            if node.right and (node.right.right is None or node.right.balanceFactor() < 0):
                node.right = node.right.rotateRight()
            return node.rotateLeft()

        # Left heavy
        if balance == -2:
            if node.left and (node.left.left is None or node.left.balanceFactor() > 0):
                node.left = node.left.rotateLeft()
            return node.rotateRight()

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

    def move_room(self, method, n=0):
        if not self.root:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            node.data.num = process_room_number(method, n, node.data.num)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return self.root
    
    def removeRoom(self, roomNumber):
        self.root, removed = self._remove(self.root, roomNumber)
        return removed

    def _remove(self, node, roomNumber):
        if node is None:
            return None, None

        if roomNumber < node.data.num:
            node.left, removed = self._remove(node.left, roomNumber)
        elif roomNumber > node.data.num:
            node.right, removed = self._remove(node.right, roomNumber)
        else:
            removed = node.data
            if node.left is None:
                return node.right, removed
            if node.right is None:
                return node.left, removed

            # Find smallest in right subtree
            successor = node.right
            while successor.left:
                successor = successor.left
            node.data = successor.data
            node.right, _ = self._remove(node.right, successor.data.num)

        # Rebalance after removal
        if node:
            lh = node.left.height if node.left else -1
            rh = node.right.height if node.right else -1
            node.height = 1 + (lh if lh > rh else rh)
            balance = rh - lh
            if balance == 2:
                if node.right and node.right.balanceFactor() < 0:
                    node.right = node.right.rotateRight()
                node = node.rotateLeft()
            elif balance == -2:
                if node.left and node.left.balanceFactor() > 0:
                    node.left = node.left.rotateLeft()
                node = node.rotateRight()
        return node, removed


    def get_all(self):
        result = []
        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
        return result
    
    def search(self, room):
        node = self.root
        while node:
            if node.data.num == room:
                return node.data
            node = node.left if room < node.data.num else node.right
        return None


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