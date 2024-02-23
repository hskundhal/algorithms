
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
                    return False
                    
            else:
                if temp.right is not None:
                    temp = temp.right
                else:
                    return False
                    
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
    def dfs_pre_order(self ):
        results = []
        if self.root is None:
            return results
        temp = self.root
        results.append(temp.value)
        
        def traverse(temp):
            if temp.left is not None:
                results.append(temp.left.value)
                traverse(temp.left) 
            if temp.right is not None:
                results.append(temp.right.value)
                traverse(temp.right)
                
            
        traverse(temp)
        return results
    
    def dfs_post_order(self):
        results = []
        if self.root is None:
            return results
        temp = self.root
        # queue = []
        # queue.append
        def traverse(temp):
            if temp.left is not None:
                traverse(temp.left)
            if temp.right is not None:
                traverse(temp.right)
            results.append(temp.value)
        traverse(temp)
        return results
        
    def dfs_in_order(self):
        results= []
        if self.root is None:
            return results
        def traverse(temp):
            if temp.left is not None:
                traverse(temp.left)
            results.append(temp.value)
            if temp.right is not None:
                traverse(temp.right)
        traverse(self.root)
        return results
    

mytree = BinaryTree()
mytree.insert(7)
mytree.insert(1)
mytree.insert(3)
mytree.insert(8)
mytree.insert(2)
mytree.insert(5)
mytree.insert(8)
mytree.insert(2)
print(mytree.BFS())
print(mytree.dfs_pre_order())
print(mytree.dfs_post_order())
print(mytree.dfs_in_order())
print(mytree.contains(7))
print(mytree.contains(6))