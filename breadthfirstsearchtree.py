# queue
# results





class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left= new_node
                    return True
            else :
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value == temp.value:
                return True
            if value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                    
            else:
                if temp.right is not None:
                    temp = temp.right
                    
        return False
    
            
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue)> 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results




mytree = BinaryTree()
mytree.insert(5)
print(mytree.insert(3))
print(mytree.insert(5))

print(mytree.contains(5))
print(mytree.BFS())
print(mytree.insert(2))
print(mytree.BFS())
mytree.insert(4)
mytree.insert(6)
print(mytree.BFS())